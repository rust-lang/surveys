from collections import defaultdict
from pathlib import Path
from typing import Optional, Any, List

import numpy as np
from plotly.graph_objs import Figure

from .survey import SurveySummary, SurveyFullAnswers, Question, SimpleQuestion


def print_answers(a: Question, b: Question):
    assert isinstance(a.kind, SimpleQuestion)
    assert isinstance(b.kind, SimpleQuestion)

    a_answers = set(a.answer for a in a.kind.answers)
    b_answers = set(a.answer for a in b.kind.answers)
    answers = a_answers | b_answers
    for answer in sorted(answers):
        has_a = answer in a_answers
        has_b = answer in b_answers
        print(answer, has_a, has_b)


def print_question_index(path: Path, new: SurveySummary, old: Optional[SurveySummary] = None):
    if old is not None:
        old_index = 0
        new_index = 0

        with open(path, "w") as f:
            while old_index < len(old.questions) or new_index < len(new.questions):
                if old_index < len(old.questions):
                    old_q = old.questions[old_index]
                    print(f"{old.year}/{old_index}: {old_q.question}", file=f)
                    old_index += 1
                if new_index < len(new.questions):
                    new_q = new.questions[new_index]
                    print(f"{new.year}/{new_index}: {new_q.question}", file=f)
                    new_index += 1
    else:
        with open(path, "w") as f:
            for (index, question) in enumerate(new.questions):
                kind = question.kind.__class__.__name__
                print(f"{new.year}/{index} ({kind}): {question.question}", file=f)


def print_answer_index(answers: SurveyFullAnswers, report: SurveySummary, path: Path):
    with open(path, "w") as f:
        for (index, question) in enumerate(answers.questions):
            if any(question == q.question for q in report.questions) and index > 0:
                print(file=f)
            print(f"{index}: {question}", file=f)


def inspect_open_answers(answers: List[str]):
    normalized = defaultdict(int)
    for answer in answers:
        answer = answer.strip().lower()
        normalized[answer] += 1
    items = sorted(normalized.items(), key=lambda x: x[1], reverse=True)
    for (value, count) in items:
        print(f"{value}: {count}")


def is_nan(value: Any) -> bool:
    return isinstance(value, float) and np.isnan(value)


def update_facet_title(annotation):
    original = annotation.text
    new_text = original.split("=")[-1]
    annotation.update(text=new_text)


def shorten_annotations(fig: Figure) -> Figure:
    fig.for_each_annotation(update_facet_title)
    return fig
