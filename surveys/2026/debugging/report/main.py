import random
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np
import pandas as pd
from plotly.graph_objs import Figure

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

OPEN_RESPONSES_DIR = ROOT_DIR / "open_responses/2026/debugging"
"""
This should resolve to the path of the directory used to store open response
answers extracted from the raw data. Typically, this is the `open_responses`
directory at the repository root or some path within.
"""

sys.path.insert(0, str(REPORT_SCRIPT_DIR))

# TODO: At runtime, only the `surveyhero.*` imports work. In my editor (VSCodium
# + `ty` extension), only the `report.surveyhero.*` imports work. The below hack
# is ugly, but it gets me the best of both worlds. Ideally, I think we should
# find a way to set things up in the project such that imports "just work", at
# runtime and in editors, without dynamically adding the import path.
try:
    from report.surveyhero.analysis import at_least_one_col
    from report.surveyhero.chart import (
        make_chart,
    )
    from report.surveyhero.parser import (
        parse_surveyhero_answers,
        parse_surveyhero_summary,
    )
    from report.surveyhero.render import (
        render_report_to_pdf,
    )
    from report.surveyhero.report import ChartReport
    from report.surveyhero.survey import (
        Answer,
        MatrixQuestion,
        SimpleQuestion,
        normalize_open_answers,
    )
    from report.surveyhero.utils import shorten_annotations
except ModuleNotFoundError:
    from surveyhero.analysis import (  # ty:ignore[unresolved-import]
        at_least_one_col,
    )
    from surveyhero.chart import (  # ty:ignore[unresolved-import]
        make_chart,
    )
    from surveyhero.parser import (  # ty:ignore[unresolved-import]
        parse_surveyhero_answers,
        parse_surveyhero_summary,
    )
    from surveyhero.render import (  # ty:ignore[unresolved-import]
        render_report_to_pdf,
    )
    from surveyhero.report import ChartReport  # ty:ignore[unresolved-import]
    from surveyhero.survey import (  # ty:ignore[unresolved-import]
        Answer,
        MatrixQuestion,
        SimpleQuestion,
        normalize_open_answers,
    )
    from surveyhero.utils import (  # ty:ignore[unresolved-import]
        shorten_annotations,
    )


def analyze() -> ChartReport:
    summary = parse_surveyhero_summary(
        Path(ROOT_DIR / "data/2026/debugging/summary.csv"), year=2026
    )
    db = parse_surveyhero_answers(
        Path(ROOT_DIR / "data/2026/debugging/responses.csv"),
        year=2026,
        summary=summary,
    )

    OPEN_RESPONSES_DIR.mkdir(parents=True, exist_ok=True)

    report = ChartReport()

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

    debugger_user = "Do you use debuggers in Rust?"
    do_you_use_debugger_q = db.q_simple_single(debugger_user)
    report.add_pie_chart(
        "do-you-use-debuggers-in-rust",
        do_you_use_debugger_q,
    )

    do_you_use_debugger_df = {
        "use": db.df[debugger_user],
        "expertise": db.df[expertise],
    }
    do_you_use_debugger_df = pd.DataFrame(do_you_use_debugger_df)
    do_you_use_debugger_df = do_you_use_debugger_df.dropna()

    def draw_debugger_usage_per_rust_expertise() -> Figure:
        fig = make_chart(
            do_you_use_debugger_q.with_title(
                lambda t: f"{t} (based on expertise)"
            ),
            do_you_use_debugger_df,
            x="use",
            kind="pie",
            facet_col="expertise",
            category_orders={
                "expertise": ["Beginner", "Intermediate", "Advanced"],
                "use": [
                    "No, I have never used debuggers in Rust",
                    "No, I don't currently use debuggers in Rust, but I have in the past",
                    "Yes",
                ],
            },
            height=450,
        )
        fig.update_layout(legend=dict(orientation="h"))
        return shorten_annotations(fig)

    report.add_custom_chart(
        "do-you-use-debuggers-in-rust-per-expertise",
        draw_debugger_usage_per_rust_expertise,
    )

    debugger_user_past = "Did you use debuggers in Rust?"
    report.add_pie_chart(
        "did-you-use-debuggers-in-rust",
        db.q_simple_single(debugger_user_past),
    )

    quit_because_of_debuggers = "Were issues with debugging support the primary reason why you stopped using Rust?"
    report.add_pie_chart(
        "were-issues-with-debugging-support-the-primary-reason-why-you-stopped-using-rust",
        db.q_simple_single(quit_because_of_debuggers).with_title(
            lambda t: t.replace("reason why", "reason\nwhy")
        ),
    )

    other_languages_diff = {
        "No, I don't currently use debuggers in other programming languages, but I have in the past": "Not anymore",
        "No, I have never used debuggers in other programming languages": "No, never",
    }
    other_languages = "Do you use debuggers in other programming languages?"
    report.add_pie_chart(
        "do-you-use-debuggers-in-other-programming-languages",
        db.q_simple_single(other_languages).rename_answers(
            other_languages_diff  # ty:ignore[invalid-argument-type] https://docs.astral.sh/ty/reference/typing-faq/#invariant-generics
        ),
    )

    os_and_debugger = "What tools and workflows do you use to debug Rust programs on which operating systems?"
    os_and_debugger_q = summary.q_by_text(os_and_debugger)

    # Combined answers throughout all OSes
    assert isinstance(os_and_debugger_q.kind, MatrixQuestion)
    answer_count = len(
        next(iter(os_and_debugger_q.kind.answer_groups.values()))
    )
    keys = sorted(os_and_debugger_q.kind.answer_groups.keys())
    answers_at_least_one_col = defaultdict()
    debugger_used_on_any_os = defaultdict()
    answers_per_os = defaultdict(list)
    for key in keys:
        data = db.get_answer_columns(
            db.get_column(key), answer_count=answer_count
        )
        debugger_used_on_any_os[key] = data.notna().any(axis=1)

        # Find entries where at least one column in the row is not nan
        at_least_one_col_data = data.notna().any(axis=1).sum()  # ty:ignore[unresolved-attribute] Assumption: .any returns a Series, not a bool
        for os in data.columns:
            os_data = data[os]
            answers_per_os["os"].append(os)
            answers_per_os["debugger"].append(key)
            answers_per_os["count"].append(os_data.notna().sum())
        answers_at_least_one_col[key] = at_least_one_col_data

    debuger_q_agg = os_and_debugger_q.with_title(
        lambda t: "What tools and workflows do you use to debug Rust programs?"
    ).with_kind(
        SimpleQuestion(
            answers=[
                Answer(answer=k, count=v)
                for (k, v) in answers_at_least_one_col.items()
            ]
        )
    )
    report.add_bar_chart(
        "what-tools-and-workflows-do-you-use-to-debug-rust-programs",
        debuger_q_agg,
        xaxis_tickangle=45,
    )
    answers_per_os = pd.DataFrame(answers_per_os)
    answers_per_os["os"] = answers_per_os["os"].replace(
        "Windows Subsystem for Linux", "WSL"
    )

    def debuggers_per_os(**kwargs) -> Figure:
        fig = make_chart(
            os_and_debugger_q,
            answers_per_os,
            kind="pie",
            x="debugger",
            y="count",
            facet_col="os",
            facet_col_wrap=3,
            facet_col_spacing=0.05,
            facet_row_spacing=0.15,
            height=900,
        )
        fig.update_layout(legend=dict(orientation="h", y=-0.15))
        return shorten_annotations(fig)

    report.add_custom_chart(
        "what-tools-and-workflows-do-you-use-to-debug-rust-programs-per-os-1",
        debuggers_per_os,
    )

    def os_per_debugger(**kwargs) -> Figure:
        answers = answers_per_os.replace(
            """I don't know, I just hit "Debug" in my IDE""", "I don't know"
        ).replace("Print debugging (e.g. println!)", "Print debugging")
        fig = make_chart(
            os_and_debugger_q,
            answers,
            kind="pie",
            x="os",
            y="count",
            facet_col="debugger",
            facet_col_wrap=4,
            facet_col_spacing=0.1,
            facet_row_spacing=0.05,
            height=800,
        )
        fig.update_layout(
            legend=dict(
                orientation="h",
            )
        )
        fig = shorten_annotations(fig)
        for ann in fig["layout"]["annotations"]:
            if "WinDbg" in ann.text:
                ann["x"] = ann["x"] + 0.05
        return fig

    report.add_custom_chart(
        "what-tools-and-workflows-do-you-use-to-debug-rust-programs-per-os-2",
        os_per_debugger,
    )

    other_debuggers = "What other debuggers or workflows do you use?"
    other_debuggers_responses = db.open_answers_raw(other_debuggers)
    with open(OPEN_RESPONSES_DIR / "other-debuggers.txt", "w") as f:
        for answer in other_debuggers_responses:
            f.write(f"{answer}\n---\n\n")
    report.add_wordcloud(
        "what-other-debuggers-or-workflows-do-you-use-wordcloud",
        db.open_answers(other_debuggers),
    )

    debugger_use_cases = "What are you using debuggers for?"
    debugger_use_cases_q = db.q_simple_multi(debugger_use_cases).rename_answers(
        {
            "Getting stack traces from hung/crashed processes": "Stack traces",
        }
    )
    report.add_bar_chart(
        "what-are-you-using-debuggers-for",
        debugger_use_cases_q,
        xaxis_tickangle=45,
    )

    assert not isinstance(debugger_use_cases_q.kind, MatrixQuestion)
    debugger_use_cases_df = db.get_answer_columns(
        db.get_column(debugger_use_cases),
        len(debugger_use_cases_q.kind.answers),
    )
    debugger_use_cases_df["expertise"] = db.df[expertise]

    def draw_debugger_use_cases_per_expertise() -> Figure:
        # Gather use-case long format by expertise
        df = (
            pd.melt(
                debugger_use_cases_df,
                id_vars=["expertise"],
                value_vars=debugger_use_cases_df.columns[:-1],
                var_name="use-case",
                value_name="value",
            )
            .dropna(subset=["value"])
            .drop(columns=["value"])
        )
        fig = make_chart(
            debugger_use_cases_q.with_title(
                lambda t: f"{t} (based on expertise)"
            ),
            df,
            x="use-case",
            kind="pie",
            facet_col="expertise",
            category_orders={
                "expertise": ["Beginner", "Intermediate", "Advanced"],
            },
            height=600,
        )
        fig.update_layout(legend=dict(orientation="h"))
        return shorten_annotations(fig)

    report.add_custom_chart(
        "what-are-you-using-debuggers-for-per-expertise",
        draw_debugger_use_cases_per_expertise,
    )

    use_case_answer_cols = db.get_answer_columns(
        db.get_column(debugger_use_cases), None
    )
    use_case_keys = use_case_answer_cols.keys()
    for debugger in debugger_used_on_any_os.keys():
        use_case_answer_cols[debugger] = debugger_used_on_any_os[debugger]
    use_case_answer_cols = use_case_answer_cols.replace(False, np.nan)
    use_case_answer_cols = use_case_answer_cols.replace(True, "x")
    use_case_by_tool_intermediate = (
        pd.melt(
            use_case_answer_cols,
            id_vars=[debugger for debugger in debugger_used_on_any_os.keys()],
            value_vars=use_case_keys,
            var_name="use-case",
            value_name="value",
        )
        .dropna(subset=["value"])
        .drop(columns=["value"])
    )
    use_case_by_tool = (
        pd.melt(
            use_case_by_tool_intermediate,
            id_vars=["use-case"],
            value_vars=[x for x in debugger_used_on_any_os.keys()],
            var_name="debugger",
            value_name="value",
        )
        .dropna(subset=["value"])
        .drop(columns=["value"])
    )

    def draw_debugger_use_cases_per_tool() -> Figure:
        df = use_case_by_tool.replace(
            """I don't know, I just hit "Debug" in my IDE""", "I don't know"
        ).replace("Print debugging (e.g. println!)", "Print debugging")
        fig = make_chart(
            debugger_use_cases_q.with_title(
                lambda t: f"{t} (based on debugger)"
            ),
            df,
            x="use-case",
            kind="pie",
            facet_col="debugger",
            facet_col_wrap=4,
            facet_col_spacing=0.1,
            facet_row_spacing=0.05,
            height=800,
        )
        fig.update_layout(legend=dict(orientation="h"))
        return shorten_annotations(fig)

    report.add_custom_chart(
        "what-are-you-using-debuggers-for-per-tool",
        draw_debugger_use_cases_per_tool,
    )

    def draw_debugger_use_cases_per_tool_other_way() -> Figure:
        df = (
            use_case_by_tool.replace(
                """I don't know, I just hit "Debug" in my IDE""", "I don't know"
            )
            .replace("Print debugging (e.g. println!)", "Print debugging")
            .replace(
                "Getting stack traces from hung/crashed processes",
                "Stack traces",
            )
        )
        fig = make_chart(
            debugger_use_cases_q.with_title(
                lambda t: f"{t} (based on debugger)"
            ),
            df,
            x="debugger",
            kind="pie",
            facet_col="use-case",
            facet_col_wrap=3,
            facet_col_spacing=0.1,
            facet_row_spacing=0.15,
            height=900,
        )
        fig.update_layout(legend=dict(orientation="h"))
        return shorten_annotations(fig)

    report.add_custom_chart(
        "what-are-you-using-debuggers-for-per-tool-1",
        draw_debugger_use_cases_per_tool_other_way,
    )

    debugger_used_for_responses = db.open_answers(debugger_use_cases)
    with open(OPEN_RESPONSES_DIR / "debugger-used-for.txt", "w") as f:
        for answer in debugger_used_for_responses:
            f.write(f"{answer}\n---\n\n")
    report.add_wordcloud(
        "what-are-you-using-debuggers-for-wordcloud",
        db.open_answers(debugger_use_cases),
    )

    multilingual = "Do you debug programs that combine Rust with any of the following languages?"
    multilingual_open = normalize_open_answers(db.open_answers(multilingual))
    multilingual_q = db.q_simple_multi(multilingual)
    multilingual_counts = at_least_one_col(
        db.get_df_for_question(multilingual_q)
    ).value_counts()

    multilingual_q2 = multilingual_q.shallow_copy()
    multilingual_q2.total_responses = multilingual_counts.sum()
    multilingual_q2 = multilingual_q2.with_kind(
        SimpleQuestion(
            answers=[
                Answer("yes", int(multilingual_counts["Yes"])),
                Answer("no", int(multilingual_counts["No"])),
            ]
        )
    ).with_title(
        lambda _t: (
            "Do you debug programs that combine Rust with other languages?"
        )
    )
    report.add_bar_chart(
        "do-you-debug-programs-that-combine-rust-with-other-languages",
        multilingual_q2,
        xaxis_tickangle=45,
    )

    report.add_bar_chart(
        "do-you-debug-programs-that-combine-rust-with-any-of-the-following-languages-",
        multilingual_q.add_open(
            multilingual_open, "assembly", "Assembly"
        ).with_title(lambda t: "If you do, with which languages?"),
        xaxis_tickangle=45,
    )
    multilingual_responses = multilingual_open
    with open(OPEN_RESPONSES_DIR / "multilingual.txt", "w") as f:
        for answer in multilingual_responses:
            f.write(f"{answer}\n---\n\n")
    report.add_wordcloud(
        "do-you-debug-programs-that-combine-rust-with-any-of-the-following-languages-wordcloud",
        multilingual_open,
    )

    debugger_difficulties = "When you DON'T use a debugger, why don't you?"
    report.add_bar_chart(
        "when-you-dont-use-a-debugger-why-dont-you",
        db.q_simple_multi(debugger_difficulties),
        xaxis_tickangle=45,
    )
    debugger_difficulties_responses = db.open_answers(debugger_difficulties)
    with open(OPEN_RESPONSES_DIR / "debugger-difficulties.txt", "w") as f:
        for answer in debugger_difficulties_responses:
            f.write(f"{answer}\n---\n\n")
    report.add_wordcloud(
        "when-you-dont-use-a-debugger-why-dont-you-wordcloud",
        db.open_answers(debugger_difficulties),
    )

    step_through_issues_bool = "Do you experience any issues when trying to step through code with your debugger?"
    step_through_issues_bool_q = db.q_simple_single(step_through_issues_bool)
    report.add_pie_chart(
        "do-you-experience-any-issues-when-trying-to-step-through-code-with-your-debugger",
        step_through_issues_bool_q,
    )

    step_through_issues_when = "When do you experience issues with trying to step through code with your debugger?"
    step_through_issues_q = db.q_simple_multi(step_through_issues_when)
    step_through_issues_q.total_responses = (
        step_through_issues_bool_q.total_responses
    )
    report.add_bar_chart(
        "when-do-you-experience-issues-with-trying-to-step-through-code-with-your-debugger",
        step_through_issues_q,
        xaxis_tickangle=45,
    )

    step_through_issues_when_responses = db.open_answers(
        step_through_issues_when
    )
    with open(
        OPEN_RESPONSES_DIR / "step-through-issues-when.txt",
        "w",
    ) as f:
        for answer in step_through_issues_when_responses:
            f.write(f"{answer}\n---\n\n")
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
    with open(OPEN_RESPONSES_DIR / "std-lib-pain.txt", "w") as f:
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
        OPEN_RESPONSES_DIR / "visualizer-attribute-avoided.txt",
        "w",
    ) as f:
        for answer in visualizer_attribute_avoided_responses:
            f.write(f"{answer}\n---\n\n")
    report.add_wordcloud(
        "why-dont-you-use-the-debugger-visualizer-attribute-wordcloud",
        db.open_answers(visualizer_attribute_avoided),
    )

    pain_points_diff = {
        "Suboptimal representations of values (e.g. Vec<T> is shown as a pointer, length and capacity rather than the elements)": "Bad values repr. (e.g. Vec<T> is shown as a pointer)",
        "Expression parser doesn't support expressions that you want to write": "Incomplete support for the Expression parser",
        "Incorrect information displayed (i.e. line numbers, variable values)": "Incorrect info shown (i.e. line nums, var values)",
        "Too much detail/irrelevant information (i.e. assembly views)": "Irrelevant details (i.e. assembly views)",
    }
    pain_points = "Which of these pain points have you experienced using a debugger with Rust?"
    report.add_bar_chart(
        "which-of-these-pain-points-have-you-experienced-using-a-debugger-with-rust",
        db.q_simple_multi(pain_points).rename_answers(pain_points_diff),  # ty:ignore[invalid-argument-type] https://docs.astral.sh/ty/reference/typing-faq/#invariant-generics
        xaxis_tickangle=45,
    )

    final_open_question = "Is there anything else you would like to tell us about debugging support in Rust?"
    final_open = db.open_answers_raw(final_open_question)
    with open(OPEN_RESPONSES_DIR / "final-anything-else.txt", "w") as f:
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

    report = analyze()

    render_report_to_pdf(
        report,
        Path(__file__).parent / "debugging-survey-2026-report.pdf",
        "Rust Debugging survey 2026 report",
        include_labels=True,
    )
