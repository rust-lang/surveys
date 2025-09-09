from pathlib import Path
from typing import Optional

from .survey import SurveyReport, SurveyFullAnswers


def print_question_index(path: Path, new: SurveyReport, old: Optional[SurveyReport] = None):
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


def print_answer_index(answers: SurveyFullAnswers, report: SurveyReport, path: Path):
    with open(path, "w") as f:
        for (index, question) in enumerate(answers.questions):
            if any(question == q.question for q in report.questions) and index > 0:
                print(file=f)
            print(f"{index}: {question}", file=f)
