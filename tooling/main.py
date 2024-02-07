import random
from pathlib import Path

import numpy as np
import pandas as pd

from surveyhero.parser import parse_surveyhero_report, parse_full_answers
from surveyhero.render import render_report_to_pdf, render_blog_post
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
    r_2022 = parse_surveyhero_report(Path("../data/data-2022.csv"), year=2022)
    answers_2022 = parse_full_answers(Path("../data/data-full-2022.csv"), 2022)
    r_2023 = parse_surveyhero_report(Path("../data/data-2023.csv"), year=2023)
    answers_2023 = parse_full_answers(Path("../data/data-full-2023.csv"), 2023)

    # index_2022 = 7
    # index_2023 = 8
    # print(r_2022.q(index_2022).question)
    # print(r_2023.q(index_2023).question)
    # print_answers(r_2022.q(index_2022), r_2023.q(index_2023))
    open_answer_index = 149
    answers = pd.Series(normalize_open_answers(answers_2022.answers[open_answer_index], replace_spaces=True))
    # print(answers.value_counts())
    # print(answers_2022.answers[open_answer_index])

    # for i in range(max(len(r_2022.questions), len(r_2023.questions))):
    #     if i < len(r_2022.questions):
    #         print(f"2022/{i}: {r_2022.questions[i].question}")
    #     if i < len(r_2023.questions):
    #         print(f"2023/{i}: {r_2023.questions[i].question}")

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

    # rename = {
    #     "Yes, I use Rust (for any purpose, even if you're just learning)": "Yes, I use Rust",
    # }
    # report.add_bar_chart("do-you-use-rust", r_2023.q(0).rename_answers(rename), r_2022.q(0).rename_answers(rename))
    #
    # report.add_bar_chart("why-did-you-stop-using-rust", r_2023.q(1), r_2022.q(1),
    #                      bar_label_vertical=True,
    #                      xaxis_tickangle=45,
    #                      max_tick_width=50)
    # report.add_wordcloud("why-did-you-stop-using-rust-wordcloud", answers_2023.answers[11])
    #
    # report.add_bar_chart("why-dont-you-use-rust", r_2023.q(2), r_2022.q(2).rename_answers({
    #     "I have not got round to it": "I haven't got around to it",
    #     "Missing Libraries": "Missing libraries"
    # }), bar_label_vertical=True, xaxis_tickangle=45, max_tick_width=40)
    # report.add_wordcloud("why-dont-you-use-rust-wordcloud", answers_2023.answers[23])
    #
    # report.add_bar_chart("how-often-do-you-use-rust", r_2023.q(3), r_2022.q(3))
    # report.add_pie_chart("how-often-do-you-code", r_2023.q(4))
    # report.add_bar_chart("how-would-you-rate-your-rust-expertise", r_2023.q(5), r_2022.q(4).rename_answers({
    #     "I can't read or write Rust": "I can't write Rust code"
    # }), xaxis_tickangle=45, max_tick_width=40)
    # report.add_pie_chart("when-did-you-learn-rust", r_2023.q(6))
    #
    # report.add_bar_chart("which-os-do-you-use", r_2023.q(7).combine_answers({
    #     "Windows": ["Windows 10/11", "Windows 8 or older"]
    # }), r_2022.q(6).rename_answers({
    #     "Mac OS": "macOS"
    # }), max_tick_width=20)
    # report.add_wordcloud("which-os-do-you-use-wordcloud", answers_2023.answers[35])
    #
    # report.add_bar_chart("which-os-do-you-target", r_2023.q(8).combine_answers({
    #     "Windows": ["Windows 10/11", "Windows 8 or older"]
    # }), r_2022.q(7).rename_answers({
    #     "Mac OS": "macOS"
    # }), bar_label_vertical=True, xaxis_tickangle=45, max_tick_width=50)
    # report.add_wordcloud("which-os-do-you-target-wordcloud", answers_2023.answers[47])
    #
    # report.add_pie_chart("which-version-of-rust-do-you-use", r_2023.q(9), max_label_width=32)
    # report.add_wordcloud("which-version-of-rust-do-you-use-wordcloud", answers_2023.answers[58])
    #
    # report.add_pie_chart("if-you-use-nightly-why", r_2023.q(10))
    # report.add_wordcloud("if-you-use-nightly-why-wordcloud", answers_2023.answers[70])
    #
    # report.add_pie_chart("what-is-the-oldest-version-of-rust-you-use", r_2023.q(11))

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
        "Disk space usage (e.g., the size of the target folder)": "Disk space usage",
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
            y=0.1,
            yref="container"
        )
    )

    # TODO: fix label width
    report.add_pie_chart("do-you-think-that-new-features-should-be-implemented", r_2023.q(14))

    render_report_to_pdf(
        report,
        Path("report.pdf"),
        "Rust annual survey 2023 report",
        include_labels=True
    )
    exit()

    report.add_matrix_chart(
        "which-features-do-you-want-stabilized",
        r_2023.q(15),
        categories=priority_categories,
        category_label=priority_label
    )
    report.add_wordcloud("which-features-do-you-want-stabilized-wordcloud", answers_2023.answers[113])

    report.add_pie_chart("which-problems-do-you-remember-encountering", r_2023.q(16).rename_answers({
        "Other (please specify)": "Other"
    }))
    report.add_wordcloud("which-problems-do-you-remember-encountering-wordcloud", answers_2023.answers[124])

    report.add_pie_chart("how-do-you-build-your-rust-projects", r_2023.q(17).combine_answers({
        "I combine Cargo and another build system": [
            "I combine Cargo and another build system",
            "If you use Cargo with (or just use) other build systems, which ones do you use?"
        ]
    }))
    report.add_wordcloud("how-do-you-build-your-rust-projects-wordcloud", answers_2023.answers[129])

    report.add_pie_chart("how-do-download-crates", r_2023.q(18))

    # TODO: fix long answers
    report.add_matrix_chart(
        "what-do-you-think-about-rust-stability",
        r_2023.q(19),
        categories=agreement_categories,
        category_label=agreement_label
    )

    # TODO: fix chart
    report.add_matrix_chart(
        "how-often-do-you-engage-in-community-events",
        r_2023.q(20),
        categories=frequency_categories,
        category_label=frequency_label
    )

    # TODO: fix chart
    report.add_matrix_chart(
        "what-was-your-experience-in-the-community",
        r_2023.q(21),
        categories=welcoming_categories,
        category_label=welcoming_label
    )

    # TODO: fix label
    report.add_pie_chart("have-you-taken-a-rust-course", r_2023.q(22), )

    report.add_pie_chart("what-kind-of-learning-materials-have-you-consumed", r_2023.q(23).rename_answers({
        "Other (please specify)": "Other"
    }))
    report.add_wordcloud("what-kind-of-learning-materisla-have-you-consumed-wordcloud", answers_2023.answers[165])

    report.add_pie_chart("are-you-employed", r_2023.q(24))
    report.add_pie_chart("do-you-design-software", r_2023.q(25))

    report.add_bar_chart("do-you-personally-use-rust-at-work", r_2023.q(26), r_2022.q(17))
    report.add_bar_chart("how-is-rust-used-at-your-organization", r_2023.q(27), r_2022.q(20).rename_answers({
        "I am unsure whether my company has considered using or currently uses Rust": "I am unsure whether my organisation has considered using or currently uses Rust",
        "I don't work for a company or my company does not develop software of any kind": "I don't work for a organisation or my organisation does not develop software of any kind",
        "My company has experimented with Rust or is considering using it": "My organisation has experimented with Rust or is considering using it",
        "My company has not seriously considered Rust for any use": "My organisation has not seriously considered Rust for any use",
        "My company makes non-trivial use of Rust (e.g., used in production or in significant tooling)": "My organisation makes non-trivial use of Rust (e.g., used in production or in significant tooling)"
    }))
    report.add_bar_chart("which-statements-apply-to-rust-at-work", r_2023.q(28), r_2022.q(19))

    # Analysis: embedded boost?
    report.add_bar_chart("why-you-use-rust-at-work", r_2023.q(29), r_2022.q(18))

    base_open = normalize_open_answers(answers_2022.answers[149], replace_spaces=True)
    base = (
        r_2022.q(23)
        .add_open(base_open, "game-development", "Computer Games")
        .add_open(base_open, "video-games", "Computer Games")
    )

    # Note: computer games were open before
    report.add_bar_chart("technology-domain", r_2023.q(30), base)
    report.add_wordcloud("technology-domain-wordcloud", answers_2023.answers[213])

    # TODO: reorder legend
    report.add_pie_chart("how-many-developers-does-your-organization-employ", r_2023.q(31))

    # TODO: merge bars
    report.add_bar_chart("is-your-organization-planning-on-hiring-rust-developers", r_2023.q(32), r_2022.q(22))

    report.add_bar_chart("which-of-the-following-statements-about-rust-do-you-agree-with", r_2023.q(33), r_2022.q(24))

    # TODO: fix label
    report.add_pie_chart("what-are-your-biggest-worries-about-rust", r_2023.q(34))
    report.add_wordcloud("what-are-your-biggest-worries-about-rust-wordcloud", answers_2023.answers[238])

    report.add_matrix_chart(
        "assessment-of-rust-employment-statements",
        r_2023.q(35),
        categories=agreement2_categories,
        category_label=agreement_label
    )

    # TODO: change question
    report.add_pie_chart("do-you-consider-yourself-to-be-a-part-of-an-underrepresented-group", r_2023.q(36))
    report.add_pie_chart("which-marginalized-group", r_2023.q(37))
    report.add_bar_chart("are-you-a-student", r_2023.q(38), r_2022.q(31))
    report.add_pie_chart("how-long-have-you-been-programming", r_2023.q(39))
    report.add_pie_chart("where-do-you-live", r_2023.q(40))
    report.add_pie_chart("in-what-ways-are-you-comfortable-communicating", r_2023.q(41))
    report.add_pie_chart("what-are-your-preferred-languages-for-technical-communication", r_2023.q(42))

    report.add_wordcloud("any-other-comments-wordcloud", answers_2023.answers[250])
    return report


if __name__ == "__main__":
    # TODO: fix charts

    random.seed(42)
    np.random.seed(42)

    report = annual_survey_2023_report()

    blog_root = Path("/projects/personal/rust/blog.rust-lang.org")
    image_dir = "2024-02-rust-survey-2023"
    render_report_to_pdf(
        report,
        blog_root / "static" / "images" / image_dir / "annual-survey-2023-report.pdf",
        "Rust annual survey 2023 report",
        include_labels=True
    )
    render_blog_post(
        template=Path("blog-2023-template.md"),
        blog_root=blog_root,
        output_name="2024-02-06-2023-Rust-Annual-Survey-2023-results.md",
        image_dir=image_dir,
        report=report
    )
