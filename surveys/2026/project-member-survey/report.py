import math
import random
import sys
from collections import defaultdict
from pathlib import Path
from typing import List, Iterable, Callable
import json

import numpy as np
import pandas as pd
from plotly.graph_objs import Figure

from surveyhero.utils import is_nan, inspect_open_answers
from surveyhero.chart import make_histogram_chart, make_chart
from surveyhero.parser import parse_surveyhero_summary, parse_surveyhero_answers
from surveyhero.render import render_report_to_pdf
from surveyhero.report import ChartReport
from surveyhero.survey import Question, SurveyFullAnswers, SurveySummary

ROOT_DIR = Path(__file__).absolute().parent.parent.parent.parent


def analyze(including_secret_data: bool) -> ChartReport:
    summary_2025 = parse_surveyhero_summary(Path(ROOT_DIR / "data/2025/contributor/summary.csv"),
                                            year=2025)
    db_2025 = parse_surveyhero_answers(Path(ROOT_DIR / "data/2025/contributor/responses.csv"),
                                       year=2025, summary=summary_2025)

    summary = parse_surveyhero_summary(Path(ROOT_DIR / "data/2026/member/summary.csv"),
                                       year=2026)
    db = parse_surveyhero_answers(
        Path(ROOT_DIR / "data/2026/member/responses.csv"), year=2026, summary=summary)

    # Normalize
    def normalize_money(money: str) -> str:
        if money in ("never", "(not practical for me)"):
            return "never"
        if isinstance(money, float) and np.isnan(money):
            return str(money)

        if money.endswith("$"):
            money = money[:-1]
        if "-" in money:
            money = money.split("-")[-1]
        money = money.replace(",", "").replace(".", "")
        return str(int(money))

    money_columns = ["4-5 days per week (full-time)", "2-3 days per week (part-time)",
                     "1 day per week or less"]
    # for col in money_columns:
    #     db.df[col] = db.df[col].apply(normalize_money)
    username_name = "What is your GitHub username?"

    def fixup_reward(username: str, fixup: Callable[[int], int]):
        df = db.df
        row_index = df[df[username_name] == username].index[0]
        for col in money_columns:
            value = df.at[row_index, col]
            if value != "never" and not is_nan(value):
                print(f"Changing {value} to {fixup(value)}")
                df.at[row_index, col] = fixup(value)

    try:
        with open("usernames_yearly_to_monthly.csv", "r") as f:
            for row in f:
                username = row.strip()
                fixup_reward(username, lambda v: int(v) / 12)
    except FileNotFoundError:
        pass

    open1 = db.open_answers_raw(
        "Do you have any other comments regarding Rust Project contributor funding and its sustainability?")
    with open("final-open-answers.txt", "w") as f:
        for answer in open1:
            f.write(f"{answer}\n---\n\n")

    open2 = db.open_answers_raw(
        "Do you have any thoughts on how the Rust Foundation Maintainers Fund has been operating so far?")
    with open("rfmf-open-answers.txt", "w") as f:
        for answer in open2:
            f.write(f"{answer}\n---\n\n")

    continent_to_country = {}

    try:
        with open("continent_to_country.json", "r") as f:
            continent_to_country = json.load(f)
    except FileNotFoundError:
        pass

    def get_continent(country: str) -> str:
        if isinstance(country, float) and math.isnan(country):
            return np.nan

        country = [c.strip() for c in country.split(",")][-1]
        if country in ["Europe"]:
            return country

        if country.islower():
            country = country[0].upper() + country[1:]

        # Country == continent
        if country in continent_to_country:
            return country
        for (continent, countries) in continent_to_country.items():
            if country in countries:
                return continent
        raise Exception(f"Continent not found for `{country}`")

    location = db.df["Where are you located?"]
    db.df["continent"] = location.apply(get_continent)
    db.df = db.df.rename(columns={
        "I am not studying, and I am unemployed or without a job": "Unemployed"
    })

    # Start of analysis
    report = ChartReport()

    contrib_reason_name = "Why did you start contributing to the Rust Project?"
    report.add_bar_chart("why-did-you-start-contributing",
                         db.q_simple_multi(contrib_reason_name),
                         sort_by_pct=False,
                         xaxis_tickangle=45)

    contrib_start_name = "When did you start contributing to the Rust Project?"
    report.add_bar_chart("when-did-you-start-contributing",
                         db.q_simple_single(contrib_start_name),
                         sort_by_pct=False,
                         xaxis_tickangle=45)

    are_you_funded_name = "Are you funded for your Rust Project contributions?"
    are_you_funded_q = db.q_simple_single(are_you_funded_name)
    report.add_bar_chart("are-you-funded", are_you_funded_q,
                         sort_by_pct=False,
                         xaxis_tickangle=45)

    contribution_start_df = db.df[contrib_start_name]

    def map_nan(value, func):
        if is_nan(value):
            return value
        return func(value)

    def iterate_teams(answer: str) -> Iterable[str]:
        if not is_nan(answer):
            for answer in answer.split(","):
                answer = answer.strip().lower()
                if answer.startswith("t-"):
                    answer = answer[2:]
                yield answer.replace(" ", "-")

    are_you_funded_df = db.df[are_you_funded_name].apply(
        lambda v: map_nan(v, lambda v: "yes" if v.startswith("Yes") else "no"))

    funded_df = defaultdict(list)
    for (funded, teams, start) in zip(are_you_funded_df,
                                      db.df["What Rust teams are you a part of?"],
                                      contribution_start_df):
        for team in iterate_teams(teams):
            funded_df["funded"].append(funded)
            funded_df["team"].append(team)
            funded_df["start"].append(start)

    def update_facet_title(annotation):
        original = annotation.text
        new_text = original.split("=")[-1]
        annotation.update(text=new_text)

    def shorten_annotations(fig: Figure) -> Figure:
        fig.for_each_annotation(update_facet_title)
        return fig

    category_order_start_contributing = [
        "During 2018 or before",
        "During 2019 or 2020",
        "During 2021 or 2022",
        "During 2023 or 2024",
        "During 2025"
    ]

    def draw_funded_per_start_contributing() -> Figure:
        return shorten_annotations(
            make_chart(are_you_funded_q, funded_df,
                       x="funded",
                       kind="bar",
                       facet_col="start",
                       category_orders=dict(start=category_order_start_contributing)))

    report.add_custom_chart("are-you-funded-per-start-of-contribution",
                            draw_funded_per_start_contributing)

    funded_df = pd.DataFrame(funded_df)
    funded_df = funded_df[
        funded_df["team"].isin(("compiler", "libs", "leadership council", "cargo", "rustup",
                                "clippy", "infra", "libs-contributors", "rustdoc", "crates.io"))]

    def draw_funded_per_team() -> Figure:
        fig = make_chart(are_you_funded_q, funded_df,
                         x="funded",
                         kind="bar",
                         facet_col="team")

        fig.for_each_annotation(update_facet_title)
        return fig

    report.add_custom_chart("are-you-funded-per-team", draw_funded_per_team)

    why_not_funded_name = "Why are you not funded anymore?"
    report.add_bar_chart("why-are-you-not-funded-anymore",
                         db.q_simple_multi(why_not_funded_name),
                         xaxis_tickangle=45)
    # report.add_wordcloud("why-are-you-not-funded-anymore-wordcloud",
    #                      db.open_answers(why_not_funded_name))

    how_much_time_name = "How much time do you spend contributing to the Rust Project monthly?"
    how_much_time_df = db.df[how_much_time_name]
    # how_much_time_df = how_much_time_df.apply(lambda v: map_nan(v, lambda v: v if v < 500 else 160))
    how_much_time_df = pd.DataFrame({
        "Hours per month": how_much_time_df
    }).dropna()

    time_q = (
        db.q_simple_single(how_much_time_name)
        .integer_answers()
        # .combine_answers({
        #     "160": ["160", "1000"]
        # })
    )
    report.add_custom_chart("how-much-time-do-you-spend-contributing",
                            lambda: make_chart(time_q, how_much_time_df, y="Hours per month",
                                               kind="box", points="all"))

    report.add_custom_chart("how-much-time-do-you-spend-contributing-cdf",
                            lambda: make_chart(time_q, how_much_time_df, x="Hours per month",
                                               kind="cdf"))

    funded_ratio_name = "How much of your time spent on Rust Project contributions is funded?"
    funded_ratio_df = db.df[funded_ratio_name]
    funded_ratio_df = funded_ratio_df.apply(lambda v: map_nan(v, lambda v: min(v, 100)))
    funded_ratio_df = pd.DataFrame({
        "% of contributions funded": funded_ratio_df
    }).dropna()
    funded_ratio_q = (
        db.q_simple_single(funded_ratio_name)
        .integer_answers()
        .map_answers(lambda c: int((int(c) / 160) * 100) if int(c) > 100 else c)
    )
    report.add_custom_chart("how-much-time-is-funded",
                            lambda: make_histogram_chart(funded_ratio_q,
                                                         x_label="% of contributions funded"))
    report.add_custom_chart("how-much-time-is-funded-cdf",
                            lambda: make_chart(funded_ratio_q, funded_ratio_df,
                                               x="% of contributions funded",
                                               kind="cdf"))

    funded_name = "How are you funded for your Rust Project contributions?"
    report.add_bar_chart("how-are-you-funded", db.q_simple_multi(funded_name), xaxis_tickangle=45)
    report.add_wordcloud("how-are-you-funded-wordcloud", db.open_answers(funded_name))

    report.add_bar_chart("how-long-have-you-been-funded", db.q_simple_single(
        "How long have you been funded for your Rust Project contributions?"), xaxis_tickangle=45,
                         sort_by_pct=False)

    contract_end_q = (
        db.q_simple_single("When does your contract/employment end?", treat_unknown_answers_as=None)
    )
    contract_end_q = db.treat_unknown_answers_as(contract_end_q, "Other")
    report.add_bar_chart("when-does-your-contract-end",
                         contract_end_q,
                         xaxis_tickangle=45,
                         sort_by_pct=False)

    likely_lose_name = "How likely is it that you will lose your funding in the near future?"
    report.add_bar_chart("how-likely-to-lose-funding", db.q_simple_single(likely_lose_name),
                         xaxis_tickangle=45,
                         sort_by_pct=False)

    contributions_directed_name = "Are your contributions directed by your source of funding?"
    # inspect_open_answers(db.open_answers(contributions_directed_name))
    # report.add_bar_chart("are-contributions-directed",
    #                      db.q_simple_single(contributions_directed_name))
    # report.add_wordcloud("are-contributions-directed-wordcloud",
    #                      db.open_answers(contributions_directed_name))

    money_name = "How much money would you like to be paid for contributing to the Rust Project?"
    baseline_money_df = db.get_answer_columns(db.get_column(money_name), answer_count=5)
    baseline_money_df["continent"] = db.df["continent"]
    baseline_money_df["employment-fulltime"] = db.df["4-5 days per week (full-time employment)"]
    baseline_money_df["employment-parttime"] = db.df["2-3 days per week (part-time employment)"]
    baseline_money_df["contracting-fulltime"] = db.df["4-5 days per week (full-time contracting)"]
    baseline_money_df["contracting-parttime"] = db.df["2-3 days per week (part-time contracting)"]

    baseline_money_q = db.q_simple_multi(money_name, answer_count=5)

    test_df = baseline_money_df.copy()
    test_df["contributor"] = db.open_answers_raw("What is your GitHub username?", dropna=False)
    test_df = test_df.dropna(subset=["contributor"])

    # test_df = test_df[test_df["contributor"].isnull()]

    def norm(v):
        if is_nan(v):
            return v
        if v == "never":
            return 0
        return v

    # days_name = "4-5 days per week (full-time)"
    days_name = "2-3 days per week (part-time)"
    test_df[days_name] = test_df[days_name].apply(norm)
    test_df = test_df.sort_values(by=[days_name], ascending=False)
    print(test_df[["contributor", days_name]])

    money_df = pd.melt(baseline_money_df, var_name="Time", value_name="USD/month",
                       id_vars=["continent", "employment", "contracting"])
    money_df["Time"] = money_df["Time"].apply(lambda v: {
        "4-5 days per week (full-time)": "4-5 days",
        "2-3 days per week (part-time)": "2-3 days",
        "1 day per week or less": "<= 1 day",
    }[v])
    money_df = money_df[money_df["USD/month"] != "never"].dropna()
    return report

    continent_category_order = [
        "USA & Canada",
        "Europe",
        "Asia",
        "Southern America",
        "Russia"
    ]
    report.add_custom_chart("how-much-money-do-you-want",
                            lambda: make_chart(baseline_money_q, money_df, x="Time",
                                               y="USD/month", points="all", kind="box"))

    report.add_custom_chart("how-much-money-do-you-want-per-continent", lambda: shorten_annotations(
        make_chart(baseline_money_q, money_df, x="Time",
                   y="USD/month", facet_col="continent",
                   xaxis_tickangle=45, kind="scatter",
                   category_orders=dict(continent=continent_category_order[:-2]))
    ))

    def add_ylim(fig: Figure) -> Figure:
        fig.update_layout(yaxis_range=[-2000, 22000])
        return fig

    money_df_employ = money_df[money_df["employment"] == 1]
    report.add_custom_chart("how-much-money-do-you-want-per-continent-prefers-employment",
                            lambda: shorten_annotations(
                                add_ylim(make_chart(baseline_money_q.with_title(
                                    lambda t: f"{t} (people who prefer employment)"),
                                    money_df_employ,
                                    x="Time",
                                    y="USD/month", facet_col="continent",
                                    xaxis_tickangle=45, kind="scatter",
                                    category_orders=dict(continent=continent_category_order[:-2])
                                ))
                            ))

    money_df_contract = money_df[money_df["contracting"] == 1]
    report.add_custom_chart("how-much-money-do-you-want-per-continent-prefers-contracting",
                            lambda: shorten_annotations(
                                add_ylim(make_chart(baseline_money_q.with_title(
                                    lambda t: f"{t} (people who prefer contracting)"),
                                    money_df_contract,
                                    x="Time",
                                    y="USD/month", facet_col="continent",
                                    xaxis_tickangle=45, kind="scatter",
                                    category_orders=dict(continent=continent_category_order[:-2])
                                ))
                            ))

    report.add_custom_chart("how-much-money-do-you-want-cdf",
                            lambda: make_chart(baseline_money_q, money_df, x="USD/month",
                                               color="Time", kind="cdf"))

    funding_arrangement_name = "What funding arrangement would you prefer?"
    funding_arrangement_q = db.q_simple_multi(funding_arrangement_name)
    funding_arrangement_df = db.get_answer_columns(db.get_column(funding_arrangement_name),
                                                   answer_count=5)
    funding_arrangement_df["continent"] = db.df["continent"]

    occupation_name = "What is your occupation?"
    occupation = db.get_answer_columns(db.get_column(occupation_name), answer_count=None)
    occupation = occupation.apply(
        lambda row: row.first_valid_index() if row.first_valid_index() is not None else np.nan,
        axis=1)
    funding_arrangement_df["occupation"] = occupation

    arrangement_df = pd.melt(funding_arrangement_df, var_name="Arrangement",
                             value_name="Preference", id_vars=["continent", "occupation"])

    col = "Preference (1=highest)"
    arrangement_df[col] = arrangement_df["Preference"].apply(
        lambda v: map_nan(v, lambda v: str(int(v))))

    funding_category_orders = {col: [str(v) for v in range(1, 6)]}
    report.add_custom_chart("funding-arrangement",
                            lambda: make_chart(funding_arrangement_q, arrangement_df,
                                               "Arrangement",
                                               color=col,
                                               kind="bar",
                                               labels={"count": "Count"},
                                               category_orders=funding_category_orders,
                                               xaxis_tickangle=45))

    report.add_custom_chart("funding-arrangement-by-continent",
                            lambda: shorten_annotations(
                                make_chart(funding_arrangement_q, arrangement_df,
                                           "Arrangement",
                                           color=col,
                                           kind="bar",
                                           facet_col="continent",
                                           labels={"count": "Count"},
                                           category_orders=funding_category_orders,
                                           xaxis_tickangle=45)))

    def unmatch_axes(fig: Figure) -> Figure:
        fig.update_yaxes(matches=None)
        fig.for_each_yaxis(lambda yaxis: yaxis.update(showticklabels=True))
        return fig

    arrangement_occupation_df = arrangement_df.dropna(subset="occupation")
    arrangement_occupation_df = arrangement_occupation_df[
        arrangement_occupation_df["occupation"] != "Other.4"]
    report.add_custom_chart("funding-arrangement-by-occupation",
                            lambda: shorten_annotations(
                                unmatch_axes(make_chart(funding_arrangement_q,
                                                        arrangement_occupation_df,
                                                        "Arrangement",
                                                        color=col,
                                                        kind="bar",
                                                        facet_col="occupation",
                                                        facet_col_wrap=3,
                                                        height=1000,
                                                        labels={"count": "Count"},
                                                        category_orders=funding_category_orders,
                                                        xaxis_tickangle=45))))

    contributor_list_name = "Would you potentially like to be included on a public list of contributors looking for funding?"
    report.add_bar_chart("public-contributor-list", db.q_simple_single(contributor_list_name),
                         xaxis_tickangle=45)
    report.add_wordcloud("public-contributor-list-wordcloud",
                         db.open_answers(contributor_list_name))

    work_q = db.q_simple_multi("What kind of work do you do within the Rust Project?")
    work_q = work_q.rename_answers({
        "Communication (e.g. writing blog posts, release notes, preparing for meetings or taking minutes)": "Communication"
    })
    report.add_bar_chart("what-kind-of-work-do-you-do",
                         work_q,
                         xaxis_tickangle=45,
                         bar_label_vertical=True
                         )
    report.add_wordcloud("what-kind-of-work-do-you-do-wordcloud",
                         db.open_answers(work_q.question))

    area_q = db.q_simple_multi("What parts of the Rust Project do you typically contribute to?")
    report.add_bar_chart("what-area-do-you-contribute-to",
                         area_q,
                         xaxis_tickangle=45)
    report.add_wordcloud("what-area-do-you-contribute-to-wordcloud",
                         db.open_answers(area_q.question))

    teams_q = (
        db.q_simple_single(
            "What Rust teams are you a part of?")
        .expand_answers(iterate_teams)
        .filter_answers(lambda a: a.count > 1)
        .with_title(lambda t: f"{t} (filtered teams with less than 2 responses)")
    )
    report.add_bar_chart("what-teams-are-you-a-part-of", teams_q,
                         bar_label_vertical=True,
                         xaxis_tickangle=45)

    report.add_bar_chart("what-is-your-occupation", db.q_simple_multi(occupation_name),
                         xaxis_tickangle=45)
    report.add_wordcloud("what-is-your-occupation-wordcloud", db.open_answers(occupation_name))

    if not including_secret_data:
        return report

    def normalize_company(answer: str) -> Iterable[str]:
        if "(" in answer:
            answer = answer[:answer.index("(")].strip()
        companies = [c.strip() for c in answer.split(",")]
        for c in companies:
            if not c:
                continue
            if "Rust Project" in c or c.lower() in ("rust foundation", "rust fundation"):
                c = "Rust Foundation"
            lower = c.lower()
            if lower[0].isdigit():
                continue
            if lower.startswith("futurewei"):
                lower = "futurewei"
            if lower.startswith("aws"):
                lower = "aws"
            if lower == "amazon aws" or lower == "amazon":
                lower = "aws"
            if lower == "aws":
                lower = "aws/amazon"
            yield lower[0].upper() + lower[1:]

    companies_q = (
        db.q_simple_single(
            "Which companies/organizations fund your contributions to the Rust Project?")
        .expand_answers(normalize_company)
        .combine_answers({
            "None": ["None", "No", "I do all of it in my free time."]
        })
    )
    report.add_bar_chart("companies-funding", companies_q, xaxis_tickangle=45,
                         bar_label_vertical=True)

    real_money_name = "How much money do you receive for your Rust Project contributions?"
    real_money_q = db.q_simple_single(real_money_name).integer_answers()

    # print(
    #     db.df[[real_money_name, username_name]].sort_values(by=[real_money_name], ascending=False))

    real_money_df = pd.DataFrame({
        "USD/hour": db.df[real_money_name],
        "continent": db.df["continent"],
        "start": db.df[contrib_start_name]
    }).dropna()
    report.add_custom_chart("how-much-money-do-you-receive",
                            lambda: make_chart(real_money_q, real_money_df, y="USD/hour",
                                               kind="box", points="all"))
    real_money_df_above_zero = real_money_df[real_money_df["USD/hour"] > 0]
    report.add_custom_chart("how-much-money-do-you-receive-without-volunteers",
                            lambda: make_chart(real_money_q.with_title(
                                lambda title: f"{title} (without volunteers)"),
                                real_money_df_above_zero,
                                y="USD/hour",
                                kind="box", points="all"))

    report.add_custom_chart("how-much-money-do-you-receive-cdf",
                            lambda: make_chart(real_money_q, real_money_df_above_zero, x="USD/hour",
                                               kind="cdf"))

    report.add_custom_chart("how-much-money-do-you-receive-by-continent",
                            lambda: shorten_annotations(
                                make_chart(real_money_q, real_money_df_above_zero, y="USD/hour",
                                           kind="scatter", facet_col="continent")))

    report.add_custom_chart("how-much-money-do-you-receive-by-start-of-contribution",
                            lambda: shorten_annotations(
                                make_chart(real_money_q, real_money_df_above_zero, y="USD/hour",
                                           kind="scatter", facet_col="start",
                                           category_orders=dict(
                                               start=category_order_start_contributing[:-1]))))

    return report


if __name__ == "__main__":
    random.seed(42)
    np.random.seed(42)

    report = analyze(including_secret_data=False)
    # report.charts["how-much-money-do-you-want-cdf"].render_fn().write_html("cdf.html")
    # report.charts["are-you-funded-per-team"].render_fn().write_html("funded-per-team.html")

    render_report_to_pdf(
        report,
        Path(__file__).parent / "member-survey-2026-report.pdf",
        "Rust Member survey 2026 report",
        include_labels=True
    )
