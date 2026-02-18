import random
import sys
from collections import defaultdict
from pathlib import Path
from typing import List

import numpy as np

ROOT_DIR = Path(__file__).absolute().parent.parent.parent.parent.parent
REPORT_SCRIPT_DIR = ROOT_DIR / "report"

sys.path.insert(0, str(REPORT_SCRIPT_DIR))

from surveyhero.parser import parse_surveyhero_summary, parse_surveyhero_answers
from surveyhero.render import render_blog_post, render_report_to_pdf
from surveyhero.report import ChartReport
from surveyhero.survey import Question, SurveyFullAnswers, SurveySummary, normalize_open_answers
from surveyhero.utils import print_question_index, print_answer_index, inspect_open_answers


def annual_survey_2025_report() -> ChartReport:
    summary_2022 = parse_surveyhero_summary(Path(ROOT_DIR / "data/data-2022.csv"), year=2022)
    summary_2023 = parse_surveyhero_summary(Path(ROOT_DIR / "data/data-2023.csv"), year=2023)
    summary_2024 = parse_surveyhero_summary(Path(ROOT_DIR / "data/data-2024.csv"), year=2024)
    summary = parse_surveyhero_summary(Path(ROOT_DIR / "data/data-2025.csv"), year=2025)
    db_2022 = parse_surveyhero_answers(
        Path(ROOT_DIR / "data/data-full-2022.csv"),
        year=2022,
        summary=summary_2022,
    )
    db_2023 = parse_surveyhero_answers(
        Path(ROOT_DIR / "data/data-full-2023.csv"),
        year=2023,
        summary=summary_2023,
    )
    db_2024 = parse_surveyhero_answers(
        Path(ROOT_DIR / "data/data-full-2024.csv"),
        year=2024,
        summary=summary_2024
    )
    db = parse_surveyhero_answers(
        Path(ROOT_DIR / "data/data-full-2025.csv"),
        year=2025,
        summary=summary
    )

    print_question_index(Path("questions.txt"), summary, old=summary_2024)
    print_answer_index(db, summary, Path("answers.txt"))

    agreement_categories = ["Agree", "Disagree"]
    agreement_label = "Response"

    frequency_categories = ["More frequently than weekly", "Weekly", "Monthly or less frequently",
                            "Never"]
    frequency_label = "Frequency"

    report = ChartReport()

    do_you_use_rust_q = "Do you use Rust?"

    rename = {
        "Yes, I use Rust (for any purpose, even if you're just learning)": "Yes, I use Rust",
    }
    report.add_bar_chart("do-you-use-rust",
                         db.q_simple_single(do_you_use_rust_q).rename_answers(rename),
                         db_2023.q_simple_single(do_you_use_rust_q).rename_answers(rename),
                         db_2024.q_simple_single(do_you_use_rust_q).rename_answers(rename),
                         )

    stopped_using_rust_q = "As you have indicated that you're not currently using Rust, why not?"
    report.add_bar_chart("why-did-you-stop-using-rust", db.q_simple_multi(stopped_using_rust_q),
                         db_2024.q_simple_multi(stopped_using_rust_q),
                         bar_label_vertical=True,
                         xaxis_tickangle=45,
                         max_tick_width=50)
    report.add_wordcloud("why-did-you-stop-using-rust-wordcloud",
                         db.open_answers(stopped_using_rust_q) + db.open_answers_raw(11))

    why_dont_you_use_rust_q = "Why don't you use Rust?"
    report.add_bar_chart("why-dont-you-use-rust", db.q_simple_multi(why_dont_you_use_rust_q),
                         db_2024.q_simple_multi(why_dont_you_use_rust_q),
                         bar_label_vertical=True,
                         xaxis_tickangle=45,
                         max_tick_width=40)
    report.add_wordcloud("why-dont-you-use-rust-wordcloud",
                         db.open_answers(why_dont_you_use_rust_q))

    how_often_you_use_rust_q = "On average, how often do you use Rust?"
    report.add_bar_chart("how-often-do-you-use-rust", db.q_simple_single(how_often_you_use_rust_q),
                         db_2022.q_simple_single(how_often_you_use_rust_q),
                         db_2023.q_simple_single(how_often_you_use_rust_q),
                         db_2024.q_simple_single(how_often_you_use_rust_q),
                         bar_label_vertical=True)

    expertise_q = "How would you rate your Rust expertise?"
    expertise_diff = {
        "I can write useful, production-ready code but it is a struggle": "I can write useful, production-ready code, but it is a struggle"
    }
    report.add_bar_chart(
        "how-would-you-rate-your-rust-expertise",
        db.q_simple_single(expertise_q),
        db_2022.q_simple_single(expertise_q).rename_answers({
            **expertise_diff,
            "I can't read or write Rust": "I can't write Rust code"
        }),
        db_2023.q_simple_single(expertise_q).rename_answers(expertise_diff),
        db_2024.q_simple_single(expertise_q),
        bar_label_vertical=True,
        xaxis_tickangle=45,
        max_tick_width=40
    )
    report.add_pie_chart("when-did-you-learn-rust",
                         db.q_simple_single("When did you learn to program in Rust?"))

    materials_q = "If you consumed learning material about Rust, which kind of material did you consume?"
    report.add_bar_chart("what-kind-of-learning-materials-have-you-consumed",
                         db.q_simple_multi(materials_q),
                         db_2024.q_simple_multi(materials_q),
                         xaxis_tickangle=45, bar_label_vertical=True, max_tick_width=40)
    report.add_wordcloud("what-kind-of-learning-materials-have-you-consumed-wordcloud",
                         db.open_answers(materials_q))

    course_q = "Are you currently taking a course that uses or teaches Rust OR have you taken a course of this type in the last year?"
    report.add_bar_chart("have-you-taken-a-rust-course", db.q_simple_single(course_q),
                         db_2023.q_simple_single(course_q),
                         db_2024.q_simple_single(course_q)
                         )

    os_usage_q = "Which operating systems do you use regularly for Rust development?"
    windows_diff = {
        "Windows": ["Windows 10/11", "Windows 8 or older"]
    }
    windows_diff2 = {
        "Windows": ["Windows 10/11", "Windows 8.1 or older"]
    }
    report.add_bar_chart("which-os-do-you-use",
                         db.q_simple_multi(os_usage_q).combine_answers(windows_diff2),
                         db_2022.q_simple_multi(os_usage_q).rename_answers({
                             "Mac OS": "macOS"
                         }),
                         db_2023.q_simple_multi(os_usage_q).combine_answers(windows_diff),
                         db_2024.q_simple_multi(os_usage_q).combine_answers(windows_diff),
                         bar_label_vertical=True,
                         max_tick_width=20)
    report.add_wordcloud("which-os-do-you-use-wordcloud", db.open_answers(os_usage_q))

    os_target_q = "Which operating systems or runtimes do you develop Rust software for?"
    report.add_bar_chart("which-os-do-you-target",
                         db.q_simple_multi(os_target_q).combine_answers(windows_diff2),
                         db_2024.q_simple_multi(os_target_q).combine_answers(windows_diff),
                         bar_label_vertical=True,
                         xaxis_tickangle=45,
                         max_tick_width=50)
    report.add_wordcloud("which-os-do-you-target-wordcloud", db.open_answers(os_target_q))

    ide_q = "Which editor or IDE setup do you use with Rust code on a regular basis?"
    ide_diff = {
        "Rust Rover (dedicated IntelliJ Rust IDE)": "Rust Rover"
    }
    ide_open_2023 = normalize_open_answers(db_2023.open_answers(ide_q))
    ide_open_2024 = normalize_open_answers(db_2024.open_answers(ide_q))
    ide_open_2025 = normalize_open_answers(db.open_answers(ide_q))
    report.add_bar_chart("what-ide-do-you-use",
                         db.q_simple_multi(ide_q).rename_answers(ide_diff)
                         .add_open(ide_open_2025, "zed", "Zed")
                         .add_open(ide_open_2025, "cursor", "Cursor"),
                         db_2023.q_simple_multi(ide_q).rename_answers(ide_diff).add_open(
                             ide_open_2023,
                             "zed",
                             "Zed"
                         ),
                         db_2024.q_simple_multi(ide_q).rename_answers(ide_diff).add_open(
                             ide_open_2024,
                             "zed",
                             "Zed"),
                         bar_label_vertical=True, xaxis_tickangle=45)
    report.add_wordcloud("what-ide-do-you-use-wordcloud", ide_open_2025)

    rust_version_q = "Which version(s) of Rust do you use for development?"
    report.add_bar_chart("which-version-of-rust-do-you-use",
                         db.q_simple_multi(rust_version_q),
                         xaxis_tickangle=45,
                         max_tick_width=40)
    report.add_wordcloud("which-version-of-rust-do-you-use-wordcloud",
                         db.open_answers(rust_version_q))

    use_nightly_q = "If you use nightly, why?"
    report.add_bar_chart("if-you-use-nightly-why", db.q_simple_multi(use_nightly_q),
                         xaxis_tickangle=45,
                         max_tick_width=40)
    report.add_wordcloud("if-you-use-nightly-why-wordcloud", db.open_answers(use_nightly_q))

    # TODO: fix SurveyHero export bug
    report.add_pie_chart("what-is-the-oldest-version-of-rust-you-use", db.q_simple_single(
        "What is the oldest version of Rust you use for any development task?"))

    stability_q = "Do you agree with the following statements on Rust stability?"
    report.add_matrix_chart(
        "what-do-you-think-about-rust-stability",
        summary.q_by_text(stability_q),
        height=800,
        categories=agreement_categories,
        category_label=agreement_label,
        option_label="Statement"
    )

    evolution_q = "What is your opinion on how fast Rust evolves?"
    report.add_bar_chart(
        "what-do-you-think-about-rust-evolution",
        db.q_simple_single(evolution_q),
        db_2024.q_simple_single(evolution_q),
        xaxis_tickangle=45,
    )

    features_q = "Which unimplemented (or nightly only) features are you looking for to be stabilized?"
    categories = ["Would unblock my use-case", "Would improve my code", "Don't need it",
                  "Don't know what it is"]
    report.add_matrix_chart(
        "which-features-do-you-want-stabilized",
        summary.q_by_text(features_q).rename_answers(
            {
                "Declarative (macro_rules!) attributes (#[attr]) and derives (#[derive(Trait)])":
                    "Declarative attribute and derive macros"
            }
        ),
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
    report.add_wordcloud("which-features-do-you-want-stabilized-wordcloud",
                         db.open_answers(
                             "Are there any features not mentioned above that you would like to be prioritized?"))

    productivity_q = "Which of the following aspects of Rust present non-trivial problems to your programming productivity?"
    categories = ["Big problem for me", "Could be improved, but does not limit me",
                  "Not an issue for me at all"]
    problems_diff = {
        "Subpar debugging experience (e.g. missing value visualizations or async stacktraces)": "Subpar debugging experience",
        "Subpar IDE support (e.g. some errors are not shown or analysis is slow)": "Subpar IDE support",
        "Encountering compiler bugs (e.g. ICEs a.k.a. internal compiler errors or miscompilations)": "Encountering compiler bugs"
    }
    report.add_matrix_chart(
        "which-problems-limit-your-productivity",
        summary.q_by_text(productivity_q).rename_answers(problems_diff),
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
    report.add_wordcloud("which-problems-limit-your-productivity-wordcloud",
                         db.open_answers(
                             "Are there any challenges not mentioned above that affect your Rust programming productivity?"))

    categories = [
        "I use it or plan to use it",
        "I cannot use this feature yet",
        "I do not need this feature",
        "I did not know it was stabilized",
        "I do not know what it is"
    ]
    report.add_matrix_chart(
        "which-stabilized-features-do-you-use",
        summary.q_by_text("Which features stabilized in the past 12 months do you use the most?"),
        categories=categories,
        category_label="Response",
        horizontal=False,
        height=800,
        textposition="inside",
        max_label_width=40,
        legend_params=dict(
            y=-0.2,
            orientation="h"
        )
    )

    build_system_q = "How do you build your Rust projects?"
    cargo_diff = {
        "I combine Cargo and another build system": [
            "I combine Cargo and another build system",
            "If you use Cargo with (or just use) other build systems, which ones do you use?"
        ]
    }
    report.add_bar_chart("how-do-you-build-your-rust-projects",
                         db.q_simple_multi(build_system_q, answer_count=4).combine_answers(
                             cargo_diff),
                         db_2024.q_simple_multi(build_system_q, answer_count=4).combine_answers(
                             cargo_diff))
    report.add_wordcloud("how-do-you-build-your-rust-projects-wordcloud",
                         db.open_answers(
                             "If you use Cargo with (or just use) other build systems, which ones do you use?"))

    download_q = "From where do you download crates to build Rust projects?"
    report.add_bar_chart("how-do-you-download-crates", db.q_simple_multi(download_q),
                         db_2024.q_simple_multi(
                             "How do you download crates to build Rust projects?")
                         .rename_answers({
                             "I use crates.io": "crates.io",
                             "I use a mirror of crates.io": "Mirror of crates.io",
                             "I use a custom/local/company registry": "Custom/local/company registry"
                         }),
                         xaxis_tickangle=45,
                         bar_label_vertical=True)
    report.add_wordcloud("how-do-you-download-crates-wordcloud", db.open_answers(download_q))

    error_codes_q = "Do you make use of compiler error codes?"
    report.add_bar_chart("do-you-use-compiler-error-codes", db.q_simple_single(error_codes_q),
                         xaxis_tickangle=45,
                         bar_label_vertical=True)
    report.add_wordcloud("do-you-use-compiler-error-codes-wordcloud",
                         db.open_answers(error_codes_q))

    community_event_q = "Roughly how often do you engage in the following Rust community activities?"
    question = summary.q_by_text(community_event_q).rename_answers({
        "Attend a Rust meetup or conference (virtual or in-person)": "Attend a Rust meetup",
        "Consume informational content about Rust (e.g., blogs, live streams, YouTube videos, etc.)": "Consume content (blogs, videos, ...)",
        "Contribute code changes (including tests) to any open-source Rust project": "Contribute code/tests to any OSS Rust project",
        "Contribute non-code changes (documentation, comments, etc.) to any open-source Rust project": "Contribute docs/comments to any OSS Rust project",
        "Discuss the Rust project in an official chat or forum (internals.rust-lang.org, Rust Zulip, etc.)": "Discuss Rust in official chat/forum",
        "Open an issue on any repo in the rust-lang GitHub organization": "Open issue on any rust-lang repo",
        "Participate in conversations about Rust on social media or websites (Hacker News, r/rust, Twitter, LinkedIn, etc.)": "Discuss Rust on social media (Hacker News, r/rust, ...)",
        "Produce informational content about Rust (e.g., blogged, live streamed, made a YouTube video, presented at a conference/meetup, etc.)": "Produce Rust content (blog, video, talk, ...)",
        "Read official Rust communication channels (e.g., This Week in Rust, the official Rust blog, the Rust Bluesky account, etc.)": "Read official Rust channels (Rust blog/Bluesky, This Week in Rust, ...)",
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

    community_welcome_q = "What has your experience been like in the following Rust community spaces?"
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
        summary.q_by_text(community_welcome_q).rename_answers(experience_diff),
        categories=categories,
        category_label="Response",
        horizontal=True,
        textposition="inside",
        max_label_width=30,
        legend_params=dict(
            orientation="h"
        )
    )

    report.add_pie_chart("are-you-employed", db.q_simple_single(
        "Are you employed full- or part-time (including paid internships)?"))
    report.add_pie_chart("do-you-design-software",
                         db.q_simple_single("Do you write or design software in your work?"))

    rust_at_work_q = "Are you personally using Rust at work?"
    report.add_bar_chart("do-you-personally-use-rust-at-work", db.q_simple_single(rust_at_work_q),
                         db_2023.q_simple_single(rust_at_work_q),
                         db_2024.q_simple_single(rust_at_work_q),
                         max_tick_width=24)
    rust_organization_q = "To what extent is Rust currently being used by your organisation?"
    report.add_bar_chart(
        "how-is-rust-used-at-your-organization",
        db.q_simple_single(rust_organization_q),
        db_2023.q_simple_single(rust_organization_q),
        db_2024.q_simple_single(rust_organization_q),
        xaxis_tickangle=45,
        bar_label_vertical=True
    )

    rust_statements_q = "Which of the following statements apply to your experience using Rust at work?"
    report.add_bar_chart(
        "which-statements-apply-to-rust-at-work",
        db.q_simple_multi(rust_statements_q),
        db_2022.q_simple_multi(rust_statements_q),
        db_2023.q_simple_multi(rust_statements_q),
        db_2024.q_simple_multi(rust_statements_q),
        xaxis_tickangle=45,
        bar_label_vertical=True
    )

    why_use_rust_at_work_q = "Which of the following statements are reasons why you use Rust at work?"
    report.add_bar_chart(
        "why-you-use-rust-at-work",
        db.q_simple_multi(why_use_rust_at_work_q),
        db_2022.q_simple_multi(why_use_rust_at_work_q),
        db_2023.q_simple_multi(why_use_rust_at_work_q),
        db_2024.q_simple_multi(why_use_rust_at_work_q),
        xaxis_tickangle=45,
        bar_label_vertical=True
    )

    domain_q = "In what technology domain(s) is Rust used at your organisation?"
    technology_diff = {
        "Programming languages and related tools (including compilers, IDEs, standard libraries, etc.)": "Programming languages and related tools"
    }
    report.add_bar_chart("technology-domain",
                         db.q_simple_multi(domain_q).rename_answers(technology_diff),
                         db_2024.q_simple_multi(domain_q).rename_answers(technology_diff),
                         legend_params=dict(
                             orientation="h",
                             y=1
                         ),
                         xaxis_tickangle=90,
                         bar_label_vertical=True,
                         max_tick_width=50)
    report.add_wordcloud("technology-domain-wordcloud", db.open_answers(domain_q))

    report.add_pie_chart("how-many-developers-does-your-organization-employ", db.q_simple_single(
        "Approximately how many total developers does your organisation employ?"),
                         legend_order=[
                             "Under 10",
                             "11-49",
                             "50-99",
                             "100-500",
                             "500-1,000",
                             "1,000-10,000",
                             "Over 10,000",
                         ])

    hiring_q = "Is your organisation planning on hiring Rust developers in the next year?"
    report.add_bar_chart("is-your-organization-planning-on-hiring-rust-developers",
                         db.q_simple_single(hiring_q),
                         db_2023.q_simple_single(hiring_q),
                         db_2024.q_simple_single(hiring_q),
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
        summary.q_by_text(
            "Please share your assessment of the following statements on Rust employment"),
        categories=categories,
        category_label="Response",
        height=800
    )

    rust_statements_q = "Which of the following statements about Rust do you feel are true?"
    report.add_bar_chart("which-of-the-following-statements-about-rust-do-you-agree-with",
                         db.q_simple_multi(rust_statements_q),
                         db_2023.q_simple_multi(rust_statements_q),
                         db_2024.q_simple_multi(rust_statements_q),
                         xaxis_tickangle=45, bar_label_vertical=True, max_tick_width=45)

    worries_q = "What are your biggest worries for the future of Rust?"
    worry_diff = {
        "Tools and documentation are not accessible enough (e.g., due to language or incompatibility with screen readers)": "Tools and documentation are not accessible enough",
        "Rust Foundation not supporting the Rust project properly (e.g. in financial, infrastructure, legal aspects)": "Rust Foundation not supporting the Rust project properly"
    }
    report.add_bar_chart("what-are-your-biggest-worries-about-rust",
                         db.q_simple_multi(worries_q).rename_answers(worry_diff),
                         db_2023.q_simple_multi(worries_q).rename_answers(worry_diff),
                         db_2024.q_simple_multi(worries_q).rename_answers(worry_diff),
                         xaxis_tickangle=55,
                         max_tick_width=45, bar_label_vertical=True)
    report.add_wordcloud("what-are-your-biggest-worries-about-rust-wordcloud",
                         db.open_answers(worries_q))

    marginal_q = summary.q_by_text(
        "Do you consider yourself a member of a group that is underrepresented or marginalized in technology?")
    report.add_pie_chart("do-you-consider-yourself-to-be-a-part-of-an-underrepresented-group",
                         marginal_q)

    which_marginal_q = "Which of the following underrepresented or marginalized groups in technology do you consider yourself a part of?"
    report.add_bar_chart("which-marginalized-group",
                         summary.q_by_text(which_marginal_q),
                         summary_2024.q_by_text(which_marginal_q),
                         xaxis_tickangle=45,
                         max_tick_width=40,
                         bar_label_vertical=True)

    student_q = "Are you a full- or part-time student?"
    report.add_bar_chart("are-you-a-student", summary.q_by_text(student_q),
                         summary_2024.q_by_text(student_q),
                         xaxis_tickangle=45,
                         max_tick_width=40,
                         bar_label_vertical=True)
    report.add_pie_chart("how-long-have-you-been-programming", summary.q_by_text(
        "How long have you been programming (in any language, for any reason)?"))
    report.add_pie_chart("where-do-you-live", summary.q_by_text("Where do you live?"))
    report.add_bar_chart("in-what-ways-are-you-comfortable-communicating", summary.q_by_text(
        "In what ways are you comfortable communicating about technical topics in English?"),
                         xaxis_tickangle=45, max_tick_width=45)
    report.add_bar_chart("what-are-your-preferred-languages-for-technical-communication",
                         summary.q_by_text(
                             "In which language(s) are you most comfortable when consuming existing technical content (e.g. blog posts, documentation, etc.)?"),
                         xaxis_tickangle=45)
    return report


if __name__ == "__main__":
    """
    Renders the PDF report and a blog post for the 2025 Annual survey report.
    Expects CSV data extracted from SurveyHero at <surveys-repo-root/data>.
    See `annual_survey_2025_report` for more details.
    """
    random.seed(42)
    np.random.seed(42)

    report = annual_survey_2025_report()

    # 2024
    # resource_dir = "2025-02-13-rust-survey-2024"
    # # Fill path to blog root (i.e. a checkout of https://github.com/rust-lang/blog.rust-lang.org)
    # blog_root = Path("/projects/personal/rust/blog.rust-lang.org")
    # # relative path in this repository where the survey Markdown template is
    # template_path = Path("surveys/2024-annual-survey/report/2025-02-13-2024-State-Of-Rust-Survey-results.md")
    # render_blog_post(
    #     template=template_path,
    #     blog_root=blog_root,
    #     resource_dir=resource_dir,
    #     report=report
    # )

    # 2025
    #resource_dir = "2025-02-13-rust-survey-2025"
    # Fill path to blog root (i.e. a checkout of https://github.com/rust-lang/blog.rust-lang.org)
    blog_dir = Path("/projects/blog.rust-lang.org")
    # subdir where to copy the generated assets for the blog post (markdown, scripts and images)
    blog_post_rel_path = Path("content/2025-state-of-rust-survey-results")
    # absolute path where the survey Markdown template is
    template_path = Path("/projects/surveys/surveys/2025/annual-survey/report/2026-02-13-2025-State-Of-Rust-Survey-results.md")
    render_blog_post(
        template=template_path,
        blog_dir=blog_dir,
        blog_post_rel_path=blog_post_rel_path,
        report=report
    )

    if len(sys.argv) == 2 and sys.argv[1] == "--skip-pdf":
        sys.exit(0)

    # Set `include_labels=False` to remove the question ID labels from the top left corner of the PDF (used for debugging)
    render_report_to_pdf(
        report,
        Path(__file__).parent / "annual-survey-2025-report.pdf",
        "Rust Annual survey 2025 report",
        include_labels=True
    )
