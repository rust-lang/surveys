# Survey questions

## Rust Usage

### Do you use Rust?

Select one:

- Yes, I have used Rust in the past three months
- I have used Rust in the past, but not in the past three months
- No, I have never used Rust

> **justification**
> Fundamental for cohort analysis
>
> **changes**
> Rephrased answers slightly to be more precise.
>
> **TODOs**
> Is three months the right amount of time?

## For previous Rust users

### How long did you use Rust before you stopped?

Select one:

> **REMOVED**
>
> While possible uses include cohort analysis (did people who stopped quickly have different
> reasons compared to those who took longer?), or tracking over time whether people spend longer
> with Rust, neither of these data are actionable.

### How long ago did you stop using Rust?

Select one:

> **REMOVED**
>
> Not useful, same reasoning as above.

### Why did you stop using Rust?

Select all that apply:

- I did not see any benefit to using Rust
- Rust was too intimidating, too hard to learn, or too complicated
- Rust didn't have the libraries I need
- Rust didn't have the tools I need
- Rust didn't have good enough IDE or editor support
- Rust didn't support the platforms I need
- Rust seemed too risky to use in production
- My company doesn't use Rust
- Switching to Rust made me less productive
- I needed better interoperability between Rust and other languages
- Other [open response]

> **justification**
> Useful for understanding why people give up on Rust.
>
> TODO should we update the answer list? I might merge the tools and IDE options

### If you indicated a lack of support for platforms or architectures that you would like to target, which would those be?

Free form.

> **REMOVED**
>
> Vague, not useful (platform support is primarily driven by supply rather than demand, there are
> unlikely to be platforms which are unknown to us and in demand).

### If you indicated a desire for increased interoperability, which of the following languages would you want to use with Rust?

Select all that apply:

> **REMOVED**
>
> Not useful (support for language interop is community, rather than project, driven).

### Please provide any additional details on why you stopped using Rust.

Free form.

> **REMOVED**
>
> Vague.

### As you have indicated that you're no longer using Rust, what prompted you to participate in this survey?

Select all that apply:

- I plan to return to using Rust in the future.
- I consider myself part of the Rust Community.
- Specifically to provide feedback on WHY I stopped using Rust.
- Curiosity.
- Other [open response]

> **ADDED**
> 
> Useful in understanding why non-users contribute;
> depth of Rust community connection;
> likelihood of returning to Rust

> **SURVEY FLOW**
>
> Skip to ##About You section

## For non-Rust users

### I never used Rust because...

Select all that apply:

- I did not see any benefit to using Rust
- Rust was too intimidating, too hard to learn, or too complicated
- Rust doesn't have the libraries I need
- Rust doesn't have the tools I need
- Rust doesn't have good enough IDE or editor support
- Rust doesn't support the platforms I need
- Rust seems too risky to use in production
- I need better interoperability between Rust and other languages
- My company doesn't use Rust
- Switching to Rust would make me less productive
- I haven't learned Rust yet, but I want to
- I haven't learned Rust yet, and I don't want to
- Other

> **justification**
>
> Useful for understanding why people don't use Rust without trying, even though they are interested enough to complete this survey.
> TODO Given the strong bias in the sample, I'm not sure if this data is actually useful.

### As you have indicated that you have not used Rust, what prompted you to participate in this survey?

Select all that apply:

- I plan to use Rust in the future.
- I consider myself part of the Rust Community.
- Specifically to provide feedback on WHY I do not use Rust.
- Curiosity.
- Other [open response]

> **ADDED**
>
> Useful in understanding why non-users contribute;
> depth of Rust community connection;
> likelihood of returning to Rust

### If you indicated a lack of support for platforms or architectures that you would like to target, which would those be?

Free form.

> **REMOVED**
>
> Vague, not useful (see same question for former Rust users).

### If you indicated a desire for increased interoperability, which of the following languages would you want to use with Rust?

Select all that apply:

> **REMOVED**
>
> Not useful (see above).

### Please provide any additional details on why you never used Rust.

Free form.

> **REMOVED**
>
> Vague.

> **SURVEY FLOW**
>
> Skip to `## About You` section

## Your Rust experience

### Which operating systems do you use regularly for Rust development as your dev machine?

Select all that apply:

- *nix
- Windows
- Windows (Windows Subsystem for Linux)
- Mac OS
- other [open response]

### Which operating systems do you develop Rust software for?

Select all that apply:

- *nix (desktop or server)
- Windows
- Mac OS
- embedded platforms
- other

> TODO should we ask if people develop for cross-platform vs a specific platform?

### Which tools do you use (at least once per month), either directly or in CI when doing Rust development?

Select all that apply:

- an IDE or editor with plugin doing more than syntax highlighting
- debugger
- profiler
- clippy
- rustfmt
- Cargo
- Rustup (TODO regualar updates vs advanced use like switching channels?)
- code coverage
- rustdoc

> **NOTE: Jasun stopped here 9/7**

> TODO lots more in this section:
> 
> * Stability of the language
>   * Do people feel that their code is being broken?
>   * How often and what is the severity of this breakage?
>   * In general, do people feel like Rust's stability guarantees are upheld?
>   * How often do people *need* to reach for nightly for the compiler or core tooling?
> * The Rust compiler as a productive tool
>   * Is the perception of {compile times, binary size, artifact disk space (i.e., the target folder)} getting better or worse over time?
> * What are "core tools" for users (i.e., they are an indispensable part of the Rust programming experience?)
> * How is the IDE experience with Rust?
> * How reliable is tooling and how happy are people in general with the user experience?
> * Do people find the edition experience relatively uneventful?
> * Does Rust work well for the platform they are targeting (i.e., the compile target)?
> * Can people usually find the library their looking for? If not, what domains seemed to be the most underserved?
> * Questions which gauge attitudes to potential new features.

### Which of the following apply to you:

- I have contributed (in any way) to a crate published on crates.io
- I am maintainer of a Rust project outside of the core project
- I have contributed (in any way) to a core Rust project (part of the rust-lang GitHub org)
- I'm a member of a Rust team or WG
- I've read the Rust blog
- I've read TWiR
- I've read GH rust-lang org/Zulip/Discord/internals/users/r/rust (separate answers or one answer?)
- I've written a comment/post on GH rust-lang org/Zulip/Discord/internals/users/r/rust (separate answers or one answer?)
- Attended a meetup (including virtual)
- participated in a private Rust community (e.g., work Slack, private messages)

> **justification**
> We'd like to get a picture of _how_ people participate in the Rust community
>
> TODO separate issue management, docs, etc. from code contribution?
> TODO possibly multiple questions for past month, past year, ever, + would you like to do 

### Have you tried but failed to complete any of the following?

- GH issue (Rust)
- GH PR (Rust)
- discuss an RFC
- write an RFC
- discuss Rust on GH rust-lang org/Zulip/internals/Discord
- publish a crate

> TODO this question seems confusing as "failing" might be hard to interpret- shall we reword it?
>
> How welcome do you feel when interacting with the Rust community in the following ways? (1/2/3/NA?) TODO in the last year
>
> - other social media (twitter, facebook, other sites 'outside' core Rust, e.g., r/programming, HN - TODO one or two answers)
> - rust-lang GH
> - other GH Rust project
> - Zulip/internals/Discord
> - users/stack overflow
> - r/rust
> - Rust conferences
> - Local Rust events, e.g., meetups

> TODO anything more objective like asking about particular incidents or kinds of incidents?
> TODO ask about blockers for participation?

## Rust at work

> This section is largely in service of the [contexts](./design/contexts.md) design document.

### Are you using Rust at work

Select one:

- Yes, for the majority of my coding
- Yes, it's one of a number of languages I use and I use it regularly
- Yes, but I only use it occasionally
- No, but it is likely in the next year
- No, I use other programming languages at work
- Not applicable (i.e., I don't write software professionally, I am student, etc.)

> **justification**
>
> We want to establish what percentage of those who could possibly use Rust in a professional setting
> are using Rust in a professional setting. This is most interesting over time. 
> Answers to this question should be combined with whether the respondent has ever used Rust.

> **TODO**: explain why the following questions are not asked
> Is Rust used in the company where you work?

### To what extent is Rust currently being used by your company?

Select one:

- My company uses Rust for a large portion of production projects.
- My company uses Rust for a small portion of production projects.
- My company uses Rust only for non-production projects (e.g., tooling).
- My company has actively experimented with Rust for use in production projects.
- My company has actively experimented with Rust for use in non-production projects.
- My company has seriously discussed but not experimented with using Rust.
- My company has not seriously considered Rust for any use.
- I am unsure whether my company has considered using or currently uses Rust.
- I don't work for a company or my company does not develop software of any kind.

> **justification**
>
> We want to establish how reliant companies are on Rust.

### In what technology domains is Rust used at your company?

Select as many as apply:

- server-side application
- desktop application
- mobile application
- web application
- embedded application
- other

> **justification**
>
> We want to known roughly what technology stacks are being most often used.
>
> **challenges**
>
> This can be ambiguous and hard to answer. For example, if you're building an operating
> system for a mobile phone, is that embedded, mobile, or something else.
> We want to understand the "shape" of Rust usage, and this question only gets at that
> in one particular way.

### Do you or your company use Rust at work?

Select one:

- Yes, I work with Rust full time
- Yes, I work with Rust part time
- No, but my company uses Rust
- No
- Not sure
- Not applicable

> **REMOVED**
>
> This question was removed from the survey, because it was not sufficient in gathering the information we wanted.

### For programmers - what languages, other than Rust, do you use at work?

Free form:

> **REMOVED**
>
> While this might be an interesting question, there's not too much that is directly actionable from it.

### Does your company plan to use Rust or evaluate Rust in the future?

Select one:

- Yes
- No
- I don't know

> **REMOVED**
>
> This data is better captured in other questions.

### How could we make Rust more appealing to your company?

Free form:

> **REMOVED**
>
> This question is too vague and unlikely to yield any interesting answers.

### How many developers at your company use Rust at work?

- 1
- 2-5
- 6-10
- 11-25
- 25-100
- More than 100
- I don't know

> **REMOVED**
>
> This question fails to consider companies with different sizes. One company with 100,000 developers
> where more than 100 use Rust is different than a company with 110 developers. We can gauge the importance
> of Rust to companies through more direct questions

### Approximately how many total developers does your company employ?

- under 10
- 11-49
- 50-99
- 100-500
- 500-1,000
- 1,000-10,000
- Over 10,000

> This question is not that interesting on its own, but it can be used as a sort of co-hort for understanding how answers 
> change depending on the size of the development effort at a company.
>
> Previously this question used "employees" instead of "developers". It is more appropriate for us to ask about the amount
> of developers at a company vs. the amount of people employed in total.

### If you summed up the size of all Rust projects at work, how big would it be?

Select one:

- Less than 1,000 lines
- 1,000 to 10,000 lines
- 10,000 to 100,000 lines
- More than 100,000 lines
- I don't know

> **REMOVED**
>
> While this might be interesting, there's nothing generally actionable from this. We are curious if Rust is playing a bigger
> role in professional settings over time, and this is better served by other questions.

### Is your company planning on hiring Rust developers in the next year?

Select one:

- Yes
- No
- I don't know

> This question assess hiring sentiment. Although there is intrinsic uncertainty, it is easy to answer and forward looking.

### What are some ways you or your company is using Rust at work?

Free form:

> **REMOVED**
>
> This question is extremely vague and has not really been useful in the past.

### How could we make Rust more accepted at your company?

Free form:

> **REMOVED**
>
> This question is vague and has not really been useful in the past.

## Rust in education

> This section is largely in service of the [contexts](./design/contexts.md) design document.

### Are you taking a course or training which uses or teaches Rust, or have you in the past year, or are you enrolled for one in the coming year?

Select one:

- Yes
- No

### Where is the course or activity taught?

Select one:

- University or other tertiary institute
- Bootcamp or other vocational-focussed educational institute
- A short training course offered by your employer or a contracted third party

> TODO are the latter two sufficiently differentiated?

### Which best describes your course or activity?

- A programming course which only teaches Rust
- A programming course which teaches Rust amongst other languages
- An computer science course (e.g., operating systems, algorithms, etc.) course which uses Rust with or without other languages
- Other course which uses Rust
- Individual project
- Group project
- Other activity

### Is Rust mandated for your course or activity, or did you choose it yourself?

- Compulsory
- Optional

## Rust community

### What resources do you use to keep up with the Rust ecosystem?

Select all that apply:

> **REMOVED**
>
> Integrated with 'How do you participate in the community' question

## Rust conferences

### Did you attend a Rust conference in the past year? If so, which ones?

Free form

> **REMOVED**
>
> Vague, not useful. Somewhat replaced by community participation question.

### If you wanted to attend a Rust conference but couldn't, why not?

Free form

> **REMOVED**
>
> Vague. Given how unusual 2020/2021 have been, I don't think these answers will be useful.

### If you are interested in attending a Rust conference, which of these regions would you travel to?

Select all that apply

> **REMOVED**
>
> Conference organisers tend to have a location in mind, rather than be looking for a location.

### Please provide more precise details about where you would travel to for a Rust conference.

Free form

> **REMOVED**
>
> Not useful. The previous list is already very detailed.

## Challenges and feedback

### What do you feel are the biggest challenges or problems for the Rust project? What could we do to improve adoption?

Free form

> **REMOVED**
>
> This is just collecting people's opinions, if we want those we are better off asking questions
> people's specific experiences rather than asking them to 'armchair general' the Rust project.
> See e.g., 'What is your biggest worry for the future of Rust?'

### What new things related to the Rust project are you most excited about in 20XX?

Free form

> **REMOVED**
>
> Vague, not useful (not actionable data; being excited about a feature is not good motivation
> for it).

### Anything else you'd like to tell us?

Free form

> **REMOVED**
>
> Vague

## Contact information

### Email address

Free form

> **REMOVED**
>
> We aren't going to contact anyone

### What are the reasons you would like to be contacted?

Select all that apply:

> **REMOVED**
>
> We aren't going to contact anyone

### If other, why would you like to be contacted?

Free form

> **REMOVED**
>
> We aren't going to contact anyone

## Your opinions about Rust

> This is a new section. I think that there are some subjective questions which are worth asking
> and I'm collecting them here. In the final survey, they may be better scattered amongst other
> questions.

### What is your biggest worry for the future of Rust?

Select one:

- Not enough usage in industry
- Too much interest from industry leads to too much politics
- Not enough users
- Doesn't add a feature I want
- Stagnation
- Instability of the language
- Superseded by an alternative
- Becomes too complex
- Not enough localization
- Other

> Alternative: could rephrase as a 'select all that apply' question
>
> **justification**
>
> Would be useful for leadership to understand the community's fears.

> TODO Other possible questions for this section:
> - Response to challenges (34 from 2020)
> - upgrades breaking code (41, 42 from 2020)
> - what is missing from the ecosystem (44 from 2020)
> - do respondents consider Rust to be an employable skill (from contexts.md)
> - stability - Do people feel that their code is being broken? (from experience.md)
> - Is the perception of {compile times, binary size, artifact disk space (i.e., the target folder)} getting better or worse over time? (from experience.md)
> - Perception of Rust's learning curve? Do people feel like Rust's learning curve is worth it? (from experience.md)

## Demographics

> For methodological purposes, the bulk of the demographics should be at the end of the survey (unless acting as filter/flow questions above)
> They're both easy to complete (beneficial at the end) and somewhat personal (but at this point folks are invested and we've built 'trust')
> Can also be problematic at start if we're asking all easy, personal questions and then get to the harder ones - easy to drop out.

## About you

See [who](./design/who.md).

The following are primarily for cohort analysis, secondarily for understanding the shape of the community.

### Do you identify with an underrepresented group in the technology industry?

Select one:

- yes
- no
- I prefer not to say

> TODO could just be an optional question instead of having "I prefer not to say"
> TODO should we ask which group?  - Can be a follow-up question that only appears to those who select "Yes"
> TODO Identify common/relevant underrepresented group categories (and include an open response)

### Are you a full- or part-time student?

Select one:

- yes
- no

> TODO Does it matter in what field? Do we want a follow-up question like in employment?

### Are you employed full- or part-time (including paid internships)?

- yes, in tech
- yes, in finance
- yes, in government
- yes, in education
- yes, other
- no

### If you are employed, which category best describes the domain in which *you* work?

> TODO - server networking, desktop application, mobile application, web application, embedded, etc.

> TODO categories
> Todo Simplify the "Are you employed?" question - make yes/no. No need for categories there when we capture categories below.

### Do you write or design software in your work?

- yes, primarily as an IC
- I primarily manage others who do
- no

> QUERY: What is an IC?
> 
> FLOW Only for those who say yes/manage above

### If you write or design software, or manage others who do so, how long have you done so professionally?

- <= 5 years
- 5 - 10 years
- 10 - 15 years
- 15 - 20 years
- > 20 years

### Excluding Rust, which programming languages are you experienced with (TODO define level of experience)

- Assembly language of any variety
- C or C++
- Java, Go, Objective C, C#, or similar object-oriented language
- Haskell, Lisp, ML, or other functional language
- Scala, Swift, Kotlin, or other modern, strongly-typed language
- Javascript, Ruby, Python, or other dynamically-typed language

> TODO are these the right categories?
> TODO Second questions for each asking level of experience?

### How long have you been programming (in any language, for fun, learning, work, any reason)?

- < 1 year
- < 3 years
- < 5 years
- < 10 year
- > 10 years

### Which operating systems do you use regularly for software development (not just Rust)?

- *nix
- Windows
- Mac OS
- other

### Which operating systems do you develop software for?

- *nix (desktop or server)
- Windows
- Mac OS
- embedded platforms
- other

> TODO should we ask if people develop for cross-platform vs a specific platform?

### Where do you live?

- North America
- Central America
- South America
- Europe
- Middle East
- Africa
- West, central, or south Asia
- east or south-east Asia
- Australasia or the pacific

> TODO are these the categories we care about? Do we want to separate China from east asia given the distinct communities?
> Note: We could use Survey Language as a proxy for separating China. This depends some on the purpose behind identifying this community and the level of accuracy needed. (Are we interested in location for future planning of events, or to identify culture/group trends?)

### Level of English (select all which apply)

- Can have a technical conversation
- Can understand most technical documentation
- Can understand a technical talk (e.g., at a conference or meetup)
- Some everyday English
- None

### What is your preferred language for technical communication

- English
- Chinese
- Hindi
- Spanish
- Russian
- Japanese
- Other

> TODO Should above Q be multiselection? "Languages"
>
> TODO other questions to understand the community
> - ask community and core team, foundation
> TODO other questions for cohort analysis?
