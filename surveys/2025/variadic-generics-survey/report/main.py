import random
import sys
from xml.parsers import expat

from collections import defaultdict
from pathlib import Path

import numpy as np
import pandas as pd
from plotly.graph_objs import Figure

CURRENT_DIR = Path(__file__).absolute().parent
"""
This should resolve to the path of the directory containing this script.
"""

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
    render_blog_post,
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
    shorten_annotations, print_question_index,
)


def analyze() -> ChartReport:
    summary = parse_surveyhero_summary(
        Path(ROOT_DIR / "data/2025/variadics/summary.csv"), year=2025
    )
    db = parse_surveyhero_answers(
        Path(ROOT_DIR / "data/2025/variadics/responses.csv"),
        year=2025,
        summary=summary,
    )

    OPEN_RESPONSES_DIR.mkdir(parents=True, exist_ok=True)

    report = ChartReport()

    experience_order = [
        "I have never used Rust",
        "Less than two years",
        "Two to four years",
        "Four to six years",
        "More than six years"
    ]
    rust_usage = "How long have you been using Rust?"
    report.add_pie_chart(
        "how-long-have-you-been-using-rust",
        db.q_simple_single(rust_usage),
        legend_order=experience_order,
    )

    heard_about_variadics = "Have you heard about variadic generics before?"
    report.add_pie_chart(
        "have-you-heard-about-variadics",
        db.q_simple_single(heard_about_variadics),
    )

    heard_from = "Where have you heard about variadic generics?"
    open_answer = "Through other means (please describe)"
    answers_diff = {
        open_answer: "Through other means"
    }
    heard_from_open = db.open_answers(heard_from, open_answer=open_answer)
    question = db.q_simple_multi(heard_from)
    question = question.add_open(heard_from_open, id="bevy", label="Bevy", replace=open_answer)
    report.add_bar_chart(
        "where-have-you-heard-about-variadics",
        question.rename_answers(answers_diff),
        xaxis_tickangle=45,
    )
    report.add_wordcloud(
        "where-have-you-heard-about-variadics-wordcloud",
        heard_from_open
    )

    easier = "Are there cases where variadic generics would have made your project easier?"
    easier_q = db.q_simple_single(easier)
    report.add_pie_chart(
        "variadics-would-make-your-project-easier",
        easier_q,
    )

    def usefulness_per_experience(**kwargs) -> Figure:
        df = db.df[[easier, rust_usage]].dropna()
        df = df.rename(columns={
            rust_usage: "Experience",
            easier: "Usefulness"
        })

        fig = make_chart(
            easier_q.with_title(lambda q: f"{q} (per Rust experience)"),
            df,
            kind="pie",
            x="Usefulness",
            facet_col="Experience",
            facet_col_wrap=3,
            height=800,
            category_orders={
                "Experience": experience_order,
                "Usefulness": ["Yes", "No"]
            }
        )
        fig.update_layout(
            legend={
                "orientation": "h",
            }
        )
        return shorten_annotations(fig)

    report.add_custom_chart(
        "variadics-would-make-your-project-easier-per-experience",
        usefulness_per_experience,
    )

    iterate = "Are there cases where you wanted to be able to iterate over lists of different types in Rust?"
    iterate_q = db.q_simple_single(iterate)
    report.add_pie_chart(
        "variadics-iteration",
        iterate_q,
    )

    def iteration_per_experience(**kwargs) -> Figure:
        df = db.df[[iterate, rust_usage]].dropna()
        df = df.rename(columns={
            rust_usage: "Experience",
            iterate: "List iteration"
        })

        fig = make_chart(
            iterate_q.with_title(lambda q: f"{q} (per Rust experience)"),
            df,
            kind="pie",
            x="List iteration",
            facet_col="Experience",
            facet_col_wrap=3,
            height=800,
            category_orders={
                "Experience": experience_order,
                "List iteration": ["Yes", "No"]
            }
        )
        fig.update_layout(
            legend={
                "orientation": "h",
            }
        )
        return shorten_annotations(fig)

    report.add_custom_chart(
        "variadics-iteration-per-experience",
        iteration_per_experience
    )

    mappings = "Are there cases where variadic mappings would have made your project easier?"
    mappings_q = db.q_simple_single(mappings)
    report.add_pie_chart(
        "variadics-mappings",
        mappings_q,
    )

    def mappings_per_experience(**kwargs) -> Figure:
        df = db.df[[mappings, rust_usage]].dropna()
        df = df.rename(columns={
            rust_usage: "Experience",
            mappings: "Variadic mappings"
        })

        fig = make_chart(
            mappings_q.with_title(lambda q: f"{q} (per Rust experience)"),
            df,
            kind="pie",
            x="Variadic mappings",
            facet_col="Experience",
            facet_col_wrap=3,
            height=800,
            category_orders={
                "Experience": experience_order,
                "Variadic mappings": ["Yes", "No"]
            }
        )
        fig.update_layout(
            legend={
                "orientation": "h",
            }
        )
        return shorten_annotations(fig)

    report.add_custom_chart(
        "variadics-mappings-per-experience",
        mappings_per_experience
    )

    non_linear = "Are there cases where non-linear mappings would have made your project easier?"
    non_linear_q = db.q_simple_single(non_linear)
    report.add_pie_chart(
        "variadics-non-linear",
        non_linear_q,
    )

    def non_linear_per_experience(**kwargs) -> Figure:
        df = db.df[[non_linear, rust_usage]].dropna()
        df = df.rename(columns={
            rust_usage: "Experience",
            non_linear: "Non-linear variadics"
        })

        fig = make_chart(
            non_linear_q.with_title(lambda q: f"{q} (per Rust experience)"),
            df,
            kind="pie",
            x="Non-linear variadics",
            facet_col="Experience",
            facet_col_wrap=3,
            height=800,
            category_orders={
                "Experience": experience_order,
                "Non-linear variadics": ["Yes", "No"]
            }
        )
        fig.update_layout(
            legend={
                "orientation": "h",
            }
        )
        return shorten_annotations(fig)

    report.add_custom_chart(
        "variadics-non-linear-per-experience",
        non_linear_per_experience
    )

    priority = "How high a priority would you say variadics are for you?"
    report.add_bar_chart(
        "variadics-priority",
        db.q_simple_single(priority),
        xaxis_tickangle=45,
        sort_by_pct=False,
    )

    return report


if __name__ == "__main__":
    random.seed(0x0D15EA5E)
    np.random.seed(0x0D15EA5E)

    report = analyze()

    render_report_to_pdf(
        report,
        Path(__file__).parent / "variadics-survey-2025-report.pdf",
        "Rust Variadics survey 2025 report",
        include_labels=True,
    )

    # blog_dir = ROOT_DIR.parent / "blog.rust-lang.org"
    # blog_post_rel_path = Path("content/rust-debugging-survey-2026-results")
    # template_path = Path(CURRENT_DIR / "blog.md")
    # render_blog_post(
    #     template=template_path,
    #     blog_dir=blog_dir,
    #     blog_post_rel_path=blog_post_rel_path,
    #     report=report,
    # )
