import dataclasses
from typing import List, Union, Dict

import pandas as pd


@dataclasses.dataclass
class Answer:
    answer: str
    count: int


@dataclasses.dataclass
class SimpleQuestion:
    answers: List[Answer]


@dataclasses.dataclass
class MatrixQuestion:
    answer_groups: Dict[str, List[Answer]]


QuestionKind = Union[SimpleQuestion, MatrixQuestion]


@dataclasses.dataclass
class Question:
    id: int
    year: int
    question: str
    total_responses: int
    kind: QuestionKind

    def is_simple(self) -> bool:
        return isinstance(self.kind, SimpleQuestion)

    def combine_answers(self, diff: Dict[str, List[str]]) -> "Question":
        assert self.is_simple()

        orig_count = sum(a.count for a in self.kind.answers)
        answers_orig = {a.answer: a for a in self.kind.answers}
        answers = []
        for (target, old_answers) in diff.items():
            count = 0
            for answer in old_answers:
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

    def rename_answers(self, diff: Dict[str, str]) -> "Question":
        assert self.is_simple()
        diff = dict(diff)

        answers = []
        for answer in self.kind.answers:
            if answer.answer in diff:
                answer = dataclasses.replace(answer, answer=diff.pop(answer.answer))
            answers.append(answer)
        assert len(diff) == 0
        return dataclasses.replace(self, kind=SimpleQuestion(answers=answers))

    def add_open(self, open_answers: List[str], id: str, label: str, replace="Other") -> "Question":
        """
        Adds a open answer with the normalized `id` under `label` to this question.
        The count added from the open answer will reduce the count present in the `replace` answer.
        """
        assert self.is_simple()
        aggregated = pd.Series(open_answers).value_counts()
        added_count = int(aggregated[id])
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
