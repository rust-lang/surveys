import dataclasses
from typing import List, Union, Dict, Optional, Callable

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
        for answer in self.kind.answers:
            count = answer.count
            if answer.answer == replace:
                count -= added_count
                assert not replaced
                replaced = True
            answers.append(dataclasses.replace(answer, count=count))
        assert replaced
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
class SurveyReport:
    year: int
    questions: List[Question]

    def q(self, index: int) -> Question:
        return self.questions[index]


@dataclasses.dataclass
class SurveyFullAnswers:
    year: int
    # Question index -> list of open answers
    answers: Dict[int, List[str]]
    questions: List[str]
    total_respondents: int


def normalize_open_answers(answers: List[str], replace_spaces=False) -> List[str]:
    new_answers = list()
    for answer in answers:
        answer = answer.lower().strip()
        if replace_spaces:
            answer = answer.replace(" ", "-")
        answer = answer.replace("rust", "").strip()
        new_answers.append(answer)
    return new_answers
