import math
import random
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import plotly.express as px
from plotly.graph_objs import Figure

from surveyhero.chart import format_title, wrap_text
from surveyhero.render import render_blog_post, render_report_to_pdf
from surveyhero.report import ChartReport
from surveyhero.survey import (
    Answer,
    Question,
    QuestionKind,
    SimpleQuestion,
)

ROOT_DIR = Path(__file__).absolute().parent.parent.parent.parent
REPORT_SCRIPT_DIR = ROOT_DIR / "report"

sys.path.insert(0, str(REPORT_SCRIPT_DIR))


def make_bar_group_chart(
        question: Question,
        yaxis_tickangle=0,
        max_tick_width=30,
        layout_args: dict[str, Any] | None = None,
        legend_params: dict[str, Any] | None = None,
        range=(0, 119)
) -> Figure:
    assert isinstance(question.kind, SimpleQuestion)

    legend_order = [a.answer for a in question.kind.answers]

    # We need to apply the size hack also to the legend, otherwise the answers won't match
    legend_order = [wrap_text(
        l,
        max_width=max_tick_width,
    ) for l in legend_order]

    data = defaultdict(list)
    totals = {}

    for answer in question.kind.answers:
        text = wrap_text(
            answer.answer,
            max_width=max_tick_width,
        )
        is_child = text.find("↳ ") != -1

        data["year"].append(str(question.year))
        data["answer"].append(text)
        data["count"].append(answer.count)
        data["color"].append("#8DA9DB" if is_child else px.colors.qualitative.Plotly[0])
    totals[str(question.year)] = question.total_responses

    data = pd.DataFrame(data)
    multiyear = len(data["year"].unique()) > 1

    answers = list(data["answer"].unique())

    # To have a nicer legend
    data = data.rename(columns={"year": "Year"})
    data["value"] = 0.0
    data["percent"] = 0.0


    # Calculate percent from all responses of that given year
    for (year, total_count) in totals.items():
        counts = data.loc[data["Year"] == year, "count"].astype(np.float32)
        data.loc[data["Year"] == year, "value"] = counts
        data.loc[data["Year"] == year, "percent"] = (counts / total_count) * 100.0

    main_year = str(question.year)


    def sort_key(answer: str) -> int:
        return legend_order[::-1].index(answer)

        key = (data["answer"] == answer) & (data["Year"] == main_year)
        return int(data.loc[key, "count"].sum())

    answers = sorted(answers, key=sort_key, reverse=True)

    # Generate label that is next to each bar
    def generate_text(row) -> str:
        value = row["value"]
        percent = row["percent"]
        if math.isclose(percent, 0.0):
            return "N/A"
        return f"{int(value)} ({percent:.1f}%)"

    data["text"] = data.apply(generate_text, axis=1)

    palette = [px.colors.qualitative.Plotly[0]]

    fig = px.bar(
        data,
        orientation="h",
        y="answer",
        x="percent",
        height=len(question.kind.answers) * 50 + 100,
        color="Year",
        color_discrete_sequence=palette,
        barmode="group",
        text="text",
        custom_data=["Year", "count", "percent"],
        category_orders={"answer": answers},
    )
    fig.update_traces(
        textposition="outside",
        hovertemplate="Count: %{customdata[1]}<br />Percent: %{customdata[2]:.1f}%<extra></extra>",
        textangle=0,
    )

    legend = {}
    if legend_params is not None:
        legend.update(legend_params)

    layout_args = layout_args or {}
    fig.update_layout(
        meta="bar-chart",
        hoverlabel={
            "bgcolor": "white",
            "font_size": 16,
            "font_family": "Rockwell"
        },
        hovermode="y unified",
        # yaxis_tickheight=40,
        yaxis_tickangle=yaxis_tickangle,
        yaxis_title="",
        xaxis_title="Answer count (percentage)",
        xaxis_range=range,
        xaxis_ticksuffix="%",
        xaxis_fixedrange=True,
        title={
            "text": format_title(question, include_kind=True),
        },
        plot_bgcolor="rgb(255, 255, 255)",
        showlegend=multiyear,
        uniformtext={
            "minsize": 12,
            "mode": "show"
        },
        margin={
            "t": 100,
            "pad": 10,
        },
        legend=legend,
        dragmode="pan",
        **layout_args
    )

    title_standoff = 50
    fig.update_xaxes(
        nticks=10,
        rangemode="tozero",
        gridcolor="rgb(229, 236, 246)",
        title_standoff=title_standoff
        # showgrid=False
    )

    colors = list(data["color"])
    fig.update_traces(
        marker_color=colors,
        selector={"type": "bar"}
    )

    return fig

# ===

def total_answers(question: QuestionKind):
    assert isinstance(question, SimpleQuestion)
    return sum([answer.count for answer in question.answers])

question1 = Question(
    id=1,
    year=2025,
    question="How long have you been using Rust?",
    total_responses=0,
    kind=SimpleQuestion(
        answers=[
            Answer(answer="Never", count=24),
            Answer(answer="Zero to two years", count=493),
            Answer(answer="Two to four years", count=1121),
            Answer(answer="Four to six years", count=867),
            Answer(answer="More than six years", count=804),
        ]
    )
)
question1.total_responses = total_answers(question1.kind)

question2 = Question(
    id=2,
    year=2025,
    question="Have you heard about variadic generics before?",
    total_responses=0,
    kind=SimpleQuestion(
        answers=[
            Answer(answer="Yes", count=2718),
            Answer(answer="No", count=586),
        ]
    )
)
question2.total_responses = total_answers(question2.kind)

question3 = Question(
    id=3,
    year=2025,
    question="Where have you heard about variadic generics?",
    total_responses=0,
    kind=SimpleQuestion(
        answers=[
            Answer(answer="Pre-RFCs and discussions on internals.rust-lang.org.", count=833),
            Answer(answer="Discussions on Reddit.", count=1236),
            Answer(answer="Blog posts on poignardazur.github.io.", count=1176),
            Answer(answer="Other programming languages.", count=1630),
            Answer(answer="Other means: (open response)", count=190),
        ]
    )
)
question3.total_responses = total_answers(question3.kind)

question4 = Question(
    id=4,
    year=2025,
    question="Where have you heard about variadic generics? (Open answers)",
    total_responses=190,
    kind=SimpleQuestion(
        answers=[
            Answer(answer="Bevy", count=60),
            Answer(answer="Discord", count=45),
            Answer(answer="<i>↳ Bevy Discord server</i>", count=22),
            Answer(answer="<i>↳ RPLCS</i>", count=10),
            Answer(answer="Zulip", count=16),
            Answer(answer="Solving a problem", count=15),
            Answer(answer="Other social apps", count=14),
            Answer(answer="Friends or colleagues", count=14),
            Answer(answer="Github", count=13),
            Answer(answer="This Week in Rust", count=7),
            Answer(answer="Existing code or docs", count=7),
        ]
    )
)

question5 = Question(
    id=5,
    year=2025,
    question="Are there cases where variadic generics would have made your project easier?",
    total_responses=0,
    kind=SimpleQuestion(
        answers=[
            Answer(answer="Yes", count=1702),
            Answer(answer="No", count=1319),
        ]
    )
)
question5.total_responses = total_answers(question5.kind)

question6 = Question(
    id=6,
    year=2025,
    question="Are there cases where variadic generics would have made your project easier? (Open answers)",
    total_responses=1025,
    kind=SimpleQuestion(
        answers=[
            Answer(answer="Implementing SomeTrait for all tuples of SomeTrait", count=227),
            Answer(answer="<i>↳ For UI</i>", count=47),
            Answer(answer="<i>↳ For serialization</i>", count=19),
            Answer(answer="Implementing traits for all function types", count=97),
            Answer(answer="<i>↳ Implementing function wrappers</i>", count=34),
            Answer(answer="Combining parsers or state machines", count=112),
            Answer(answer="<i>↳ For SQL/ORM queries</i>", count=38),
            Answer(answer="<i>↳ For Web/RPC/REST endpoints</i>", count=24),
            Answer(answer="<i>↳ For file parsing</i>", count=17),
            Answer(answer="Variadic functions", count=65),
            Answer(answer="<i>↳ zip-like functions</i>", count=26),
            Answer(answer="<i>↳ println-like functions, logging</i>", count=18),
            Answer(answer="<i>↳ join-like functions</i>", count=8),
            Answer(answer="Structure-of-arrays and ECS", count=52),
            Answer(answer="Dependency injection", count=38),
            Answer(answer="Representing a graph node", count=38),
            Answer(answer="<i>↳ For a compiler/interpreter</i>", count=20),
            Answer(answer="Language interop", count=32),
            Answer(answer="<i>↳ With C++</i>", count=8),
            Answer(answer="<i>↳ With C variadic functions</i>", count=6),
            Answer(answer="<i>↳ With Python</i>", count=6),
            Answer(answer="<i>↳ With Lua</i>", count=5),
            Answer(answer="<i>↳ With another language</i>", count=7),
            Answer(answer="N-dimensional maths", count=20),
            Answer(answer="Builder pattern", count=9),
            Answer(answer="Function pipelines", count=6),
            Answer(answer="io_uring", count=4),
        ]
    )
)

question7 = Question(
    id=7,
    year=2025,
    question="Mentioned wanting variadics for a specific project",
    total_responses=0,
    kind=SimpleQuestion(
        answers=[
            Answer(answer="Bevy", count=83),
            Answer(answer="Axum", count=21),
            Answer(answer="Diesel", count=9),
        ]
    )
)
question7.total_responses = total_answers(question7.kind)

question8 = Question(
    id=8,
    year=2025,
    question="People who mentioned disliking the macro workaround",
    total_responses=51,
    kind=SimpleQuestion(
        answers=[
            Answer(answer="Documentation bloat", count=10),
            Answer(answer="Unreadable compile errors", count=14),
            Answer(answer="Source code bloat", count=13),
            Answer(answer="Long compile times", count=13),
        ]
    )
)

question9 = Question(
    id=9,
    year=2025,
    question="Are there cases where variadic mappings would have made your project easier?",
    total_responses=0,
    kind=SimpleQuestion(
        answers=[
            Answer(answer="Yes ", count=1287),
            Answer(answer="No ", count=1168),
        ]
    )
)
question9.total_responses = total_answers(question9.kind)

question10 = Question(
    id=10,
    year=2025,
    question="Are there cases where non-linear mappings would have made your project easier?",
    total_responses=0,
    kind=SimpleQuestion(
        answers=[
            Answer(answer="Yes ", count=696),
            Answer(answer="No ", count=1537),
        ]
    )
)
question10.total_responses = total_answers(question10.kind)

question11 = Question(
    id=11,
    year=2025,
    question="Are there cases where non-linear mappings would have made your project easier? (Open answers)",
    total_responses=205,
    kind=SimpleQuestion(
        answers=[
            Answer(answer="Type filtering", count=38),
            Answer(answer="<i>↳ For Bevy queries </i>", count=10),
            Answer(answer="As a specialization workaround", count=18),
            Answer(answer="Other specific use-cases", count=19),
        ]
    )
)
question11.total_responses = total_answers(question11.kind)

question12 = Question(
    id=12,
    year=2025,
    question="How high a priority would you say variadics are for you?",
    total_responses=0,
    kind=SimpleQuestion(
        answers=[
            Answer(answer="It should be the highest priority feature", count=48),
            Answer(answer="Very important", count=286),
            Answer(answer="Moderately important", count=599),
            Answer(answer="Nice to have", count=1015),
            Answer(answer="I don't care", count=182),
            Answer(answer="I don't want Rust to have variadics", count=99),
        ]
    )
)
question12.total_responses = total_answers(question12.kind)

question13 = Question(
    id=13,
    year=2025,
    question="Do you have any further comments related to variadic generics?",
    total_responses=572,
    kind=SimpleQuestion(
        answers=[
            Answer(answer="I really want variadics", count=34),
            Answer(answer="Variadics add too much complexity to the language", count=22),
            Answer(answer="Rust must not become like C++", count=18),
            Answer(answer="I miss variadics from C++", count=22),
            Answer(answer="Macros work fine as a workaround", count=25),
            Answer(answer="Non-linear variadics are too complex", count=13),
            Answer(answer="The article's example syntax is bad ", count=28),
            Answer(answer="<i>↳ Should be keyword-based, not dot-dot-dot</i>", count=5),
            Answer(answer="<i>↳ The 'for where' non-linear syntax is bad</i>", count=7),
            Answer(answer="Feature X is more important", count=23),
            Answer(answer="We should have type-to-type functions", count=7),
            Answer(answer="Variadics should also cover struct fields", count=8),
            Answer(answer="Compliments/thanks", count=18),
        ]
    )
)
question13.total_responses = total_answers(question13.kind)

# ===

def write_file(path: Path, content: bytes):
    with open(path, "wb") as f:
        f.write(content)

def write_chart(chart: Figure, filename: str):
    assert chart
    svg_bytes = chart.to_image(format="svg")
    assert svg_bytes
    write_file(Path(f"./{filename}.svg"), svg_bytes)
    png_bytes = chart.to_image(format="png")
    assert png_bytes
    write_file(Path(f"./{filename}.png"), png_bytes)


def variadic_use_cases_report() -> ChartReport:
    report = ChartReport()

    report.add_custom_chart("how-long-rust", lambda: make_bar_group_chart(question1, range=(0, 60)))
    report.add_pie_chart("heard-about-variadics", question2)
    report.add_custom_chart("where-heard-about-variadics", lambda: make_bar_group_chart(question3, range=(0, 60)))
    report.add_custom_chart("where-heard-about-variadics-open", lambda: make_bar_group_chart(question4, range=(0, 60)))
    report.add_pie_chart("use-cases-variadic-generics", question5)
    report.add_custom_chart("use-cases-variadic-generics-open", lambda: make_bar_group_chart(question6, range=(0, 35)))
    report.add_custom_chart("specific-project", lambda: make_bar_group_chart(question7, range=(0, 100)))
    report.add_custom_chart("disliked-macros", lambda: make_bar_group_chart(question8, range=(0, 60)))
    report.add_pie_chart("use-cases-variadic-mappings", question9)
    report.add_pie_chart("use-cases-variadic-nonlinear", question10)
    report.add_custom_chart("use-cases-variadic-nonlinear-open", lambda: make_bar_group_chart(question11, range=(0, 60)))
    report.add_custom_chart("variadics-priority-level", lambda: make_bar_group_chart(question12, range=(0, 60)))
    report.add_custom_chart("last-comments", lambda: make_bar_group_chart(question13, range=(0, 60)))

    return report


if __name__ == "__main__":
    random.seed(42)
    np.random.seed(42)

    report = variadic_use_cases_report()

    template_path = Path(__file__).absolute().parent / "2025-09-variadic-use-cases-results.md"

    # Fill path to blog roost
    blog_dir = Path("/home/olivier-faure/Documents/blog.rust-lang.org/content2/variadic_results/")
    render_blog_post(
        template=template_path,
        blog_dir=blog_dir,
        report=report
    )

    render_report_to_pdf(
        report,
        Path(__file__).parent / "variadic-use-cases-results.pdf",
        "Variadic Generics Micro Survey results",
        include_labels=False
    )


# render_png requires Kaleido which requires Chrome
