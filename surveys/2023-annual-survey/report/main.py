import dataclasses
import random
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT_DIR = Path(__file__).absolute().parent.parent.parent.parent
REPORT_SCRIPT_DIR = ROOT_DIR / "report"

sys.path.insert(0, str(REPORT_SCRIPT_DIR))

from surveyhero.parser import parse_surveyhero_report, parse_surveyhero_answers
from surveyhero.render import render_blog_post, render_report_to_pdf
from surveyhero.report import ChartReport
from surveyhero.survey import Question, normalize_open_answers


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


def annual_survey_2023_report() -> ChartReport:
    r_2022 = parse_surveyhero_report(Path(ROOT_DIR / "data/data-2022.csv"), year=2022)
    answers_2022 = parse_surveyhero_answers(Path(ROOT_DIR / "data/data-full-2022.csv"), 2022)
    r_2023 = parse_surveyhero_report(Path(ROOT_DIR / "data/data-2023.csv"), year=2023)
    answers_2023 = parse_surveyhero_answers(Path(ROOT_DIR / "data/data-full-2023.csv"), 2023)

    priority_categories = ["High Priority", "Medium Priority", "Low Priority", "Should not be prioritised"]
    priority_label = "Priority"

    agreement_categories = ["Agree", "Disagree"]
    agreement_label = "Statement"

    agreement2_categories = ["Agree", "Neither agree nor disagree", "Disagree"]

    frequency_categories = ["More frequently than weekly", "Weekly", "Monthly or less frequently", "Never"]
    frequency_label = "Frequency"

    welcoming_categories = ["I feel welcome", "I do not feel particularly welcome or unwelcome", "I feel unwelcome",
                            "I've never participated in this activity"]
    welcoming_label = "Answer"

    report = ChartReport()

    rename = {
        "Yes, I use Rust (for any purpose, even if you're just learning)": "Yes, I use Rust",
    }
    report.add_bar_chart("do-you-use-rust", r_2023.q(0).rename_answers(rename), r_2022.q(0).rename_answers(rename))

    base = r_2022.q(1)
    base = base.rename_answers({
        "Rust did not help me achieve my goals": None
    })
    report.add_bar_chart("why-did-you-stop-using-rust", r_2023.q(1), base,
                         bar_label_vertical=True,
                         xaxis_tickangle=45,
                         max_tick_width=50)
    report.add_wordcloud("why-did-you-stop-using-rust-wordcloud", answers_2023.answers[11])

    report.add_bar_chart("why-dont-you-use-rust", r_2023.q(2), r_2022.q(2).rename_answers({
        "I have not got round to it": "I haven't got around to it",
        "Missing Libraries": "Missing libraries"
    }), bar_label_vertical=True, xaxis_tickangle=45, max_tick_width=40)
    report.add_wordcloud("why-dont-you-use-rust-wordcloud", answers_2023.answers[23])

    report.add_bar_chart("how-often-do-you-use-rust", r_2023.q(3), r_2022.q(3), )
    report.add_pie_chart("how-often-do-you-code", r_2023.q(4), legend_params=dict(
        orientation="h"
    ))
    report.add_bar_chart("how-would-you-rate-your-rust-expertise", r_2023.q(5), r_2022.q(4).rename_answers({
        "I can't read or write Rust": "I can't write Rust code"
    }), xaxis_tickangle=45, max_tick_width=40)
    report.add_pie_chart("when-did-you-learn-rust", r_2023.q(6))

    report.add_bar_chart("which-os-do-you-use", r_2023.q(7).combine_answers({
        "Windows": ["Windows 10/11", "Windows 8 or older"]
    }), r_2022.q(6).rename_answers({
        "Mac OS": "macOS"
    }), max_tick_width=20)
    report.add_wordcloud("which-os-do-you-use-wordcloud", answers_2023.answers[35])

    report.add_bar_chart("which-os-do-you-target", r_2023.q(8).combine_answers({
        "Windows": ["Windows 10/11", "Windows 8 or older"]
    }), r_2022.q(7).rename_answers({
        "Mac OS": "macOS"
    }), bar_label_vertical=True, xaxis_tickangle=45, max_tick_width=50)
    report.add_wordcloud("which-os-do-you-target-wordcloud", answers_2023.answers[47])

    report.add_bar_chart("which-version-of-rust-do-you-use", r_2023.q(9), xaxis_tickangle=45, max_tick_width=40)
    report.add_wordcloud("which-version-of-rust-do-you-use-wordcloud", answers_2023.answers[58])

    report.add_bar_chart("if-you-use-nightly-why", r_2023.q(10), xaxis_tickangle=45, max_tick_width=40)
    report.add_wordcloud("if-you-use-nightly-why-wordcloud", answers_2023.answers[70])

    report.add_pie_chart("what-is-the-oldest-version-of-rust-you-use", r_2023.q(11))

    base_open = normalize_open_answers(answers_2022.answers[82])
    base = r_2022.q(11).rename_answers({
        "Emacs": "Emacs (or derivatives like Doom Emacs, Spacemacs, etc.)",
        "IntelliJ/CLion/other JetBrains IDE": "IntelliJ/CLion/other JetBrains IDE + Rust plugin"
    }).add_open(base_open, "helix", "Helix")

    report.add_bar_chart("what-ide-do-you-use", r_2023.q(12), base,
                         bar_label_vertical=True, xaxis_tickangle=45)
    report.add_wordcloud("what-ide-do-you-use-wordcloud", answers_2023.answers[83])

    question = r_2023.q(13).rename_answers({
        "Memory usage (i.e., how much RAM rustc uses when compiling)": "Memory usage",
        "Disk space usage (e.g., the size of target folder)": "Disk space usage",
        "Bugs in the compiler (i.e., ICEs a.k.a. internal compiler errors, miscompilations, etc.)": "Compiler bugs",
        "Documentation (rustdoc, docs.rs)": "Documentation tools",
        "Package management (crates.io)": "Package management",
        "Rust language and standard library documentation": "Language, stdlib docs"
    })
    report.add_matrix_chart(
        "how-should-work-be-prioritized",
        question,
        categories=priority_categories,
        category_label=priority_label,
        horizontal=True,
        height=800,
        legend_params=dict(
            y=-0.1,
            orientation="h"
        )
    )

    report.add_pie_chart("do-you-think-that-new-features-should-be-implemented", r_2023.q(14))

    question = r_2023.q(15).rename_answers({
        "Compile time reflection (variadic generics)": "Compile time reflection",
        "Improved traits (trait alias, implied bounds, associated type defaults)": "Improved traits",
        "Improved const (generic const expressions, const expr for custom types, const trait methods)": "Improved const",
    })
    report.add_matrix_chart(
        "which-features-do-you-want-stabilized",
        question,
        categories=priority_categories,
        category_label=priority_label,
        horizontal=True,
        legend_params=dict(
            orientation="h"
        )
    )
    report.add_wordcloud("which-features-do-you-want-stabilized-wordcloud", answers_2023.answers[113])

    report.add_bar_chart("which-problems-do-you-remember-encountering", r_2023.q(16).rename_answers({
        "Other (please specify)": "Other"
    }), xaxis_tickangle=45)
    report.add_wordcloud("which-problems-do-you-remember-encountering-wordcloud", answers_2023.answers[124])

    report.add_bar_chart("how-do-you-build-your-rust-projects", r_2023.q(17).combine_answers({
        "I combine Cargo and another build system": [
            "I combine Cargo and another build system",
            "If you use Cargo with (or just use) other build systems, which ones do you use?"
        ]
    }))
    report.add_wordcloud("how-do-you-build-your-rust-projects-wordcloud", answers_2023.answers[129])

    report.add_bar_chart("how-do-download-crates", r_2023.q(18), xaxis_tickangle=45)

    report.add_matrix_chart(
        "what-do-you-think-about-rust-stability",
        r_2023.q(19),
        categories=agreement_categories,
        category_label=agreement_label
    )

    question = r_2023.q(20).rename_answers({
        "Attend a Rust meetup or conference (virtual or in-person)": "Attend a Rust meetup",
        "Consume informational content about Rust (e.g., blogs, live streams, YouTube videos, etc.)": "Consume content (blogs, videos, ...)",
        "Contribute code changes (including tests) to any project in the rust-lang GitHub organization": "Contribute code/tests to any rust-lang repo",
        "Contribute non-code changes (documentation, comments, etc.) to any project in the rust-lang GitHub organization": "Contribute docs/comments to any rust-lang repo",
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
        legend_params=dict(
            orientation="h"
        ),
        height=800
    )

    question = r_2023.q(21).rename_answers({
        "Community focused on a specific area of Rust software development (e.g. game development, audio, etc.)": "Community focused on a specific Rust area",
        "Discussions (issues, pull requests, etc.) on a repository inside the rust-lang GitHub organization": "Discussions on a rust-lang repo",
        "Discussions (issues, pull requests, etc.) on a repository outside of the rust-lang GitHub organization": "Discussions on a repo outside rust-lang",
        "Official Rust community forums or chats (users.rust-lang.org, internals.rust-lang.org, the official Rust Discord, or the Rust Zulip)": "Official Rust forum/chat (URLO, IRLO, Discord, Zulip)",
        "Unofficial Rust community forums or chats (e.g., reddit.com/r/rust, Hacker News, the Rust Community Discord, etc.)": "Unofficial Rust forum/chat (r/rust, Hacker News, ...)"
    })
    report.add_matrix_chart(
        "what-was-your-experience-in-the-community",
        question,
        categories=welcoming_categories,
        category_label=welcoming_label,
        horizontal=True,
        legend_params=dict(
            orientation="h"
        )
    )

    report.add_pie_chart("have-you-taken-a-rust-course", r_2023.q(22), )

    report.add_bar_chart("what-kind-of-learning-materials-have-you-consumed", r_2023.q(23).rename_answers({
        "Other (please specify)": "Other"
    }), xaxis_tickangle=45)
    report.add_wordcloud("what-kind-of-learning-materials-have-you-consumed-wordcloud", answers_2023.answers[165])

    report.add_pie_chart("are-you-employed", r_2023.q(24))
    report.add_pie_chart("do-you-design-software", r_2023.q(25))

    report.add_bar_chart("do-you-personally-use-rust-at-work", r_2023.q(26), r_2022.q(17))
    report.add_bar_chart("how-is-rust-used-at-your-organization", r_2023.q(27), r_2022.q(20).rename_answers({
        "I am unsure whether my company has considered using or currently uses Rust": "I am unsure whether my organisation has considered using or currently uses Rust",
        "I don't work for a company or my company does not develop software of any kind": "I don't work for a organisation or my organisation does not develop software of any kind",
        "My company has experimented with Rust or is considering using it": "My organisation has experimented with Rust or is considering using it",
        "My company has not seriously considered Rust for any use": "My organisation has not seriously considered Rust for any use",
        "My company makes non-trivial use of Rust (e.g., used in production or in significant tooling)": "My organisation makes non-trivial use of Rust (e.g., used in production or in significant tooling)"
    }), xaxis_tickangle=45)
    report.add_bar_chart("which-statements-apply-to-rust-at-work", r_2023.q(28), r_2022.q(19), xaxis_tickangle=45)

    # Analysis: embedded boost?
    report.add_bar_chart("why-you-use-rust-at-work", r_2023.q(29), r_2022.q(18), xaxis_tickangle=45,
                         bar_label_vertical=True)

    base_open = normalize_open_answers(answers_2022.answers[149], replace_spaces=True)
    diff = {
        "Programming languages and related tools (including compilers, IDEs, standard libraries, etc.)": "Programming languages and related tools",
        "Desktop computer or mobile phone libraries or services": "Desktop or mobile libraries or services"
    }
    base = (
        r_2022.q(23)
        .add_open(base_open, "game-development", "Computer Games")
        .add_open(base_open, "video-games", "Computer Games")
        .add_open(base_open, "database", "Database implementation")
        .rename_answers(diff)
    )

    # Note: computer games were open before
    report.add_bar_chart("technology-domain", r_2023.q(30).rename_answers(diff), base, xaxis_tickangle=-90,
                         bar_label_vertical=True, max_tick_width=50)
    report.add_wordcloud("technology-domain-wordcloud", answers_2023.answers[213])

    report.add_pie_chart("how-many-developers-does-your-organization-employ", r_2023.q(31),
                         legend_order=[
                             "Under 10",
                             "11-49",
                             "50-99",
                             "100-500",
                             "500-1,000",
                             "1,000-10,000",
                             "Over 10,000",
                         ])

    # TODO: merge bars
    report.add_bar_chart("is-your-organization-planning-on-hiring-rust-developers", r_2023.q(32), r_2022.q(22),
                         legend_order=[
                             "No",
                             "No (it is planning to hire other developers)",
                             "No (it is not planning to hire any developers)",
                             "Yes",
                             "I don't know",
                         ], xaxis_tickangle=45)

    report.add_bar_chart("which-of-the-following-statements-about-rust-do-you-agree-with", r_2023.q(33), r_2022.q(24),
                         xaxis_tickangle=45, bar_label_vertical=True, max_tick_width=45)

    question = r_2023.q(34).rename_answers({
        "Tools and documentation are not accessible enough (e.g., due to language or incompatibility with screen readers)": "Tools and documentation are not accessible enough",
        "Rust Foundation not supporting the Rust project properly (e.g. in financial, infrastructure, legal aspects)": "Rust Foundation not supporting the Rust project properly"
    })
    # base = r_2022.q(25)
    # The closed answer set is too different this year to provide a meaningful comparison
    report.add_bar_chart("what-are-your-biggest-worries-about-rust", question, xaxis_tickangle=55,
                         max_tick_width=45)
    report.add_wordcloud("what-are-your-biggest-worries-about-rust-wordcloud", answers_2023.answers[238])

    report.add_matrix_chart(
        "assessment-of-rust-employment-statements",
        r_2023.q(35),
        categories=agreement2_categories,
        category_label=agreement_label
    )

    question = dataclasses.replace(
        r_2023.q(36),
        question="Do you consider yourself a member of a group that is underrepresented or marginalized in technology?"
    )
    report.add_pie_chart("do-you-consider-yourself-to-be-a-part-of-an-underrepresented-group", question)
    report.add_bar_chart("which-marginalized-group", r_2023.q(37), xaxis_tickangle=45)
    report.add_bar_chart("are-you-a-student", r_2023.q(38), r_2022.q(31), xaxis_tickangle=45,
                         bar_label_vertical=True)
    report.add_pie_chart("how-long-have-you-been-programming", r_2023.q(39))
    report.add_pie_chart("where-do-you-live", r_2023.q(40))
    report.add_bar_chart("in-what-ways-are-you-comfortable-communicating", r_2023.q(41),
                         xaxis_tickangle=45, max_tick_width=45)
    report.add_bar_chart("what-are-your-preferred-languages-for-technical-communication", r_2023.q(42),
                         xaxis_tickangle=45)

    # report.add_wordcloud("any-other-comments-wordcloud", answers_2023.answers[250])
    return report


if __name__ == "__main__":
    """
    Renders the PDF report and a blog post for the 2023 Annual survey report.
    Expects CSV data extracted from SurveyHero at <surveys-repo-root/data>.
    See `annual_survey_2023_report` for more details.
    """
    random.seed(42)
    np.random.seed(42)

    report = annual_survey_2023_report()

    render_report_to_pdf(
        report,
        Path(__file__).parent / "annual-survey-2023-report.pdf",
        "Rust Annual survey 2023 report",
        include_labels=False
    )

    resource_dir = "2024-02-rust-survey-2023"
    # Fill path to blog roost
    blog_root = Path("")
    render_blog_post(
        template=Path("2024-02-26-2023-Rust-Annual-Survey-2023-results.md"),
        blog_root=blog_root,
        resource_dir=resource_dir,
        report=report
    )
