#let maketitle(
  title: str,
  date: datetime,
  authors: (),
  type: (),
  doc,
) = {
  set page(paper: "a4", margin: (
    x: 1.135in,
    y: 1.345in

  ))
  set text(font: "Palatino")
  place(
    top + left,
    image("~/Dev/rust/rust-lang/surveys/typst/template/rust-logo-blk.svg"),
  )
  place(
    horizon + left,
    grid(
      columns: 2,
      rows: 1,
      align: top,
      gutter: 1em,
      rect(
        stroke: none,
        inset: 0em,
        width: 100%,
        stack(
          dir: ttb,
          spacing: 1em,
          text(title, weight: 700, size: 25pt),
        ),
      ),
      stack(
        dir: ttb,
        spacing: 1em,
        [Compiled and presented by the Rust Survey Team],
        text(size: 10pt)[
          #smallcaps[Report Dated] #date.display("[weekday repr:long], [day]th [month repr:long] [year]")
        ],
      ),
    ),
  )
  pagebreak()
  show outline.entry: set block(above: 1.2em)
  outline(title: text(size: 20pt, weight: 700)[Contents #v(1.2em)])
  pagebreak()
  show heading.where(level: 1): set text(font: "Palatino", size: 20pt)
  set heading(numbering: "I.") // For Level 1 headings (e.g., 1, 2, 3)
  set heading(numbering: "I.1.")
  set page(columns: 2)
  doc
}

#let acute(x) = x + "\u{301}"

#show: doc => maketitle(
  authors: ([Jakub Ber#acute("a")nek], "apiraino"),
  date: datetime.today(),
  type: "Report Template",
  title: "The State of Rust Survey Report, 2024",
  doc,
)
= Executive Summary
Hello, Rustaceans!

The Rust Survey Team is excited to share the results of our
#link("https://blog.rust-lang.org/2024/12/05/annual-survey-2024-launch.html")[2024 survey on the Rust Programming language];,
conducted between December 5, 2024 and December 23, 2024. As in previous
years, the 2024 State of Rust Survey was focused on gathering insights
and feedback from Rust users, and all those who are interested in the
future of Rust more generally.

This ninth edition of the survey surfaced new insights and learning
opportunities straight from the global Rust language community, which we
will summarize below. In addition to this blog post, #strong[we have
  also prepared a
  #link("https://raw.githubusercontent.com/rust-lang/surveys/main/surveys/2024-annual-survey/report/annual-survey-2024-report.pdf")[report];]
containing charts with aggregated results of all questions in the
survey.

#strong[Our sincerest thanks to every community member who took the time
  to express their opinions and experiences with Rust over the past year.
  Your participation will help us make Rust better for everyone.]

There's a lot of data to go through, so strap in and enjoy!

== Participation
<participation>
#figure(
  scope: "parent",
  placement: bottom,
  align(center)[#table(
  stroke:none,
      columns: (16.67%, 18.06%, 20.83%, 29.17%, 15.28%),
      align: (center, right, right, right, right),
      table.header(
      table.hline(),
        [#strong[Survey];],
        [#strong[Started];],
        [#strong[Completed];],
        [#strong[Completion
            rate];],
        [#strong[Views];],
      ),
      table.hline(),
      [2023], [11 950], [9 710], [82.2%], [16 028],
      [2024], [9 450], [7 310], [77.4%], [13 564],
      table.hline(),
    )],
  kind: table,
  caption: "Participation",
)<table:participation>

As shown in @table:participation, in 2024, we have received fewer survey views than in the
previous year. This was likely caused simply by the fact that the survey
ran only for two weeks, while in the previous year it ran for almost a
month. However, the completion rate has also dropped, which seems to
suggest that the survey might be a bit too long. We will take this into
consideration for the next edition of the survey.

== Community
<community>
The State of Rust survey not only gives us excellent insight into how
many Rust users around the world are using and experiencing the language
but also gives us insight into the makeup of our global community. This
information gives us a sense of where the language is being used and
where access gaps might exist for us to address over time. We hope that
this data and our related analysis help further important discussions
about how we can continue to prioritize global access and inclusivity in
the Rust community.

Same as every year, we asked our respondents in which country they live
in. The top 10 countries represented were, in order: United States
(22%), Germany (14%), United Kingdom (6%), France (6%), China (5%),
Canada (3%), Netherlands (3%), Russia (3%), Australia (2%), and Sweden
(2%). We are happy to see that Rust is enjoyed by users from all around
the world! You can try to find your country in the chart below:

We also asked whether respondents consider themselves members of a
marginalized community. Out of those who answered, 74.5% selected no,
15.5% selected yes, and 10% preferred not to say.

We have asked the group that selected “yes” which specific groups they
identified as being a member of. The majority of those who consider
themselves a member of an underrepresented or marginalized group in
technology identify as lesbian, gay, bisexual, or otherwise
non-heterosexual. The second most selected option was neurodivergent at
46% followed by trans at 35%.

Each year, we must acknowledge the diversity, equity, and inclusivity
(DEI) related gaps in the Rust community and open source as a whole. We
believe that excellent work is underway at the Rust Foundation to
advance global access to Rust community gatherings and distribute grants
to a diverse pool of maintainers each cycle, which you can learn more
about #link("https://rustfoundation.org/community")[here];. Even so,
global inclusion and access is just one element of DEI, and the survey
working group will continue to advocate for progress in this domain.

== Rust usage
<rust-usage>
The number of respondents that self-identify as a Rust user was quite
similar to last year, around 92%. This high number is not surprising,
since we primarily target existing Rust developers with this survey.

Similarly as last year, around 31% of those who did not identify as Rust
users cited the perception of difficulty as the primary reason for not
using Rust. The most common reason for not using Rust was that the
respondents simply haven't had the chance to try it yet.

Of the former Rust users who participated in the 2024 survey, 36% cited
factors outside their control as a reason why they no longer use Rust,
which is a 10pp decrease from last year. This year, we also asked
respondents if they would consider using Rust again if an opportunity
comes up, which turns out to be true for a large fraction of the
respondents (63%). That is good to hear!

#quote(block: true)[
  Closed answers marked with N/A were not present in the previous
  version(s) of the survey.
]

Those not using Rust anymore told us that it is because they don't
really need it (or the goals of their company changed) or because (like
above) it was not the right tool for the job. A few reported being
overwhelmed by the language or its ecosystem in general or that
switching or introducing Rust would have been too expensive in terms of
human effort.

Of those who used Rust in 2024, 53% did so on a daily (or nearly daily)
basis --- an increase of 4pp from the previous year. We can observe an
upward trend in the frequency of Rust usage over the past few years,
which suggests that Rust is being increasingly used at work. This is
also confirmed by other answers mentioned in the Rust at Work section
later below.

Rust expertise is also continually increasing amongst our respondents!
20% of respondents can write (only) simple programs in Rust (a decrease
of 3pp from 2023), while 53% consider themselves productive using Rust
--- up from 47% in 2023. While the survey is just one tool to measure
the changes in Rust expertise overall, these numbers are heartening as
they represent knowledge growth for many Rustaceans returning to the
survey year over year.

Unsurprisingly, the most popular version of Rust is #emph[latest
  stable];, either the most recent one or whichever comes with the users'
Linux distribution. Almost a third of users also use the latest nightly
release, due to various reasons (see below). However, it seems that the
beta toolchain is not used much, which is a bit unfortunate. We would
like to encourage Rust users to use the beta toolchain more (e.g.~in CI
environments) to help test soon-to-be stabilized versions of Rust.

People that use the nightly toolchain mostly do it to gain access to
specific unstable language features. Several users have also mentioned
that rustfmt works better for them on nightly or that they use the
nightly compiler because of faster compilation times.

== Learning Rust
<learning-rust>
To use Rust, programmers first have to learn it, so we are always
interested in finding out how do they approach that. Based on the survey
results, it seems that most users learn from Rust documentation and also
from
#link("https://doc.rust-lang.org/book/")[The Rust Programming Language]
book, which has been a favourite learning resource of new Rustaceans for
a long time. Many people also seem to learn by reading the source code
of Rust crates. The fact that both the documentation and source code of
tens of thousands of Rust crates is available on
#link("https://docs.rs")[docs.rs] and GitHub makes this easier.

In terms of answers belonging to the "Other" category, they can be
clustered into three categories: people using LLM (large language model)
assistants (Copilot, ChatGPT, Claude, etc.), reading the official Rust
forums (Discord, #link("https://users.rust-lang.org/")[URLO];) or being
mentored while contributing to Rust projects. We would like to extend a
big thank you to those making our spaces friendly and welcoming for
newcomers, as it is important work and it pays off. Interestingly, a
non-trivial number of people "learned by doing" and used rustc error
messages and clippy as a guide, which is a good indicator of the quality
of Rust diagnostics.

In terms of formal education, it seems that Rust has not yet penetrated
university curriculums, as this is typically a very slowly moving area.
Only a very small number of respondents (around 3%) have taken a
university Rust course or use university learning materials.

== Programming environment
<programming-environment>
In terms of operating systems used by Rustaceans, Linux was the most
popular choice, and it seems that it is getting increasingly popular
year after year. It is followed by macOS and Windows, which have a very
similar share of usage.

#quote(block: true)[
  As you can see in the
  #link("../../../images/2025-02-13-rust-survey-2024/which-os-do-you-use-wordcloud.png")[wordcloud];,
  there are also a few users that prefer Arch, btw.
]

Rust programmers target a diverse set of platforms with their Rust
programs. We saw a slight uptick in users targeting embedded and mobile
platforms, but otherwise the distribution of platforms stayed mostly the
same as last year. Since the WebAssembly target is quite diverse, we
have split it into two separate categories this time. Based on the
results it is clear that when using WebAssembly, it is mostly in the
context of browsers (23%) rather than other use-cases (7%).

We cannot of course forget the favourite topic of many programmers:
which IDE (developer environment) they use. Although Visual Studio Code
still remains the most popular option, its share has dropped by 5pp this
year. On the other hand, the Zed editor seems to have gained
considerable traction recently. The small percentage of those who
selected "Other" are using a wide range of different tools: from
CursorAI to classics like Kate or Notepad++. Special mention to the 3
people using "ed", that's quite an achievement.

#quote(block: true)[
  You can also take a look at the linked
  #link("../../../images/2025-01-rust-survey-2024/what-ide-do-you-use-wordcloud.png")[wordcloud]
  that summarizes open answers to this question (the "Other" category), to
  see what other editors are also popular.
]

== Rust at Work
<rust-at-work>
We were excited to see that more and more people use Rust at work for
the majority of their coding, 38% vs 34% from last year. There is a
clear upward trend in this metric over the past few years.

The usage of Rust within companies also seems to be rising, as 45% of
respondents answered that their organisation makes non-trivial use of
Rust, which is a 7pp increase from 2023.

Once again, the top reason employers of our survey respondents invested
in Rust was the ability to build relatively correct and bug-free
software. The second most popular reason was Rust's performance
characteristics. 21% of respondents that use Rust at work do so because
they already know it, and it's thus their default choice, an uptick of
5pp from 2023. This seems to suggest that Rust is becoming one of the
baseline languages of choice for more and more companies.

Similarly to the previous year, a large percentage of respondents (82%)
report that Rust helped their company achieve its goals. In general, it
seems that programmers and companies are quite happy with their usage of
Rust, which is great!

In terms of technology domains, the situation is quite similar to the
previous year. Rust seems to be especially popular for creating server
backends, web and networking services and cloud technologies. It also
seems to be gaining more traction for embedded use-cases.

#quote(block: true)[
  You can scroll the chart to the right to see more domains. Note that the
  Automotive domain was not offered as a closed answer in the 2023 survey
  (it was merely entered through open answers), which might explain the
  large jump.
]

It is exciting to see the continued growth of professional Rust usage
and the confidence so many users feel in its performance, control,
security and safety, enjoyability, and more!

== Challenges
<challenges>
As always, one of the main goals of the State of Rust survey is to shed
light on challenges, concerns, and priorities on Rustaceans' minds over
the past year.

We have asked our users about aspects of Rust that limit their
productivity. Perhaps unsurprisingly, slow compilation was at the top of
the list, as it seems to be a perennial concern of Rust users. As
always, there are efforts underway to improve the speed of the compiler,
such as enabling the
#link("https://blog.rust-lang.org/2023/11/09/parallel-rustc.html")[parallel frontend]
or switching to a
#link("https://blog.rust-lang.org/2024/05/17/enabling-rust-lld-on-linux.html")[faster linker by default];.
We invite you to test these improvements and let us know if you
encounter any issues.

Other challenges included subpar support for debugging Rust and high
disk usage of Rust compiler artifacts. On the other hand, most Rust
users seem to be very happy with its runtime performance, the
correctness and stability of the compiler and also Rust's documentation.

In terms of specific unstable (or missing) features that Rust users want
to be stabilized (or implemented), the most desired ones were async
closures and if/let while chains. Well, we have good news! Async
closures will be stabilized in the next version of Rust (1.85), and
if/let while chains will hopefully follow
#link("https://github.com/rust-lang/rust/pull/132833")[soon after];,
once Edition 2024 is released (which will also happen in Rust 1.85).

Other coveted features are generators (both sync and async) and more
powerful generic const expressions. You can follow the
#link("https://rust-lang.github.io/rust-project-goals/2025h1/goals.html")[Rust Project Goals]
to track the progress of these (and other) features.

People were really helpful and tried hard pointing their most notable
issues limiting productivity in the open answers to this question. We
have seen mentions of struggles with async programming (an all-time
favourite), debuggability of errors (which people generally love, but
they are not perfect for everyone) or Rust tooling being slow or
resource intensive (rust-analyzer and rustfmt). Some users also want a
better IDE story and improved interoperability with other languages.

This year, we have also included a new question about the speed of
Rust's evolution. While most people seem to be content with the status
quo, more than a quarter of people who responded to this question would
like Rust to stabilize and/or add features more quickly, and only 7% of
respondents would prefer Rust to slow down or completely stop adding new
features.

Interestingly, when we asked respondents about their main worries for
the future of Rust, one of the top answers remained the worry that Rust
will become too complex. This seems to be in contrast with the answers
to the previous question. Perhaps Rust users still seem to consider the
complexity of Rust to be manageable, but they worry that one day it
might become too much.

We are happy to see that the amount of respondents concerned about Rust
Project governance and lacking support of the Rust Foundation has
dropped by about 6pp from 2023.

== Looking ahead
<looking-ahead>
Each year, the results of the State of Rust survey help reveal the areas
that need improvement in many areas across the Rust Project and
ecosystem, as well as the aspects that are working well for our
community.

If you have any suggestions for the Rust Annual survey, please
#link("https://github.com/rust-lang/surveys/issues")[let us know];!

We are immensely grateful to those who participated in the 2024 State of
Rust Survey and facilitated its creation. While there are always
challenges associated with developing and maintaining a programming
language, this year we were pleased to see a high level of survey
participation and candid feedback that will truly help us make Rust work
better for everyone.

If you'd like to dig into more details, we recommend you to browse
through the full
#link("https://raw.githubusercontent.com/rust-lang/surveys/main/surveys/2024-annual-survey/report/annual-survey-2024-report.pdf")[survey report];.

#pagebreak()

= Aggregated Results
