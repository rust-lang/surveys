import itertools
import random
import sys
from pathlib import Path
from typing import List, Any, Callable

import numpy as np
import pandas as pd
import plotly.express as px
from collections import defaultdict
from plotly.graph_objs import Figure

CURRENT_DIR = Path(__file__).absolute().parent
ROOT_DIR = CURRENT_DIR.parent.parent.parent.parent
REPORT_SCRIPT_DIR = ROOT_DIR / "report"

sys.path.insert(0, str(REPORT_SCRIPT_DIR))

from surveyhero.parser import parse_surveyhero_report, parse_surveyhero_answers
from surveyhero.render import render_blog_post, render_report_to_pdf
from surveyhero.report import ChartReport
from surveyhero.survey import Question, SurveyFullAnswers, SurveyReport, rating_to_simple_question
from surveyhero.utils import print_question_index


def print_answers(a: Question, b: Question):
    assert a.is_simple()
    assert b.is_simple()

    a_answers = set(a.answer for a in a.kind.answers)
    b_answers = set(a.answer for a in b.kind.answers)
    answers = a_answers | b_answers
    for answer in sorted(answers):
        has_a = answer in a_answers
        has_b = answer in b_answers
        print(answer, has_a, has_b)


def print_answer_index(answers: SurveyFullAnswers, report: SurveyReport, path: Path):
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


def group_by_pct(df: pd.DataFrame, group_by_columns: List[str]) -> pd.DataFrame:
    grouped_count = df.groupby(group_by_columns).agg({
        "id": "count"
    }).rename(columns={"id": "pct"})

    reset_level = tuple(itertools.islice(range(len(group_by_columns)), len(group_by_columns) - 1))
    grouped_pct = grouped_count.groupby(level=reset_level).apply(lambda x: 100 * x / x.sum())
    return grouped_pct.reset_index(level=reset_level)["pct"].reset_index()


def render_stacked_bar_chart(
        df: pd.DataFrame,
        col: str,
        row: str,
        title: str,
        col_title: str,
        row_title: str,
        pct=True,
        height=600,
        grid=None,
        **kwargs
) -> Figure:
    """
    Renders a stacked bar chart from the individual groups created by `col` and `row`.

    If `pct` is `True`, then the values will be normalized to percentages within the individual
    groups.
    """
    assert col in df.columns
    assert col != col_title
    assert row in df.columns
    assert row != row_title

    if pct:
        title += " (%)"
    else:
        title += " (absolute counts)"

    df = df.rename(columns={
        row: row_title,
        col: col_title
    })
    if "category_orders" in kwargs and row in kwargs["category_orders"]:
        kwargs["category_orders"][row_title] = kwargs["category_orders"][row]
        del kwargs["category_orders"][row]
    if "category_orders" in kwargs and col in kwargs["category_orders"]:
        kwargs["category_orders"][col_title] = kwargs["category_orders"][col]
        del kwargs["category_orders"][col]

    row = row_title
    col = col_title

    group_by_columns = [col, row]
    if grid is not None:
        group_by_columns = [grid] + group_by_columns

    title = f"<b>{title}</b>"
    if pct:
        df = df[~df[col].isna()]
        assert len(df) > 0
        data = group_by_pct(df, group_by_columns)
        title += '<br /><span style="font-size: 0.8em;">The percentages are relative to each individual group on the X axis</span>'
    else:
        data = df.groupby(group_by_columns)["id"].count().reset_index().rename(
            columns=dict(id="count"))

    data = data.rename(columns=dict(pct="Percentage (%)"))
    fig = px.bar(data,
                 x=col,
                 y="Percentage (%)" if pct else "count",
                 color=row,
                 facet_col=grid,
                 facet_col_wrap=3,
                 title=title,
                 height=height,
                 **kwargs)
    fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))

    return fig


def compiler_performance_2025_report(df: pd.DataFrame) -> ChartReport:
    res = parse_surveyhero_report(
        Path(ROOT_DIR / "data/2025/compiler-performance/summary.csv"),
        year=2025)
    answers = parse_surveyhero_answers(
        Path(ROOT_DIR / "data/2025/compiler-performance/responses.csv"), year=2025)

    print_answer_index(answers, res, Path("answers.txt"))
    print_question_index(Path("questions.txt"), res)

    report = ChartReport()
    report.add_bar_chart("do-you-use-rust", res.q(0))
    report.add_bar_chart("reason-stop-using-rust", res.q(1))
    report.add_bar_chart("development-os", res.q(2), xaxis_tickangle=30)
    report.add_bar_chart("rust-at-company", res.q(3), xaxis_tickangle=30,
                         sort_by_pct=False)

    build_systems_diff = {
        "I use some other build system": ["I use some other build system",
                                          "If you use other build system(s), which ones do you use?"]
    }
    report.add_bar_chart("build-systems", res.q(4).combine_answers(build_systems_diff),
                         xaxis_tickangle=30)
    report.add_wordcloud("build-systems-wordcloud", answers.answers[21])

    report.add_bar_chart("how-do-you-build-rust-projects", res.q(5),
                         xaxis_tickangle=30)

    workflows_diff = {
        "Type checking (change code, type check using cargo check or IDE)": "cargo check",
        "Running tests (change code, run tests cargo test or IDE)": "cargo test",
        "Unoptimized rebuilds (change code, rebuild without optimizations)": "Unoptimized rebuilds",
        "Optimized rebuilds (change code, rebuild with optimizations)": "Optimized rebuilds",
        "Workspace rebuilds (change a crate which causes multiple other crates in your workspace to be rebuilt)": "Workspace rebuilds",
        "Clean unoptimized builds (build a crate graph from scratch)": "Clean unoptimized builds",
        "Clean optimized builds (build a crate graph from scratch)": "Clean optimized builds",
        "CI (Continuous Integration) builds": "CI builds",
    }
    report.add_matrix_chart("limiting-workflows", res.q(6).rename_answers(workflows_diff),
                            horizontal=True,
                            category_label="Severity",
                            height=800,
                            textposition="inside",
                            legend_params=dict(
                                orientation="h",
                                y=-0.05,
                            ))
    report.add_bar_chart("caching", res.q(7))
    report.add_wordcloud("caching-wordcloud", answers.answers[42])

    report.add_bar_chart(
        "project-size-lines",
        res.q(8),
        xaxis_tickangle=30,
        sort_by_pct=False
    )
    report.add_bar_chart(
        "project-size-dependencies",
        res.q(9),
        xaxis_tickangle=30,
        sort_by_pct=False
    )
    report.add_bar_chart(
        "rebuild-wait-time",
        res.q(10),
        xaxis_tickangle=30,
        sort_by_pct=False
    )

    rebuild_time_order = [
        "<1s",
        "1-5s",
        "5-10s",
        "10-30s",
        "30s-1m",
        "1-5m",
        ">5m"
    ]

    os_order = ["Linux", "macOS", "Windows", "Windows Subsystem for Linux", "Other"]
    report.add_custom_chart("rebuild-wait-time-os",
                            lambda **kwargs: render_stacked_bar_chart(
                                df,
                                col="os",
                                row="rebuild-time",
                                col_title="Operating system",
                                row_title="Rebuild time",
                                title="Average rebuild time based on OS",
                                category_orders={
                                    "os": os_order,
                                    "rebuild-time": rebuild_time_order
                                },
                                **kwargs
                            ),
                            height=800)

    core_count_order = [
        "1",
        "2-4",
        "5-8",
        "9-16",
        "17-32",
        "More than 32 cores"
    ]
    code_size_order = [
        "Less than 2 thousand lines",
        "2-10 thousand lines",
        "11-50 thousand lines",
        "51-100 thousand lines",
        "101-500 thousand lines",
        "More than 500 thousand lines of code"
    ]
    report.add_custom_chart("rebuild-wait-time-code-size",
                            lambda **kwargs: render_stacked_bar_chart(
                                df,
                                col="code-size",
                                row="rebuild-time",
                                col_title="Codebase size",
                                row_title="Rebuild time",
                                title="Average rebuild time based on project size",
                                category_orders={
                                    "code-size": code_size_order,
                                    "rebuild-time": rebuild_time_order
                                },
                                **kwargs
                            ), height=800)

    df["lines-of-code-est"] = df["code-size"].apply(lambda v: {
        "2-10 thousand lines": 5000,
        "11-50 thousand lines": 25000,
        "51-100 thousand lines": 75000,
        "101-500 thousand lines": 250000,
    }.get(v, np.nan))
    df["rebuild-time-est"] = df["rebuild-time"].apply(lambda v: {
        "Less than a second": 0.5,
        "Between 1 and 5 seconds": 2.5,
        "Between 5 and 10 seconds": 7.5,
        "Between 10 and 30 seconds": 20,
        "Between 30 seconds and 1 minute": 45,
        "Between 1 and 5 minutes": 150,
    }.get(v, np.nan))
    df["build-perf-est"] = df["lines-of-code-est"] / df["rebuild-time-est"]
    group = df.groupby("core-count")["build-perf-est"].mean().reset_index()
    # report.add_custom_chart("rebuild-wait-time-code-size-hw-cores",
    #                         lambda **kwargs: px.bar(group,
    #                                                 x="core-count",
    #                                                 y="build-perf-est",
    #                                                 category_orders={
    #                                                     "core-count": core_count_order
    #                                                 }))
    report.add_custom_chart("rebuild-wait-time-dep-count",
                            lambda **kwargs: render_stacked_bar_chart(
                                df,
                                col="dep-count",
                                row="rebuild-time",
                                col_title="",
                                row_title="Rebuild time",
                                grid="code-size",
                                title="Average rebuild time based on project size and dependency count",
                                facet_col_spacing=0.05,
                                category_orders={
                                    "dep-count": [
                                        "No dependencies",
                                        "1-10 dependencies",
                                        "11-50 dependencies",
                                        "51-100 dependencies",
                                        "101-200 dependencies",
                                        "201-300 dependencies",
                                        "301-500 dependencies",
                                        "More than 500 dependencies"
                                    ],
                                    "rebuild-time": rebuild_time_order,
                                    "code-size": code_size_order
                                },
                                **kwargs
                            ), height=800)

    report.add_matrix_chart(
        "problems",
        res.q(11),
        horizontal=True,
        category_label="Severity",
        height=800,
        textposition="inside",
        legend_params=dict(
            orientation="h",
            y=-0.05,
        )
    )
    report.add_bar_chart(
        "compile-error-examination",
        res.q(12),
    )
    report.add_wordcloud("compile-error-examination-wordcloud", answers.answers[57])
    report.add_matrix_chart(
        "cargo-commands",
        res.q(13),
        horizontal=True,
        category_label="Severity",
        height=800,
        textposition="inside",
        legend_params=dict(
            orientation="h",
            y=-0.05,
        )
    )
    report.add_matrix_chart(
        "profiling-tools",
        res.q(14),
        horizontal=True,
        category_label="Severity",
        height=800,
        textposition="inside",
        legend_params=dict(
            orientation="h",
            y=-0.05,
        )
    )
    comptime_mechanisms_diff = {
        "Disable (or reduce) debuginfo (e.g. set debug = 0 in Cargo.toml)": "Disable or reduce debuginfo",
        "Parallel compiler frontend (pass -Zthreads=<N> to the compiler)": "Parallel compiler frontend",
        'Cranelift codegen backend (e.g. set codegen-backend = "cranelift" in Cargo.toml)': "Cranelift backend",
        "Alternative linker (e.g. lld/mold/wild)": "Alternative linker",
        "Caching compiler wrapper (e.g. sccache)": "Caching compiler wrapper",
        "Share target directory amongst multiple projects (e.g. with CARGO_TARGET_DIR)": "Share target directory",
        "Split crates into smaller crates": "Split crates",
        "Reduce the amount of dependencies": "Reduce dependency count",
        "Create a Cargo feature to make certain dependencies (or their features) opt-in": "Create opt-in Cargo features",
        "Reduce usage of generic code (e.g. by converting it to dyn Trait instead)": "Reduce usage of generic code",
    }
    report.add_matrix_chart(
        "compile-time-improvement-mechanisms",
        res.q(15).rename_answers(comptime_mechanisms_diff),
        horizontal=True,
        category_label="Severity",
        height=800,
        textposition="inside",
        legend_params=dict(
            orientation="h",
            y=-0.05,
        )
    )
    report.add_bar_chart(
        "alternative-linker",
        res.q(16),
    )
    report.add_custom_chart("alternative-linker-os", lambda **kwargs: render_stacked_bar_chart(
        df,
        col="os",
        row="linker",
        col_title="",
        row_title="Rebuild time",
        title="Alternative linker used based on OS",
        pct=False,
        category_orders={
            "os": os_order
        },
        **kwargs
    ))

    report.add_wordcloud("alternative-linker-wordcloud", answers.answers[87])
    report.add_bar_chart(
        "nightly-compiler",
        res.q(17),
    )
    report.add_wordcloud(
        "nightly-compiler-wordcloud",
        answers.answers[89],
    )
    report.add_bar_chart(
        "debugger",
        res.q(18),
        xaxis_tickangle=30,
        sort_by_pct=False
    )
    report.add_bar_chart(
        "profiler",
        res.q(19),
        xaxis_tickangle=30,
        sort_by_pct=False
    )
    report.add_bar_chart(
        "required-debuginfo",
        res.q(20),
    )

    frequency_order = ["Almost always", "Often",
                       "Sometimes", "Never or very rarely"]
    debuginfo_order = ["Yes", "Only for my code", "No"]
    report.add_custom_chart(
        "required-debuginfo-debugger",
        lambda **kwargs: render_stacked_bar_chart(
            df,
            "how-often-do-you-use-debugger",
            "require-debuginfo",
            col_title="Do you use a debugger?",
            row_title="Do you require debuginfo?",
            title="Debuginfo requirement based on the usage of a debugger",
            category_orders={
                "how-often-do-you-use-debugger": frequency_order,
                "require-debuginfo": debuginfo_order
            },
            **kwargs
        )
    )
    report.add_custom_chart(
        "required-debuginfo-profiler",
        lambda **kwargs: render_stacked_bar_chart(
            df,
            "how-often-do-you-use-profiler",
            "require-debuginfo",
            col_title="Do you use a profiler?",
            row_title="Do you require debuginfo?",
            title="Debuginfo requirement based on the usage of a profiler",
            category_orders={
                "how-often-do-you-use-profiler": frequency_order,
                "require-debuginfo": debuginfo_order
            },
            **kwargs
        )
    )

    report.add_bar_chart(
        "hw-cores",
        res.q(21),
        sort_by_pct=False
    )
    report.add_custom_chart(
        "rebuild-wait-time-hw-cores",
        lambda **kwargs: render_stacked_bar_chart(
            df,
            col="core-count",
            row="rebuild-time",
            row_title="Rebuild time",
            col_title="",
            title="Rebuild time based on core count",
            category_orders={
                "rebuild-time": rebuild_time_order,
                "core-count": core_count_order
            },
            **kwargs
        )
    )

    report.add_bar_chart(
        "hw-ram",
        res.q(22),
        sort_by_pct=False
    )
    report.add_bar_chart(
        "satisfaction",
        rating_to_simple_question(res.q(23)).with_title(
            lambda title: format(f"{title}\n(0 = worst, 10 = best)")),
        sort_by_pct=False,
        height=400
    )
    report.add_custom_chart(
        "satisfaction-code-size",
        lambda **kwargs: render_stacked_bar_chart(
            df,
            col="code-size",
            row="satisfaction",
            row_title="Satisfaction (10 = best)",
            col_title="",
            title="Overall satisfaction based on project size",
            category_orders={
                "code-size": code_size_order
            },
            **kwargs
        )
    )
    report.add_custom_chart(
        "satisfaction-os",
        lambda **kwargs: render_stacked_bar_chart(
            df,
            col="os",
            row="satisfaction",
            row_title="Satisfaction (10 = best)",
            col_title="",
            title="Overall satisfaction based on operating system",
            category_orders={
                "os": os_order,
                "code-size": code_size_order
            },
            **kwargs
        )
    )

    return report


def create_df(path: Path) -> pd.DataFrame:
    data = pd.read_csv(path)

    def remap(df, col, mapping):
        return df[col].map(lambda v: mapping.get(v, v))

    def find_single_value_or_nan(row):
        nonnan_value = row.last_valid_index()
        if nonnan_value is None:
            return np.nan
        if nonnan_value.startswith("Other"):
            return "Other"
        return nonnan_value

    def find_any_or_nan(row, needles: List[str]):
        nonnan_value = row.last_valid_index()
        if nonnan_value is None:
            return np.nan
        return any(v in needles for v in row if v is not np.nan)

    def reconstruct_col(name: str, answer_count: int, map_value: Callable[[Any], Any]):
        """
        Reconstructs answers from a wide format to a long format.
        For example, if `name` is `foo` and there are three answers:

        foo a   b   c
            x   nan nan
            nan x   nan
            nan nan nan
            nan nan x

        Then it would return ["a", "b", nan, "c"].
        """
        col_index = data.columns.get_loc(name)
        col_data = data.iloc[:, col_index + 1:col_index + answer_count + 1]

        return col_data.apply(map_value, axis=1)

    frequency_mapping = {
        "Almost always (e.g. after almost every build)": "Almost always",
        "Sometimes (e.g. once per week or less)": "Sometimes",
        "Often (e.g. multiple times per day)": "Often"
    }
    df = pd.DataFrame({
        "id": data["ID"],
        "core-count": data["How many cores does your computer have?"],
        "rebuild-time": data[
            'How long do you need to wait for the compiler to rebuild your code after making a change?'].apply(
            lambda v: {
                "Less than a second": "<1s",
                "Between 1 and 5 seconds": "1-5s",
                "Between 5 and 10 seconds": "5-10s",
                "Between 10 and 30 seconds": "10-30s",
                "Between 30 seconds and 1 minute": "30s-1m",
                "Between 1 and 5 minutes": "1-5m",
                "More than 5 minutes": ">5m",
            }.get(v, v)),
        "how-often-do-you-use-debugger": remap(
            data,
            "How often do you use a debugger to debug your Rust code?",
            frequency_mapping),
        "how-often-do-you-use-profiler": remap(
            data,
            "How often do you use a profiler to profile your Rust code?",
            frequency_mapping),
        "require-debuginfo": remap(
            data,
            "Do you require unoptimized builds to have debuginfo by default?",
            {
                "Yes, I want full debuginfo by default": "Yes",
                "Yes, but I do not need full debuginfo for my dependencies, just for my code": "Only for my code",
                "No, I would prefer slightly faster compilation with less debuginfo by default": "No"
            }
        ),
        "os": reconstruct_col("Which operating systems do you use regularly for Rust development?",
                              5, find_single_value_or_nan),
        "code-size": data[
            "How large is the Rust project that you work on in terms of lines of Rust code?"],
        "dep-count": data[
            "How large is the Rust project that you work on in terms of (Cargo) dependencies?"],
        "linker": reconstruct_col("If you use an alternative linker, which one do you use?", 5,
                                  find_single_value_or_nan),
        "satisfaction": data["Overall, how satisfied are you with Rust compilation performance?"],
        "used-workarounds": reconstruct_col(
            "Have you used any of the following mechanisms to improve compilation performance?", 13,
            lambda row: find_any_or_nan(row,
                                        ["It helps me to improve compile times",
                                         "I tried it, but it didn't help"])),
        "uses-ci": ~data["On CI (Continuous Integration) infrastructure"].isna(),
        "uses-ci-caching": ~reconstruct_col("Do you use any caching to speed up CI builds?", 4,
                                            lambda row: find_single_value_or_nan(row)).isna(),
        "ci-is-blocker": data["CI (Continuous Integration) builds"].isin(
            ("Big problem for me",))  # "Could be improved, but does not limit me"))
    })
    print(f"Used workaround: {df['used-workarounds'].value_counts()}")

    uses_ci = df["uses-ci"].sum()
    uses_ci_is_blocker = (df["uses-ci"] & df["ci-is-blocker"]).sum()
    uses_ci_is_blocker_no_caching = (
            df["uses-ci"] & df["ci-is-blocker"] & ~df["uses-ci-caching"]).sum()
    print(f"Uses CI: {uses_ci}")
    print(
        f"Uses CI, CI is blocker: {uses_ci_is_blocker} ({(uses_ci_is_blocker / uses_ci) * 100:.2f}%)")
    print(f"Uses CI, CI is blocker, no caching: {uses_ci_is_blocker_no_caching}")
    print(
        f"No cache blocking ratio: {(uses_ci_is_blocker_no_caching / uses_ci_is_blocker) * 100:.2f}%")

    return df


if __name__ == "__main__":
    random.seed(42)
    np.random.seed(42)

    df = create_df(ROOT_DIR / "data/2025/compiler-performance/responses.csv")

    report = compiler_performance_2025_report(df)

    render_report_to_pdf(
        report,
        Path(__file__).parent / "compiler-performance-2025-report.pdf",
        "Compiler performance survey\n2025 report",
        include_labels=False
    )

    blog_dir = Path(
        "/projects/personal/rust/blog.rust-lang.org/content/rust-compiler-performance-survey-2025-results")
    template_path = Path(CURRENT_DIR / "blog.md")
    render_blog_post(
        template=template_path,
        blog_dir=blog_dir,
        report=report
    )
