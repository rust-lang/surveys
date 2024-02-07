import csv
import re
from collections import defaultdict
from pathlib import Path

from .survey import SurveyFullAnswers, Question, MatrixQuestion, Answer, SimpleQuestion, SurveyReport


def parse_full_answers(path: Path, year: int) -> SurveyFullAnswers:
    """
    Parses the full CSV from SurveyHero,
    which contains all responses from individual respondents (except
    for sensitive data, which should have been filtered after export
    from SH).
    """
    answers = defaultdict(list)
    with open(path) as f:
        reader = csv.reader(f)
        questions = next(reader)
        total_respondents = 0

        for line in reader:
            total_respondents += 1
            for (id, answer) in enumerate(line):
                answer = answer.strip()
                if answer:
                    answers[id].append(answer)
    return SurveyFullAnswers(
        year=year,
        answers=answers,
        questions=questions,
        total_respondents=total_respondents
    )


COUNT_REGEX = re.compile(r" \(n = (\d+)\)$")


def parse_surveyhero_report(path: Path, year: int) -> SurveyReport:
    """
    Parses the report CSV from SurveyHero,
    which contains aggregated response counts for individual answers.
    """
    with open(path) as f:
        active_question = None
        questions = []

        for row in csv.reader(f):
            if row and "Answer" in row:
                if active_question is not None:
                    questions.append(active_question)
                question = row[0]
                kind = SimpleQuestion(answers=[])
                if row[1] == "Row":
                    kind = MatrixQuestion(answer_groups=defaultdict(list))

                count = int(COUNT_REGEX.search(question).group(1))
                question = question[:question.rindex("(")].strip()
                active_question = Question(
                    id=len(questions),
                    year=year,
                    question=normalize_question(question),
                    total_responses=count,
                    kind=kind
                )
            else:
                assert active_question is not None

                if all(r == "" for r in row):
                    # Empty row
                    continue
                elif "Average" in row or "Standard Deviation" in row:
                    # Statistics
                    continue
                else:
                    if isinstance(active_question.kind, SimpleQuestion):
                        answer = row[1]
                        count = int(row[2])
                        active_question.kind.answers.append(Answer(
                            answer=normalize_answer(answer),
                            count=count,
                        ))
                    elif isinstance(active_question.kind, MatrixQuestion):
                        group = normalize_answer(row[1])
                        answer = row[2]
                        count = int(row[3])
                        active_question.kind.answer_groups[group].append(Answer(
                            answer=normalize_answer(answer),
                            count=count,
                        ))
                    else:
                        print(row)
                        assert False
        if active_question is not None:
            questions.append(active_question)
    return SurveyReport(
        questions=questions,
        year=year
    )


def normalize_question(question: str) -> str:
    return question.lstrip("- ").strip()


def normalize_answer(answer: str) -> str:
    return answer.rstrip(".").strip()
