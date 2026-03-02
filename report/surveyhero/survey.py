import dataclasses
import re
from collections import defaultdict
from typing import List, Union, Dict, Optional, Callable, Iterable, Set

import numpy as np
import pandas as pd


@dataclasses.dataclass
class Answer:
    answer: str
    count: int


@dataclasses.dataclass
class SimpleQuestion:
    answers: List[Answer]

    def rename_answers(self, diff: Dict[str, Optional[str]]) -> "SimpleQuestion":
        diff = dict(diff)

        answers = []
        for answer in self.answers:
            if answer.answer in diff:
                updated = diff.pop(answer.answer)
                if updated is None:
                    continue
                answer = dataclasses.replace(answer, answer=updated)
            answers.append(answer)
        if len(diff) != 0:
            raise Exception(f"Some diffs were not applied: {diff}\nAnswers: {self.answers}")
        return dataclasses.replace(self, answers=answers)


@dataclasses.dataclass
class MatrixQuestion:
    answer_groups: Dict[str, List[Answer]]

    def rename_answers(self, diff: Dict[str, str]) -> "MatrixQuestion":
        diff = dict(diff)

        answer_groups = {}
        for (group, items) in self.answer_groups.items():
            if group in diff:
                group = diff.pop(group)
            answer_groups[group] = items
        if len(diff) > 0:
            raise Exception(f"Rename answers diff not empty: {diff}. Answers: {self.answer_groups}")
        return dataclasses.replace(self, answer_groups=answer_groups)


@dataclasses.dataclass
class RatingAnswer:
    answer: Answer
    rating: int


@dataclasses.dataclass
class RatingQuestion:
    answers: List[RatingAnswer]

    def rename_answers(self, _diff: Dict[str, str]) -> "RatingQuestion":
        return self


QuestionKind = Union[SimpleQuestion, MatrixQuestion, RatingQuestion]


@dataclasses.dataclass
class Question:
    id: int
    year: int
    question: str
    total_responses: int
    kind: QuestionKind

    def is_simple(self) -> bool:
        return isinstance(self.kind, SimpleQuestion)

    def is_matrix(self) -> bool:
        return isinstance(self.kind, MatrixQuestion)

    def is_single_answer(self) -> bool:
        if isinstance(self.kind, SimpleQuestion):
            return sum(answer.count for answer in self.kind.answers) == self.total_responses
        elif isinstance(self.kind, MatrixQuestion):
            return False
        else:
            assert False

    def combine_answers(self, diff: Dict[str, List[str]]) -> "Question":
        assert self.is_simple()

        orig_count = sum(a.count for a in self.kind.answers)
        answers_orig = {a.answer: a for a in self.kind.answers}
        answers = []
        for (target, old_answers) in diff.items():
            count = 0
            for answer in old_answers:
                if answer not in answers_orig:
                    raise Exception(f"Answer {answer} not in {answers_orig}")
                count += answers_orig[answer].count
                answers_orig.pop(answer)
            assert count > 0
            answers.append(Answer(answer=target, count=count))
        answers.extend(answers_orig.values())

        answer_texts = {a.answer: index for (index, a) in enumerate(self.kind.answers)}
        answers = sorted(answers, key=lambda a: (
            answer_texts.get(a.answer, 999),
            a.answer
        ))
        assert orig_count == sum(a.count for a in answers)
        return dataclasses.replace(self, kind=SimpleQuestion(answers=answers))

    def integer_answers(self) -> "Question":
        assert self.is_simple()
        return dataclasses.replace(self, kind=SimpleQuestion(answers=[
            Answer(answer=str(int(float(answer.answer))), count=answer.count) for answer in
            self.kind.answers
        ]))

    def expand_answers(self, func: Callable[[str], Iterable[str]]) -> "Question":
        assert self.is_simple()

        answers = defaultdict(int)
        for answer in self.kind.answers:
            for answer in list(func(answer.answer)):
                answers[answer] += 1
        return dataclasses.replace(self, kind=SimpleQuestion(answers=[
            Answer(answer, count) for (answer, count) in sorted(answers.items(), key=lambda i: i[0])
        ]))

    def filter_answers(self, func: Callable[[Answer], bool]) -> "Question":
        assert self.is_simple()

        answers = []
        for answer in self.kind.answers:
            if func(answer):
                answers.append(answer)
        return dataclasses.replace(self, kind=SimpleQuestion(answers=answers))

    def rename_answers(self, diff: Dict[str, Optional[str]]) -> "Question":
        return dataclasses.replace(self, kind=self.kind.rename_answers(diff))

    def add_open(self, open_answers: List[str], id: str, label: str, replace="Other") -> "Question":
        """
        Adds a open answer with the normalized `id` under `label` to this question.
        The count added from the open answer will reduce the count present in the `replace` answer.
        """
        assert self.is_simple()
        aggregated = pd.Series(open_answers).value_counts()
        added_count = 0
        for key in aggregated.index:
            if id in key:
                added_count += int(aggregated[key])
        assert added_count > 0

        answers = []
        replaced = False
        added = False
        for answer in self.kind.answers:
            count = answer.count
            if answer.answer == replace:
                count -= added_count
                assert not replaced
                replaced = True
            elif answer.answer == label:
                assert not added
                count += added_count
                added = True
            answers.append(dataclasses.replace(answer, count=count))
        assert replaced
        if not added:
            answers.append(Answer(answer=label, count=added_count))
        return dataclasses.replace(self, kind=SimpleQuestion(answers=answers))

    def with_title(self, func: Callable[[str], str]) -> "Question":
        return Question(
            id=self.id,
            year=self.year,
            question=func(self.question),
            total_responses=self.total_responses,
            kind=self.kind
        )


def rating_to_simple_question(question: Question) -> Question:
    assert isinstance(question.kind, RatingQuestion)
    return Question(
        id=question.id,
        year=question.year,
        total_responses=question.total_responses,
        question=question.question,
        kind=SimpleQuestion(answers=[Answer(answer=str(a.rating), count=a.answer.count) for a in
                                     question.kind.answers])
    )


@dataclasses.dataclass
class SurveySummary:
    year: int
    questions: List[Question]

    def q(self, index: int) -> Question:
        return self.questions[index]

    def q_by_text(self, question_text: str) -> Question:
        for question in self.questions:
            if question.question == question_text:
                return question
        raise Exception(f"Question with text `{question_text}` not found")


@dataclasses.dataclass()
class Column:
    name: str
    index: int
    data: pd.Series


@dataclasses.dataclass
class SurveyFullAnswers:
    year: int
    # Question index -> list of open answers
    answers: Dict[int, List[str]]
    questions: List[str]
    total_respondents: int
    df: pd.DataFrame
    summary: Optional[SurveySummary] = None

    def q_simple_single(self, question_or_id: int | str,
                        treat_unknown_answers_as: Optional[str] = "Other") -> Question:
        col = self.get_column(question_or_id)
        response_count = np.sum(col.data.count())

        ref_question = self.get_summary_question(col.name)
        if ref_question is not None:
            assert ref_question.is_simple() and ref_question.is_single_answer()

        counts = dict(col.data.value_counts())

        answers = self.sort_answers(counts, col)
        question = Question(
            id=col.index,
            year=self.year,
            question=col.name,
            total_responses=response_count,
            kind=SimpleQuestion(
                answers=answers
            )
        )
        if treat_unknown_answers_as is not None and self.get_summary_question(col.name) is not None:
            question = self.treat_unknown_answers_as(
                question,
                treat_unknown_answers_as=treat_unknown_answers_as
            )
        return question

    def q_simple_multi(self, question_or_id: int | str,
                       answer_count: Optional[int] = None) -> Question:
        col = self.get_column(question_or_id)
        answer_data = self.get_answer_columns(col, answer_count=answer_count)
        if answer_count is None:
            for c in answer_data.columns:
                assert not c.endswith("?")
        non_na_answers = answer_data.apply(lambda r: r.count(), axis=1)
        response_count = len(non_na_answers[non_na_answers != 0])

        ref_question = self.get_summary_question(col.name)
        if ref_question is not None:
            assert ref_question.is_simple() and not ref_question.is_single_answer()
            answer_data = normalize_answers(ref_question, answer_data)

        counts = dict(answer_data.count())
        answers = self.sort_answers(counts, col)
        return Question(
            id=col.index,
            year=self.year,
            question=col.name,
            total_responses=response_count,
            kind=SimpleQuestion(
                answers=answers
            )
        )

    def open_answers(self, question_or_id: int | str) -> List[str]:
        col = self.get_column(question_or_id)
        ref_question = self.get_summary_question(col.name)

        if ref_question is not None:
            if ref_question.is_single_answer():
                known_answers = set(answer.answer for answer in ref_question.kind.answers)
                answer_data = list(col.data.dropna())
                return [answer for answer in answer_data if answer not in known_answers]
            else:
                answer_data = self.get_answer_columns(col, answer_count=None)
                answer_data = answer_data.rename(columns={
                    k: normalize_answer_other(k)
                    for k in answer_data.columns.values
                })
                return list(answer_data["Other"].dropna())
        else:
            return list(col.data.dropna())

    def open_answers_raw(self, question_or_id: int | str, dropna=True) -> List[str]:
        df = self.df[self.get_column(question_or_id).name]
        if dropna:
            df = df.dropna()
        return list(df)

    def treat_unknown_answers_as(self, question: Question, treat_unknown_answers_as: str):
        assert question.is_simple()

        answer_map = {answer.answer: index for (index, answer) in enumerate(question.kind.answers)}
        if treat_unknown_answers_as not in answer_map:
            answer_map[treat_unknown_answers_as] = len(answer_map)

        ref_question = self.get_summary_question(question.question)
        assert ref_question is not None
        ref_keys = set([answer.answer for answer in ref_question.kind.answers])

        counts = {answer.answer: answer.count for answer in question.kind.answers}
        unknown_keys = [k for k in counts if k not in ref_keys]
        other_count = counts.get(treat_unknown_answers_as, 0)
        for key in unknown_keys:
            other_count += counts.pop(key)
        if other_count > 0:
            counts[treat_unknown_answers_as] = other_count
        answers = sorted(counts.items(), key=lambda i: answer_map[i[0]])
        return dataclasses.replace(question, kind=SimpleQuestion(
            answers=[Answer(answer=answer, count=count) for
                     (answer, count) in answers]))

    def get_answer_columns(self, col: Column, answer_count: Optional[int]) -> pd.DataFrame:
        ref_question = self.get_summary_question(col.name)
        if answer_count is None:
            if ref_question is None:
                raise Exception(
                    f"Must provide either `answer_count` or a summary thas has the question `{col.name}`")
            if ref_question.is_simple():
                answer_count = len(ref_question.kind.answers)
            elif ref_question.is_matrix():
                answer_count = len(ref_question.kind.answer_groups)
            else:
                raise Exception(f"Unsupported question type: {ref_question}")

        return self.df.iloc[:, col.index + 1:col.index + 1 + answer_count]

    def get_column(self, question_or_id: int | str) -> Column:
        if isinstance(question_or_id, int):
            col_name = self.df.iloc[:, question_or_id].name
            col_index = question_or_id
        else:
            col_name = question_or_id
            col_index = self.df.columns.get_loc(question_or_id)
        col_data = self.df[col_name]
        return Column(name=col_name, index=col_index, data=col_data)

    def get_summary_question(self, col_name: str) -> Optional[Question]:
        if self.summary is not None:
            ref_questions = [q for q in self.summary.questions if q.question == col_name]
            if ref_questions:
                assert len(ref_questions) == 1
                return ref_questions[0]
        return None

    def sort_answers(self, counts: Dict[str, int], col: Column) -> List[Answer]:
        ref_question = self.get_summary_question(col.name)
        answer_map = {}
        if ref_question is not None:
            assert isinstance(ref_question.kind, SimpleQuestion)
            answer_map = {a.answer: i for (i, a) in enumerate(ref_question.kind.answers)}

        answers = [(normalize_answer_other(str(answer)), count) for (answer, count) in
                   counts.items()]
        for (index, (answer, _)) in enumerate(answers):
            if answer not in answer_map:
                answer_map[answer] = index
        answers = sorted(answers, key=lambda i: answer_map[i[0]])
        return [Answer(answer=str(answer), count=count) for (answer, count) in answers]


OTHER_REGEX = re.compile("^Other(\.\d+)?$")


def normalize_answer_other(answer: str) -> str:
    if OTHER_REGEX.match(answer) is not None:
        return "Other"
    if answer.startswith("Other "):
        return "Other"
    return answer


RENUMBERED_ANSWER_REGEX = re.compile("^(.+?)\.\d+$")


def normalize_answers(ref_question: Question, answer_data: pd.DataFrame) -> pd.DataFrame:
    """
    When multiple questions have the same answers, the answers will be parsed as `<answer>.1`,
    `<answer.2>`, etc. by pandas.
    If we have the reference question available, try to normalize the answers based on it.
    """
    answers: Set[str] = set(answer.answer for answer in ref_question.kind.answers)
    data = defaultdict(list)
    for col in answer_data.columns:
        answer_col = answer_data[col]
        if col not in answers:
            match = RENUMBERED_ANSWER_REGEX.match(col)
            if match:
                col = match.group(1)
            else:
                raise Exception(
                    f"Answer `{col}` not found in answers `{sorted(answers)}`\nof question {ref_question}")

        data[col] = answer_col

    return pd.DataFrame(data)


def normalize_open_answers(answers: List[str], replace_spaces=False) -> List[str]:
    new_answers = list()
    for answer in answers:
        answer = answer.lower().strip()
        if replace_spaces:
            answer = answer.replace(" ", "-")
        answer = answer.replace("rust", "").strip()
        new_answers.append(answer)
    return new_answers
