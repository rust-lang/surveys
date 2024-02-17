import math
import string
import textwrap
from collections import defaultdict
from typing import List, Any, Dict, Optional

import numpy as np
import pandas as pd
import plotly.express as px
from plotly.graph_objs import Figure
from wordcloud import WordCloud

from .survey import Question, MatrixQuestion


def format_title(question: Question, include_kind: bool = False) -> str:
    kind = ""
    if include_kind:
        kind = "single answer" if question.is_single_answer() else "multiple answers"
        kind = f", {kind}"

    return f'<b>{wrap_text(question.question, max_width=75)}</b><br /><span style="font-size: 0.8em;">(total responses = {question.total_responses}{kind})</span>'


def wrap_text(text: str, max_width: int) -> str:
    text = textwrap.wrap(text, width=max_width, break_long_words=False)
    text = "<br />".join(text)
    return text


def make_bar_chart(
        questions: List[Question],
        height=600,
        bar_label_vertical=False,
        xaxis_tickangle=0,
        max_tick_width=30,
        legend_order: Optional[List[str]] = None,
        layout_args: Optional[Dict[str, Any]] = None
) -> Figure:
    assert len(questions) > 0
    assert len(set(question.year for question in questions)) == len(questions)

    if legend_order is not None:
        legend_order = [wrap_text(l, max_width=max_tick_width) for l in legend_order]

    data = defaultdict(list)
    totals = {}

    for question in questions:
        assert question.is_simple()
        for answer in question.kind.answers:
            text = wrap_text(answer.answer, max_width=max_tick_width)

            data["year"].append(str(question.year))
            data["answer"].append(text)
            data["count"].append(answer.count)
        totals[str(question.year)] = question.total_responses
    data = pd.DataFrame(data)
    multiyear = len(data["year"].unique()) > 1

    answers = list(data["answer"].unique())

    # To have a nicer legend
    data = data.rename(columns={"year": "Year"})
    data["percent"] = 0.0

    # Backfill missing answers
    for answer in answers:
        for year in totals.keys():
            count = data[(data["answer"] == answer) & (data["Year"] == year)]
            if len(count) == 0:
                data = pd.concat((data, pd.DataFrame({
                    "answer": [answer],
                    "Year": [year],
                    "count": [0]
                })))

    # Calculate percent from all responses of that given year
    for (year, total_count) in totals.items():
        counts = data.loc[data["Year"] == year, "count"].astype(np.float32)
        data.loc[data["Year"] == year, "percent"] = (counts / total_count) * 100.0

    main_year = str(questions[0].year)

    def sort_key(answer: str) -> int:
        if legend_order is not None:
            return legend_order[::-1].index(answer)

        key = (data["answer"] == answer) & (data["Year"] == main_year)
        return int(data.loc[key, "count"].sum())

    answers = sorted(answers, key=sort_key, reverse=True)

    # Generate label that is shown above each bar
    def generate_text(row) -> str:
        value = row["percent"]
        if math.isclose(value, 0.0):
            return "N/A"
        return f"{value:.1f}%"

    data["text"] = data.apply(generate_text, axis=1)

    fig = px.bar(
        data,
        x="answer",
        y="percent",
        color="Year",
        barmode="group",
        text="text",
        custom_data=["Year", "count"],
        category_orders={"answer": answers},
        height=height,
    )
    fig.update_traces(
        textposition="outside",
        hovertemplate="Year: %{customdata[0]}<br />Count: %{customdata[1]}<br />Percent: %{text}<extra></extra>",
        textangle=-90 if bar_label_vertical else 0,
    )

    layout_args = layout_args or {}
    fig.update_layout(
        meta="bar-chart",
        hoverlabel=dict(
            bgcolor="white",
            font_size=16,
            font_family="Rockwell"
        ),
        hovermode="x unified",
        xaxis_title=None,
        # xaxis_tickwidth=40,
        xaxis_tickangle=xaxis_tickangle,
        yaxis_title="Percent out of all responses (%)",
        yaxis_range=[0, 119],
        yaxis_ticksuffix="%",
        yaxis_fixedrange=True,
        title_text=format_title(questions[0], include_kind=True),
        plot_bgcolor="rgb(255, 255, 255)",
        showlegend=multiyear,
        uniformtext=dict(
            minsize=12,
            mode="show"
        ),
        margin=dict(
            pad=10,
            b=10
        ),
        dragmode="pan",
        **layout_args
    )

    title_standoff = 50
    if height > 400:
        title_standoff = 25
    fig.update_yaxes(
        nticks=10,
        rangemode="tozero",
        gridcolor="rgb(229, 236, 246)",
        title_standoff=title_standoff
        # showgrid=False
    )

    return fig


def make_pie_chart(
        question: Question,
        height=800,
        legend_params: Optional[Dict[str, Any]] = None,
        legend_order: Optional[List[str]] = None,
        max_label_width=30,
) -> Figure:
    assert question.is_simple()

    # For questions with multiple answers, a pie chart would show wrong results
    assert question.is_single_answer()

    data = defaultdict(list)
    for answer in question.kind.answers:
        text = wrap_text(answer.answer, max_width=max_label_width)
        data["answer"].append(text)
        data["count"].append(answer.count)
        data["percent"].append((answer.count / question.total_responses) * 100)

    category_orders = {}
    if legend_order is not None:
        category_orders["answer"] = legend_order

    df = pd.DataFrame(data)
    fig = px.pie(
        df,
        values="count",
        names="answer",
        title=format_title(question),
        custom_data=["percent"],
        height=height,
        category_orders=category_orders
    )
    fig.update_traces(
        # textposition="outside",
        # textinfo="percent+label",
        # outsidetextfont=dict(size=10),
        textposition="inside",
        textinfo="percent",
        hovertemplate="Answer: %{label}<br />Count: %{value} <br />Percent: %{customdata:.2f}%"
    )

    legend = {}
    # y=0,
    # x=0,
    # xref="container",
    # yref="container",
    # yanchor="top",
    # xanchor="right",
    if legend_params is not None:
        legend.update(legend_params)

    fig.update_layout(
        meta="pie-chart",
        hoverlabel=dict(
            bgcolor="white",
            font_size=16,
            font_family="Rockwell",
        ),
        # showlegend=False,
        showlegend=True,
        legend=legend,
        margin=dict(
            l=0,
            b=0,
            pad=0
        ),
        dragmode="pan"
    )

    return fig


def make_matrix_chart(
        question: Question,
        categories: List[str],
        category_label: str,
        height=600,
        horizontal: bool = False,
        max_label_width=20,
        legend_params: Optional[Dict[str, Any]] = None
) -> Figure:
    """
    Create a matrix chart with different categories.
    `categories`: List of categories, sorted from most to least important
    """
    assert isinstance(question.kind, MatrixQuestion)

    mapping = dict(zip(categories[::-1], range(1, len(categories) + 1)))

    items = question.kind.answer_groups.items()
    items = [(wrap_text(group, max_width=max_label_width), value) for (group, value) in items]

    group_score = {}
    data = defaultdict(list)
    for (group, levels) in items:
        score = 0
        total_count = sum(answer.count for answer in levels)
        for answer in levels:
            data["Category"].append(group)
            data[category_label].append(answer.answer)

            percent = (answer.count / total_count) * 100
            data["Count"].append(percent)
            data["Percent (out of this category)"].append(f"{percent:.2f}%")
            score += answer.count * mapping[answer.answer]
        score /= total_count
        group_score[group] = score

    group_keys = sorted(group_score.keys(), key=lambda k: group_score[k], reverse=True)
    df = pd.DataFrame(data)

    keys = dict(x="Count", y="Category")
    if not horizontal:
        keys = dict(y="Count", x="Category")

    fig = px.bar(
        df,
        **keys,
        color=category_label,
        text="Percent (out of this category)",
        category_orders=dict(
            Category=group_keys
        ),
        title=format_title(question),
        height=1000 if not horizontal else height,
        hover_data=[category_label]
    )
    fig.update_traces(
        orientation="h" if horizontal else "v",
        textposition="outside",
        hovertemplate=f"Category: %{{y}}<br />{category_label}: %{{customdata[0]}}<br />Percent: %{{text}}<extra></extra>",
    )

    legend = {}
    if legend_params is not None:
        legend.update(legend_params)

    layout_args = {}
    if horizontal:
        layout_args["xaxis_range"] = [0, 110]

    fig.update_layout(
        meta="matrix-chart",
        hoverlabel=dict(
            bgcolor="white",
            font_size=16,
            font_family="Rockwell",
        ),
        # hovermode="y unified",
        yaxis_title=None,
        yaxis_tickangle=0,
        # https://stackoverflow.com/a/52397461/1107768
        yaxis_ticksuffix="   ",
        yaxis_fixedrange=True,
        xaxis_title="Percent out of the category (%)",
        xaxis_ticksuffix="%",
        xaxis_fixedrange=True,
        legend=legend,
        dragmode="pan",
        **layout_args
    )
    fig.update_xaxes(
        showgrid=False,
    )

    return fig


def make_wordcloud(answers: List[str], height=600) -> bytes:
    from matplotlib import colormaps
    from .render import pillow_to_png_bytes

    text = " ".join(answers)
    printable = set(string.printable)
    text = "".join(c for c in text if c in printable)

    wc = WordCloud(
        width=800,
        height=height,
        scale=1,
        min_word_length=3,
        colormap=colormaps["summer"],
        max_words=50,
        random_state=42
    ).generate(text)
    return pillow_to_png_bytes(wc.to_image())
