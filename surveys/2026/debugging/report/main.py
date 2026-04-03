import random
import sys
from collections import defaultdict
from pathlib import Path
from typing import List

import numpy as np

ROOT_DIR = Path(__file__).absolute().parent.parent.parent.parent.parent
"""
This should resolve to the path of the surveys repository as a whole.
"""

REPORT_SCRIPT_DIR = ROOT_DIR / "report"
"""
This should resolve to the path of the directory containing the report library.
This is typically the directory that contains `.venv` after `uv sync`, and is
also typically where the `pyproject.toml` is contained.
"""

sys.path.insert(0, str(REPORT_SCRIPT_DIR))

# TODO: At runtime, only the `surveyhero.*` imports work. In my editor (VSCodium
# + `ty` extension), only the `report.surveyhero.*` imports work. The below hack
# is ugly, but it gets me the best of both worlds. Ideally, I think we should
# find a way to set things up in the project such that imports "just work", at
# runtime and in editors, without dynamically adding the import path.
try:
    from report.surveyhero.parser import (
        parse_surveyhero_answers,
        parse_surveyhero_summary,
    )
    from report.surveyhero.render import render_report_to_pdf
    from report.surveyhero.report import ChartReport
    from report.surveyhero.survey import (
        MatrixQuestion,
        Question,
        RatingQuestion,
        SimpleQuestion,
        SurveyFullAnswers,
        SurveySummary,
    )
except ModuleNotFoundError:
    from surveyhero.parser import (  # ty:ignore[unresolved-import]
        parse_surveyhero_answers,
        parse_surveyhero_summary,
    )
    from surveyhero.render import (  # ty:ignore[unresolved-import]
        render_report_to_pdf,
    )
    from surveyhero.report import ChartReport  # ty:ignore[unresolved-import]
    from surveyhero.survey import (  # ty:ignore[unresolved-import]
        MatrixQuestion,
        Question,
        RatingQuestion,
        SimpleQuestion,
        SurveyFullAnswers,
        SurveySummary,
    )


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


def print_question_index(old: SurveySummary, new: SurveySummary, path: Path):
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


def print_answer_index(
    answers: SurveyFullAnswers, report: SurveySummary, path: Path
):
    with open(path, "w") as f:
        for index, question in enumerate(answers.questions):
            if (
                any(question == q.question for q in report.questions)
                and index > 0
            ):
                print(file=f)
            print(f"{index}: {question}", file=f)


def inspect_open_answers(answers: List[str]):
    normalized = defaultdict(int)
    for answer in answers:
        answer = answer.strip().lower()
        normalized[answer] += 1
    items = sorted(normalized.items(), key=lambda x: x[1], reverse=True)
    for value, count in items:
        print(f"{value}: {count}")


# TODO: The original copied version of this function assumed any `Question.kind`
# has an `answers` field. This is not true of `MatrixQuestion`. It also relied
# on `is_simple` to ensure both questions are the same kind, which only really
# works if there are only two kinds of question. There seem to be a lot of
# mistakes of this variety in the report library itself, where the `Question`
# type is treated as though `MatrixQuestion` does not exist. Maybe those should
# be fixed?
def assert_same(q_summary: Question, q_answers: Question):
    assert q_summary.question == q_answers.question
    assert type(q_summary.kind) is type(q_answers.kind)
    match q_summary.kind:
        case SimpleQuestion() | RatingQuestion():
            assert isinstance(q_answers.kind, SimpleQuestion) or isinstance(
                q_answers.kind, RatingQuestion
            )
            assert q_summary.kind.answers == q_answers.kind.answers  # ty:ignore[unresolved-attribute] this is only thrown with the import hack
        case MatrixQuestion():
            assert isinstance(q_answers.kind, MatrixQuestion)
            assert q_summary.kind.answer_groups == q_answers.kind.answer_groups
        case _:
            raise NotImplementedError(
                f"assert_same doesn't know how to handle the QuestionKind {type(q_summary.kind)}"
            )

    assert q_summary.is_single_answer() == q_answers.is_single_answer()


# TODO: including_secret_data is currently unused. Figure out what information
# qualifies as "secret data" and decide if it can be removed.
def analyze(including_secret_data: bool) -> ChartReport:
    summary = parse_surveyhero_summary(
        Path(ROOT_DIR / "data/2026/debugging-summary.csv"), year=2026
    )
    db = parse_surveyhero_answers(
        Path(ROOT_DIR / "data/2026/debugging-responses.csv"),
        year=2026,
        summary=summary,
    )

    report = ChartReport()

    # TODO: Should this be a bar chart instead? One of the responses makes up a
    # very small percentage of the total responses, so the label is very small.
    # On the one hand, this hurts readability. On the other hand, I feel like a
    # pie chart does a very good job of visually conveying the data.
    expertise = "How would you rate your Rust expertise?"
    report.add_pie_chart(
        "how-would-you-rate-your-rust-expertise",
        db.q_simple_single(expertise),
        legend_order=[
            "I have never used Rust",
            "Beginner",
            "Intermediate",
            "Advanced",
        ],
    )

    rust_user = "Do you currently use Rust?"
    report.add_pie_chart(
        "do-you-currently-use-rust",
        db.q_simple_single(rust_user),
    )

    # TODO: Figure out the best way, if any, to merge responses with those from
    # the did-you-use-debuggers-in-rust variant. (Maybe these are best as
    # separate charts?)
    debugger_user = "Do you use debuggers in Rust?"
    report.add_pie_chart(
        "do-you-use-debuggers-in-rust",
        db.q_simple_single(debugger_user),
    )

    debugger_user_past = "Did you use debuggers in Rust?"
    report.add_pie_chart(
        "did-you-use-debuggers-in-rust",
        db.q_simple_single(debugger_user_past),
    )

    quit_because_of_debuggers = "Were issues with debugging support the primary reason why you stopped using Rust?"
    report.add_pie_chart(
        "were-issues-with-debugging-support-the-primary-reason-why-you-stopped-using-rust",
        db.q_simple_single(quit_because_of_debuggers),
    )

    other_languages_diff = {
        "No, I don't currently use debuggers in other programming languages, but I have in the past": "Not anymore",
        "No, I have never used debuggers in other programming languages": "No, never",
    }
    other_languages = "Do you use debuggers in other programming languages?"
    report.add_pie_chart(
        "do-you-use-debuggers-in-other-programming-languages",
        db.q_simple_single(other_languages).rename_answers(
            other_languages_diff  # ty:ignore[invalid-argument-type] TODO: I think this is a mistake in the type signature of `SimpleQuestion.rename_answers`.
        ),
    )

    # TODO: I find this chart difficult to interpret. I think this should either
    # be replaced or accompanied by a bar chart or some other chart, possibly
    # multiple. I want to better represent information such as:
    # - Of all responses, X% of users use the specific combo "Debugger" + "OS"
    # - Of all responses for "Debugger", X% of users did so on "OS"
    # - Of all responses for "Debugger", X% of users selected more than one "OS"
    # - Of all responses for "OS", X% of users used "Debugger"
    # - Of all responses for "OS", X% of users selected more than one "Debugger"
    # Where "Debugger" is a specific choice of the tool/debugger response and
    # "OS" is a specific choice of the OS response. I don't think all of these
    # questions absolutely need to be answered, but they are the kinds of
    # questions I initially think of for this data, and I don't feel like most
    # of these are represented well, if at all, by the existing chart. If any
    # are, I think it'd be "Of all responses for 'Debugger', X% of users did so
    # on 'OS'".
    os_and_debugger = "What tools and workflows do you use to debug Rust programs on which operating systems?"
    report.add_matrix_chart(
        "what-tools-and-workflows-do-you-use-to-debug-rust-programs-on-which-operating-systems",
        summary.q_by_text(os_and_debugger),
        horizontal=True,
        # TODO: With textpositon="inside", I can't read the percentages for
        # (IDK/OTHER) or (Visual Studio Debugger/OTHER), and can barely read
        # (dbg!/OTHER), (lldb(IDE)/OTHER), and (WinDbg/WSL). Without it, I can't
        # read the percentage for (WinDbg/WSL). Can I make them all fairly easy
        # to read somehow?
        # textposition="inside",
        legend_params=dict(
            orientation="h",
            y=-0.05,
        ),
    )

    # TODO: Some of the most prominent words produced in the wordcloud are very
    # generic, especially given the context of the survey and question ("use",
    # "debugger", "debugging", etc.). Is this something we want to filter for?
    # If so, how should we go about it?
    other_debuggers = "What other debuggers or workflows do you use?"
    other_debuggers_responses = db.open_answers_raw(other_debuggers)
    with open(
        Path(__file__).parent / "open-response-other-debuggers.txt", "w"
    ) as f:
        for answer in other_debuggers_responses:
            f.write(f"{answer}\n---\n\n")
    report.add_wordcloud(
        "what-other-debuggers-or-workflows-do-you-use-wordcloud",
        db.open_answers(other_debuggers),
    )

    debugger_used_for_diff = {
        "Getting stack traces from hung/crashed processes": "Stack traces",
    }
    debugger_used_for = "What are you using debuggers for?"
    report.add_bar_chart(
        "what-are-you-using-debuggers-for",
        db.q_simple_multi(debugger_used_for).rename_answers(
            debugger_used_for_diff  # ty:ignore[invalid-argument-type] TODO: I think this is a mistake in the type signature of `SimpleQuestion.rename_answers`.
        ),
        xaxis_tickangle=45,
    )
    debugger_used_for_responses = db.open_answers(debugger_used_for)
    with open(
        Path(__file__).parent / "open-response-debugger-used-for.txt", "w"
    ) as f:
        for answer in debugger_used_for_responses:
            f.write(f"{answer}\n---\n\n")
    # TODO: Similarly to the previous wordcloud related TODO, does it really
    # provide any value to know that one of the most prominent words in answers
    # to a question about "what you use debuggers for" is "debugging"?
    report.add_wordcloud(
        "what-are-you-using-debuggers-for-wordcloud",
        db.open_answers(debugger_used_for),
    )

    multilingual = "Do you debug programs that combine Rust with any of the following languages?"
    report.add_bar_chart(
        "do-you-debug-programs-that-combine-rust-with-any-of-the-following-languages",
        db.q_simple_multi(multilingual),
        xaxis_tickangle=45,
    )
    multilingual_responses = db.open_answers(multilingual)
    with open(
        Path(__file__).parent / "open-response-multilingual.txt", "w"
    ) as f:
        for answer in multilingual_responses:
            f.write(f"{answer}\n---\n\n")
    report.add_wordcloud(
        "do-you-debug-programs-that-combine-rust-with-any-of-the-following-languages-wordcloud",
        db.open_answers(multilingual),
    )

    # Because the answers to the question ended in periods, the report library
    # was unable to process these responses. The usual "rename" method did not
    # resolve it, so this requires patching the dataframe directly.
    debugger_difficulties_diff = {
        "I don't need to debug because my code works.": "I don't need to debug because my code works",
        "I don't know how to use debuggers.": "I don't know how to use debuggers",
        "It's easier or faster to solve problems through print debugging or logs.": "It's easier or faster to solve problems through print debugging or logs",
        "It's easier or faster to let an AI model debug my code.": "It's easier or faster to let an AI model debug my code",
        "The types from external libraries I'm working with have poor debugger support.": "The types from external libraries I'm working with have poor debugger support",
        "The types from the standard library I'm working with have poor debugger support.": "The types from the standard library I'm working with have poor debugger support",
        "The language features I'm working with have poor debugger support.": "The language features I'm working with have poor debugger support",
    }
    # TODO: Figure out shorter labels that are easier to read without losing
    # significant information.
    debugger_difficulties = "When you DON'T use a debugger, why don't you?"
    db.df = db.df.rename(debugger_difficulties_diff, axis="columns")
    report.add_bar_chart(
        "when-you-dont-use-a-debugger-why-dont-you",
        db.q_simple_multi(debugger_difficulties),
        xaxis_tickangle=45,
    )
    debugger_difficulties_responses = db.open_answers(debugger_difficulties)
    with open(
        Path(__file__).parent / "open-response-debugger-difficulties.txt", "w"
    ) as f:
        for answer in debugger_difficulties_responses:
            f.write(f"{answer}\n---\n\n")
    # TODO: Similarly to the previous wordcloud related TODO, does it really
    # provide any value to know that one of the most prominent words in answers
    # to a question about "why you don't use debuggers" is "debugger"?
    report.add_wordcloud(
        "when-you-dont-use-a-debugger-why-dont-you-wordcloud",
        db.open_answers(debugger_difficulties),
    )

    step_through_issues_bool = "Do you experience any issues when trying to step through code with your debugger?"
    report.add_pie_chart(
        "do-you-experience-any-issues-when-trying-to-step-through-code-with-your-debugger",
        db.q_simple_single(step_through_issues_bool),
    )

    # TODO: Could these be relabeled without the leading "When" and trailing
    # "are involved" without confusing people?
    step_through_issues_when = "When do you experience issues with trying to step through code with your debugger?"
    report.add_bar_chart(
        "when-do-you-experience-issues-with-trying-to-step-through-code-with-your-debugger",
        db.q_simple_multi(step_through_issues_when),
        xaxis_tickangle=45,
    )
    step_through_issues_when_responses = db.open_answers(
        step_through_issues_when
    )
    with open(
        Path(__file__).parent / "open-response-step-through-issues-when.txt",
        "w",
    ) as f:
        for answer in step_through_issues_when_responses:
            f.write(f"{answer}\n---\n\n")
    # TODO: Similarly to the previous wordcloud related TODO, does it really
    # provide any value to know that one of the most prominent words in answers
    # to a question about "when you experience issues stepping through code with
    # your debugger" is "debugger"?
    report.add_wordcloud(
        "when-do-you-experience-issues-with-trying-to-step-through-code-with-your-debugger-wordcloud",
        db.open_answers(step_through_issues_when),
    )

    # TODO: When making a wordcloud, the report automatically titles it,
    # "Wordcloud of open answers for the previous chart:". In this case, that is
    # just not true. I think a wordcloud can be useful without a parent chart;
    # maybe add_wordcloud should be patched to allow overriding this?
    std_lib_pain = (
        "What standard library types are hard to work with when debugging?"
    )
    std_lib_pain_responses = db.open_answers_raw(std_lib_pain)
    with open(
        Path(__file__).parent / "open-response-std-lib-pain.txt", "w"
    ) as f:
        for answer in std_lib_pain_responses:
            f.write(f"{answer}\n---\n\n")
    report.add_wordcloud(
        "what-standard-library-types-are-hard-to-work-with-when-debugging-wordcloud",
        db.open_answers(std_lib_pain),
    )

    visualizer_attribute_known = "If you are a library author, are you aware of and using the debugger visualizer attribute?"
    report.add_pie_chart(
        "if-you-are-a-library-author-are-you-aware-of-and-using-the-debugger-visualizer-attribute",
        db.q_simple_single(visualizer_attribute_known),
    )

    # Because the answers to the question ended in periods, the report library
    # was unable to process these responses. The usual "rename" method did not
    # resolve it, so this requires patching the dataframe directly.
    visualizer_attribute_avoided_diff = {
        "I don't know how to write visualizer scripts.": "I don't know how to write visualizer scripts",
        "My debugger is not supported.": "My debugger is not supported",
        "My libraries' types do not need them.": "My libraries' types do not need them",
        "I don't have time to maintain visualizer attributes.": "I don't have time to maintain visualizer attributes",
    }
    db.df = db.df.rename(visualizer_attribute_avoided_diff, axis="columns")
    visualizer_attribute_avoided = (
        "Why don't you use the debugger visualizer attribute?"
    )
    report.add_bar_chart(
        "why-dont-you-use-the-debugger-visualizer-attribute",
        db.q_simple_multi(visualizer_attribute_avoided),
        xaxis_tickangle=45,
    )
    visualizer_attribute_avoided_responses = db.open_answers(
        visualizer_attribute_avoided
    )
    with open(
        Path(__file__).parent
        / "open-response-visualizer-attribute-avoided.txt",
        "w",
    ) as f:
        for answer in visualizer_attribute_avoided_responses:
            f.write(f"{answer}\n---\n\n")
    # TODO: Similarly to most of the previous wordcloud related TODOs, does it
    # really provide any value to know that some of the most prominent words in
    # answers to a question about "why you don't use the debugger visualizer
    # attribute" are "debugger", "visualiser", "script", and "use"?
    report.add_wordcloud(
        "why-dont-you-use-the-debugger-visualizer-attribute-wordcloud",
        db.open_answers(visualizer_attribute_avoided),
    )

    # TODO: Figure out shorter labels that are easier to read without losing
    # significant information.
    pain_points = "Which of these pain points have you experienced using a debugger with Rust?"
    report.add_bar_chart(
        "which-of-these-pain-points-have-you-experienced-using-a-debugger-with-rust",
        db.q_simple_multi(pain_points),
        xaxis_tickangle=45,
    )

    final_open_question = "Is there anything else you would like to tell us about debugging support in Rust?"
    final_open = db.open_answers_raw(final_open_question)
    with open(
        Path(__file__).parent / "open-response-final-anything-else.txt", "w"
    ) as f:
        for answer in final_open:
            f.write(f"{answer}\n---\n\n")
    # TODO: When making a wordcloud, the report automatically titles it,
    # "Wordcloud of open answers for the previous chart:". In this case, that is
    # just not true. I think a wordcloud can be useful without a parent chart;
    # maybe add_wordcloud should be patched to allow overriding this?
    report.add_wordcloud(
        "is-there-anything-else-you-would-like-to-tell-us-about-debugging-support-in-rust-wordcloud",
        db.open_answers(final_open_question),
    )

    return report


if __name__ == "__main__":
    random.seed(0x0D15EA5E)
    np.random.seed(0x0D15EA5E)

    report = analyze(including_secret_data=False)

    render_report_to_pdf(
        report,
        Path(__file__).parent / "debugging-survey-2026-report.pdf",
        "Rust Debugging survey 2026 report",
        include_labels=True,
    )
