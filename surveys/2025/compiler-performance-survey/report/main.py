import random
import sys
from collections import defaultdict
from pathlib import Path
from typing import List

import numpy as np

from surveyhero.utils import print_question_index

ROOT_DIR = Path(__file__).absolute().parent.parent.parent.parent.parent
REPORT_SCRIPT_DIR = ROOT_DIR / "report"

sys.path.insert(0, str(REPORT_SCRIPT_DIR))

from surveyhero.parser import parse_surveyhero_report, parse_surveyhero_answers
from surveyhero.render import render_report_to_pdf
from surveyhero.report import ChartReport
from surveyhero.survey import Question, SurveyFullAnswers, SurveyReport, SimpleQuestion, Answer, \
    rating_to_simple_question


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


def compiler_performance_2025_report() -> ChartReport:
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
    report.add_wordcloud("alternative-linker-wordcloud", answers.answers[87])
    report.add_bar_chart(
        "nightly-compiler",
        res.q(17),
    )
    report.add_wordcloud(
        "nightly-compiler-wordcloud",
        answers.answers[89],
    )
    report.add_wordcloud(
        "other-mechanisms-wordcloud",
        answers.answers[90],
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
    report.add_bar_chart(
        "hw-cores",
        res.q(21),
        sort_by_pct=False
    )
    report.add_bar_chart(
        "hw-ram",
        res.q(22),
        sort_by_pct=False
    )
    report.add_bar_chart(
        "satisfaction",
        rating_to_simple_question(res.q(23)),
        sort_by_pct=False,
        height=400
    )
    return report


if __name__ == "__main__":
    random.seed(42)
    np.random.seed(42)

    report = compiler_performance_2025_report()

    render_report_to_pdf(
        report,
        Path(__file__).parent / "compiler-performance-2025-report.pdf",
        "Compiler performance survey\n2025 report",
        include_labels=True
    )
