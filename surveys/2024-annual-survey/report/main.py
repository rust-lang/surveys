import random
import sys
from collections import defaultdict
from pathlib import Path
from typing import List

import numpy as np

ROOT_DIR = Path(__file__).absolute().parent.parent.parent.parent
REPORT_SCRIPT_DIR = ROOT_DIR / "report"

sys.path.insert(0, str(REPORT_SCRIPT_DIR))

from surveyhero.parser import parse_surveyhero_report, parse_surveyhero_answers
from surveyhero.render import render_blog_post, render_report_to_pdf
from surveyhero.report import ChartReport
from surveyhero.survey import Question, SurveyFullAnswers, SurveyReport, normalize_open_answers


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


def print_question_index(old: SurveyReport, new: SurveyReport, path: Path):
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


def annual_survey_2024_report() -> ChartReport:
    r_2022 = parse_surveyhero_report(Path(ROOT_DIR / "data/data-2022.csv"), year=2022)
    r_2023 = parse_surveyhero_report(Path(ROOT_DIR / "data/data-2023.csv"), year=2023)
    r_2024 = parse_surveyhero_report(Path(ROOT_DIR / "data/data-2024.csv"), year=2024)
    answers_2023 = parse_surveyhero_answers(Path(ROOT_DIR / "data/data-full-2023.csv"), year=2023)
    answers_2024 = parse_surveyhero_answers(Path(ROOT_DIR / "data/data-full-2024.csv"), year=2024)

    print_question_index(r_2023, r_2024, Path("questions.txt"))
    print_answer_index(answers_2024, r_2024, Path("answers.txt"))

    agreement_categories = ["Agree", "Disagree"]
    agreement_label = "Response"

    frequency_categories = ["More frequently than weekly", "Weekly", "Monthly or less frequently", "Never"]
    frequency_label = "Frequency"

    report = ChartReport()

    rename = {
        "Yes, I use Rust (for any purpose, even if you're just learning)": "Yes, I use Rust",
    }
    report.add_bar_chart("do-you-use-rust", r_2024.q(0).rename_answers(rename), r_2023.q(0).rename_answers(rename))

    base = r_2023.q(1).rename_answers({
        "I no longer have the opportunity to use Rust due to factors outside of my control":
            "I no longer have the opportunity to use Rust due to factors outside my control"
    })
    report.add_bar_chart("why-did-you-stop-using-rust", r_2024.q(1), base,
                         bar_label_vertical=True,
                         xaxis_tickangle=45,
                         max_tick_width=50)
    report.add_wordcloud("why-did-you-stop-using-rust-wordcloud", answers_2024.answers[10] + answers_2024.answers[11])

    base = r_2023.q(2).rename_answers({
        "I can't use Rust due to factors outside of my control":
        "I can't use Rust due to factors outside my control"
    })
    report.add_bar_chart("why-dont-you-use-rust", r_2024.q(2), base,
                         bar_label_vertical=True,
                         xaxis_tickangle=45,
                         max_tick_width=40)
    report.add_wordcloud("why-dont-you-use-rust-wordcloud", answers_2024.answers[23])

    report.add_bar_chart("how-often-do-you-use-rust", r_2024.q(3), r_2023.q(3), r_2022.q(3),
                         bar_label_vertical=True)

    expertise_diff = {
        "I can write useful, production-ready code but it is a struggle": "I can write useful, production-ready code, but it is a struggle"
    }
    report.add_bar_chart(
        "how-would-you-rate-your-rust-expertise",
        r_2024.q(4),
        r_2023.q(5).rename_answers(expertise_diff),
        r_2022.q(4).rename_answers({
            **expertise_diff,
            "I can't read or write Rust": "I can't write Rust code"
        }),
        bar_label_vertical=True,
        xaxis_tickangle=45,
        max_tick_width=40
    )
    report.add_pie_chart("when-did-you-learn-rust", r_2024.q(5))

    # Let's not use base, as the answers are too different
    _base = r_2023.q(23).rename_answers({
        "Other (please specify)": "Other",
        "Videos": "Videos or live-streams",
        "Online exercises (Rustlings, Rust by Example, etc.)": "Online exercises (Rustlings, 100 Exercises To Learn Rust, etc.)"
    })
    report.add_bar_chart("what-kind-of-learning-materials-have-you-consumed", r_2024.q(6).rename_answers({
        "Other (please specify)": "Other"
    }), xaxis_tickangle=45, bar_label_vertical=True, max_tick_width=40)
    report.add_wordcloud("what-kind-of-learning-materials-have-you-consumed-wordcloud", answers_2024.answers[37])

    report.add_bar_chart("have-you-taken-a-rust-course", r_2024.q(7), r_2023.q(22))

    windows_diff = {
        "Windows": ["Windows 10/11", "Windows 8 or older"]
    }
    report.add_bar_chart("which-os-do-you-use",
                         r_2024.q(8).combine_answers(windows_diff),
                         r_2023.q(7).combine_answers(windows_diff),
                         r_2022.q(6).rename_answers({
                             "Mac OS": "macOS"
                         }),
                         bar_label_vertical=True,
                         max_tick_width=20)
    report.add_wordcloud("which-os-do-you-use-wordcloud", answers_2024.answers[45])

    report.add_bar_chart("which-os-do-you-target",
                         r_2024.q(9).combine_answers(windows_diff),
                         r_2023.q(8).combine_answers(windows_diff),
                         bar_label_vertical=True,
                         xaxis_tickangle=45,
                         max_tick_width=50)
    report.add_wordcloud("which-os-do-you-target-wordcloud", answers_2024.answers[58])

    ide_diff = {
        "Rust Rover (dedicated IntelliJ Rust IDE)": "Rust Rover"
    }
    zed_2023 = normalize_open_answers(answers_2023.answers[83])
    zed_2024 = normalize_open_answers(answers_2024.answers[70])
    report.add_bar_chart("what-ide-do-you-use",
                         r_2024.q(10).rename_answers(ide_diff).add_open(zed_2024, "zed", "Zed"),
                         r_2023.q(12).rename_answers(ide_diff).add_open(zed_2023, "zed", "Zed"),
                         bar_label_vertical=True, xaxis_tickangle=45)
    report.add_wordcloud("what-ide-do-you-use-wordcloud", answers_2024.answers[70])

    report.add_bar_chart("which-version-of-rust-do-you-use", r_2024.q(11),
                         xaxis_tickangle=45,
                         max_tick_width=40)
    report.add_wordcloud("which-version-of-rust-do-you-use-wordcloud", answers_2024.answers[81])

    report.add_bar_chart("if-you-use-nightly-why", r_2024.q(12), xaxis_tickangle=45, max_tick_width=40)
    report.add_wordcloud("if-you-use-nightly-why-wordcloud", answers_2024.answers[93])

    report.add_pie_chart("what-is-the-oldest-version-of-rust-you-use", r_2024.q(13))

    report.add_matrix_chart(
        "what-do-you-think-about-rust-stability",
        r_2024.q(14),
        height=800,
        categories=agreement_categories,
        category_label=agreement_label,
        option_label="Statement"
    )

    report.add_bar_chart(
        "what-do-you-think-about-rust-evolution",
        r_2024.q(15),
        xaxis_tickangle=45,
    )

    categories = ["Would unblock my use-case", "Would improve my code", "Don't need it",
                  "Don't know what it is"]
    report.add_matrix_chart(
        "which-features-do-you-want-stabilized",
        r_2024.q(16),
        categories=categories,
        category_label="Response",
        horizontal=True,
        height=800,
        max_label_width=30,
        textposition="inside",
        legend_params=dict(
            orientation="h",
            y=-0.05,
        )
    )
    report.add_wordcloud("which-features-do-you-want-stabilized-wordcloud", answers_2024.answers[121])

    categories = ["Big problem for me", "Could be improved, but does not limit me", "Not an issue for me at all"]
    problems_diff = {
        "Subpar debugging experience (e.g. missing value visualizations or async stacktraces)": "Subpar debugging experience",
        "Subpar IDE support (e.g. some errors are not shown or analysis is slow)": "Subpar IDE support",
        "Encountering compiler bugs (e.g. ICEs a.k.a. internal compiler errors or miscompilations)": "Encountering compiler bugs"
    }
    report.add_matrix_chart(
        "which-problems-limit-your-productivity",
        r_2024.q(17).rename_answers(problems_diff),
        categories=categories,
        category_label="Response",
        horizontal=True,
        height=1000,
        textposition="inside",
        max_label_width=40,
        legend_params=dict(
            y=-0.05,
            orientation="h"
        )
    )
    report.add_wordcloud("which-problems-limit-your-productivity-wordcloud", answers_2024.answers[142])

    categories = [
        "I use this feature",
        "I cannot use this feature yet",
        "I do not need this feature",
        "I did not know it was stabilized",
        "I do not know what it is"
    ]
    report.add_matrix_chart(
        "which-stabilized-features-do-you-use",
        r_2024.q(18),
        categories=categories,
        category_label="Response",
        horizontal=True,
        height=1000,
        textposition="inside",
        max_label_width=40,
        legend_params=dict(
            y=-0.05,
            orientation="h"
        )
    )

    cargo_diff = {
        "I combine Cargo and another build system": [
            "I combine Cargo and another build system",
            "If you use Cargo with (or just use) other build systems, which ones do you use?"
        ]
    }
    report.add_bar_chart("how-do-you-build-your-rust-projects",
                         r_2024.q(19).combine_answers(cargo_diff),
                         r_2023.q(17).combine_answers(cargo_diff))
    report.add_wordcloud("how-do-you-build-your-rust-projects-wordcloud", answers_2024.answers[162])

    report.add_bar_chart("how-do-download-crates", r_2024.q(20), r_2023.q(18), xaxis_tickangle=45)

    question = r_2024.q(21).rename_answers({
        "Attend a Rust meetup or conference (virtual or in-person)": "Attend a Rust meetup",
        "Consume informational content about Rust (e.g., blogs, live streams, YouTube videos, etc.)": "Consume content (blogs, videos, ...)",
        "Contribute code changes (including tests) to any open-source Rust project": "Contribute code/tests to any OSS Rust project",
        "Contribute non-code changes (documentation, comments, etc.) to any open-source Rust project": "Contribute docs/comments to any OSS Rust project",
        "Discuss the Rust project in an official chat or forum (internals.rust-lang.org, Rust Zulip, etc.)": "Discuss Rust in official chat/forum",
        "Open an issue on any repo in the rust-lang GitHub organization": "Open issue on any rust-lang repo",
        "Participate in conversations about Rust on social media or websites (Hacker News, r/rust, Twitter, LinkedIn, etc.)": "Discuss Rust on social media (Hacker News, r/rust, ...)",
        "Produce informational content about Rust (e.g., blogged, live streamed, made a YouTube video, presented at a conference/meetup, etc.)": "Produce Rust content (blog, video, talk, ...)",
        "Read official Rust communication channels (e.g., This Week in Rust, the official Rust blog, the Rust Twitter account, etc.)": "Read official Rust channels (Rust blog/twitter, This Week in Rust, ...)",
        "Write, comment on, contribute to discussion of, or provide edits to an open RFC": "Comment or contribute to an open RFC"
    })
    report.add_matrix_chart(
        "how-often-do-you-engage-in-community-events",
        question,
        categories=frequency_categories,
        category_label=frequency_label,
        horizontal=True,
        textposition="inside",
        max_label_width=30,
        legend_params=dict(
            orientation="h"
        ),
        height=800
    )

    categories = [
        "I feel welcome",
        "I do not feel particularly welcome or unwelcome",
        "I feel unwelcome",
        "I've never participated in this activity"
    ]
    experience_diff = {
        "Community focused on a specific area of Rust software development (e.g. game development, audio, etc.)": "Community focused on a specific Rust area",
        "Discussions (issues, pull requests, etc.) on a repository inside the rust-lang GitHub organization": "Discussions on a rust-lang repo",
        "Discussions (issues, pull requests, etc.) on a repository outside the rust-lang GitHub organization": "Discussions on a repo outside rust-lang",
        "Official Rust community forums or chats (users.rust-lang.org, internals.rust-lang.org, the official Rust Discord, or the Rust Zulip)": "Official Rust forum/chat (URLO, IRLO, Discord, Zulip)",
        "Unofficial Rust community forums or chats (e.g., reddit.com/r/rust, Hacker News, the Rust Community Discord, etc.)": "Unofficial Rust forum/chat (r/rust, Hacker News, ...)"
    }
    report.add_matrix_chart(
        "what-was-your-experience-in-the-community",
        r_2024.q(22).rename_answers(experience_diff),
        categories=categories,
        category_label="Response",
        horizontal=True,
        textposition="inside",
        max_label_width=30,
        legend_params=dict(
            orientation="h"
        )
    )

    report.add_pie_chart("are-you-employed", r_2024.q(23))
    report.add_pie_chart("do-you-design-software", r_2024.q(24))

    report.add_bar_chart("do-you-personally-use-rust-at-work", r_2024.q(25), r_2023.q(26),
                         r_2022.q(17),
                         max_tick_width=24)
    report.add_bar_chart(
        "how-is-rust-used-at-your-organization",
        r_2024.q(26),
        r_2023.q(27),
        r_2022.q(20).rename_answers({
            "I am unsure whether my company has considered using or currently uses Rust": "I am unsure whether my organisation has considered using or currently uses Rust",
            "I don't work for a company or my company does not develop software of any kind": "I don't work for a organisation or my organisation does not develop software of any kind",
            "My company has experimented with Rust or is considering using it": "My organisation has experimented with Rust or is considering using it",
            "My company has not seriously considered Rust for any use": "My organisation has not seriously considered Rust for any use",
            "My company makes non-trivial use of Rust (e.g., used in production or in significant tooling)": "My organisation makes non-trivial use of Rust (e.g., used in production or in significant tooling)"
        }),
        xaxis_tickangle=45,
        bar_label_vertical=True
    )
    report.add_bar_chart(
        "which-statements-apply-to-rust-at-work",
        r_2024.q(27),
        r_2023.q(28),
        r_2022.q(19),
        xaxis_tickangle=45,
        bar_label_vertical=True
    )

    report.add_bar_chart(
        "why-you-use-rust-at-work",
        r_2024.q(28),
        r_2023.q(29),
        r_2022.q(18),
        xaxis_tickangle=45,
        bar_label_vertical=True
    )

    base_open = normalize_open_answers(answers_2023.answers[213], replace_spaces=True)
    technology_diff = {
        "Programming languages and related tools (including compilers, IDEs, standard libraries, etc.)": "Programming languages and related tools"
    }
    base = (
        r_2023.q(30)
        .rename_answers({
            **technology_diff,
            "Computer Games": "Computer games",
            "Scientific and/or numeric computing": "Scientific and/or numerical computing",
        })
        .add_open(base_open, "automotive", "Automotive")
    )

    report.add_bar_chart("technology-domain", r_2024.q(29).rename_answers(technology_diff), base,
                         legend_params=dict(
                             orientation="h",
                             y=1
                         ),
                         xaxis_tickangle=90,
                         bar_label_vertical=True,
                         max_tick_width=50)
    report.add_wordcloud("technology-domain-wordcloud", answers_2024.answers[235])

    report.add_pie_chart("how-many-developers-does-your-organization-employ", r_2024.q(30),
                         legend_order=[
                             "Under 10",
                             "11-49",
                             "50-99",
                             "100-500",
                             "500-1,000",
                             "1,000-10,000",
                             "Over 10,000",
                         ])

    report.add_bar_chart("is-your-organization-planning-on-hiring-rust-developers", r_2024.q(31), r_2023.q(32),
                         legend_order=[
                             "No",
                             "No (it is planning to hire other developers)",
                             "No (it is not planning to hire any developers)",
                             "Yes",
                             "I don't know",
                         ], xaxis_tickangle=45)

    categories = [
        "Agree",
        "Neither agree nor disagree",
        "Disagree"
    ]
    report.add_matrix_chart(
        "assessment-of-rust-employment-statements",
        r_2024.q(32),
        categories=categories,
        category_label="Response",
        height=800
    )

    report.add_bar_chart("which-of-the-following-statements-about-rust-do-you-agree-with", r_2024.q(33), r_2023.q(33),
                         xaxis_tickangle=45, bar_label_vertical=True, max_tick_width=45)

    worry_diff = {
        "Tools and documentation are not accessible enough (e.g., due to language or incompatibility with screen readers)": "Tools and documentation are not accessible enough",
        "Rust Foundation not supporting the Rust project properly (e.g. in financial, infrastructure, legal aspects)": "Rust Foundation not supporting the Rust project properly"
    }
    question = r_2024.q(34).rename_answers(worry_diff)
    base = r_2023.q(34).rename_answers(worry_diff)
    report.add_bar_chart("what-are-your-biggest-worries-about-rust", question, base, xaxis_tickangle=55,
                         max_tick_width=45, bar_label_vertical=True)
    report.add_wordcloud("what-are-your-biggest-worries-about-rust-wordcloud", answers_2024.answers[264])

    question = r_2024.q(35)
    report.add_pie_chart("do-you-consider-yourself-to-be-a-part-of-an-underrepresented-group", question)

    report.add_bar_chart("which-marginalized-group", r_2024.q(36), xaxis_tickangle=45)

    report.add_bar_chart("are-you-a-student", r_2024.q(37), r_2023.q(38),
                         xaxis_tickangle=45,
                         max_tick_width=40,
                         bar_label_vertical=True)
    report.add_pie_chart("how-long-have-you-been-programming", r_2024.q(38))
    report.add_pie_chart("where-do-you-live", r_2024.q(39))
    report.add_bar_chart("in-what-ways-are-you-comfortable-communicating", r_2024.q(40),
                         xaxis_tickangle=45, max_tick_width=45)
    report.add_bar_chart("what-are-your-preferred-languages-for-technical-communication", r_2024.q(41),
                         xaxis_tickangle=45)
    return report


if __name__ == "__main__":
    """
    Renders the PDF report and a blog post for the 2024 Annual survey report.
    Expects CSV data extracted from SurveyHero at <surveys-repo-root/data>.
    See `annual_survey_2024_report` for more details.
    """
    random.seed(42)
    np.random.seed(42)

    report = annual_survey_2024_report()

    resource_dir = "2025-02-13-rust-survey-2024"
    # Fill path to blog root (i.e. a checkout of https://github.com/rust-lang/blog.rust-lang.org)
    blog_root = Path("/projects/personal/rust/blog.rust-lang.org")
    # relative path in this repository where the survey Markdown template is
    template_path = Path("surveys/2024-annual-survey/report/2025-02-13-2024-State-Of-Rust-Survey-results.md")
    render_blog_post(
        template=template_path,
        blog_root=blog_root,
        resource_dir=resource_dir,
        report=report
    )

    if len(sys.argv) == 2 and sys.argv[1] == "--skip-pdf":
        sys.exit(0)

    render_report_to_pdf(
        report,
        Path(__file__).parent / "annual-survey-2024-report.pdf",
        "Rust Annual survey 2024 report",
        include_labels=False
    )
