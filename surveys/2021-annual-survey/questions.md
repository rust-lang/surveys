# Survey questions

Whether or not you use Rust Programming Language <https://rust-lang.org> today, we want to hear from you!

The Rust Community Team has created this survey to help us gauge how we're doing, what can be improved, and how we can best engage with all of you as we move forward.

This is your chance to have a say in the development priorities for Rust.

Unless you choose to enter your email, your answers will be anonymous. Any personal data you submit as a part of this survey will be handled in accordance with our policy as described in our Frequently Asked Questions:

https://github.com/rust-community/team/wiki/State-of-the-Rust-Language-Community-Survey-FAQ

We estimate it will take about 10-15 minutes to complete.

> TODOs:
>
> - Ensure that the survey actually takes 10-15 minutes

## Rust Usage

### Do you use Rust?

Select one:

- Yes, I have used Rust [`NEXT`](#your-rust-experience)
- No, I don't use Rust, but I have in the past [`NEXT`](#for-previous-rust-users)
- No, I have never used Rust [`NEXT`](#for-non-rust-users)

> **justification**
>
> Fundamental for cohort analysis
>
> **changes**
>
> Rephrased answers slightly.

## For previous Rust users

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
- Other (open response)

> **justification**
>
> Useful for understanding why people give up on Rust.
>
> **TODO**
>
> - What will we actually do with this information once we know it?

### As you have indicated that you're no longer using Rust, what prompted you to participate in this survey?

Select all that apply:

- I plan to return to using Rust in the future.
- I consider myself part of the Rust Community.
- Specifically to provide feedback on why I stopped using Rust.
- To provide feedback on Rust in general.
- Curiosity.
- Other (open response)

> **ADDED**
>
> **justification**
>
> Useful in understanding why non-users contribute;

> **SURVEY FLOW**
>
> Skip to `## About You` section

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
- Other (open response)

> **justification**
>
> Useful for understanding why people don't use Rust without trying, even though they are interested enough to complete this survey.
>
> **TODO** Given the strong bias in the sample, I'm not sure if this data is actually useful.

### As you have indicated that you have not used Rust, what prompted you to participate in this survey?

Select all that apply:

- I plan to use Rust in the future.
- I consider myself part of the Rust Community.
- Specifically to provide feedback on WHY I do not use Rust.
- Curiosity.
- Other (open response)

> **ADDED**
>
> Useful in understanding why non-users contribute to the survey

> **SURVEY FLOW**
>
> Skip to `## About You` section

## Your Rust experience

### How would you rate your Rust expertise?

Select 0-4 (0 = I can't write or read Rust, 1 = I can write simple exercises in Rust, 2 = I can write useful, production-ready code but it is a struggle, 3 = I am productive writing Rust, 4 = I'm an expert)

> **justification**
>
> Useful for cohort analysis, i.e., for other questions we can query if answers are significantly different for beginners vs advanced users.

### How often do you use Rust?

Select one:

- Daily or nearly so
- Weekly or nearly so
- Monthly or nearly so
- Rarely

> **justification**
>
> This can be useful demographic information as a proxy for how "important" Rust is
> in someone's technical life.
>
> We deliberately use calendar time for this question to gauge how "serious" the
> programmers use of Rust is. This does mean that we will group together, for example,
> those who program once a week but always in Rust and those who program daily but
> use Rust once a week.

### How would you rate the learning of these concepts?

Options: Easy, Moderate, Tricky, Very Difficult, Still Don't Get it, N/A (haven't learned)

Concepts: Enums, Modules, Ownership & Borrowing, Iterators, Traits, Generics and Trait Bounds, Lifetimes, Cargo, Macros, Unsafe, Async I/O, Pattern Matching, Collections, Closures, FFI, Concurrency

> **TODO** this question usually makes great blog material, but it's really not actionable. Teachers of Rust generally have a good idea of what's difficult to teach, and Rust compiler devs have a good idea of what the papercuts are. Perhaps it should be removed.
> **Justification** Might not be directly applicable, but does provide verification of the perceptions of teachers/devs.
Plus, it demonstrates to users that you are interested in their perceptions of where the papercuts are.

### I would use Rust more if...

Select all that apply:

- I saw more benefit of using Rust
- Rust wasn't too intimidating or too complicated
- Rust had the libraries I need
- Rust had the tools I need
- Rust had good enough IDE or editor support
- Rust supported the platforms I need
- Rust didn't seem too risky to use in production
- Rust had better interoperability support with other languages
- My company used Rust
- Switching to Rust didn't make me less productive
- Other (open response)

> **TODO** this question seems like it could be useful, but how?
> **Justification** I think it's this question in combination with follow-up questions that really provides us with the insight. It's not just "I need better Interoperability" - it's "I need better interop with these languages.
> This q provides the scope of the concern, while the follow-up provides the actionable. (The scope helps determine which actionable to prioritize.)

### If you indicated a desire for increased interoperability, which of the following languages would you want to use with Rust?

- C
- C++
- C#
- Clojure
- Elm
- Elixir
- Erlang
- Go
- Haskell
- Java
- JavaScript
- Objective-C
- PHP
- Python
- Ruby
- Scala
- Swift

> **justification**
>
> This question has led to surprising answers in the past that could help the lang team better prioritize features that make interop easier.

### Which operating systems do you use regularly for Rust development as your dev machine?

Select all that apply:

- *nix
- Windows
- Windows Subsystem for Linux
- Mac OS
- Other (open response)

### On the primary machine you compile Rust code on, how many logical CPU threads do you have?

Please count logical CPUs here, not cores or sockets. To get this number on
Linux, run `nproc`; on macOS, run `sysctl -n hw.ncpu`; on Windows, run
`echo %NUMBER_OF_PROCESSORS%`.

Free form.

> **justification**
>
> Question added by Josh Triplett. The answers can help tune parallel rustc:
>
> - When we encounter a scalability issue that starts at a certain number of CPUs, it'll be good to know what proportion of the Rust community is affected.
> - It'll help when tuning algorithms or build systems whose memory usage may depend on the number of CPUs present.
> - It'll help with prioritization around whether to make something go faster by throwing more CPUs at it or by optimizing on the same number of CPUs.
> - It'll help avoid assumptions that rust developers might otherwise make about how universal the caliber of hardware they have is.

### Which operating systems do you develop Rust software for?

Select all that apply:

- *nix (desktop or server)
- Windows
- Mac OS
- iOS
- Android
- Embedded platforms (with an operating system)
- Embedded platforms (bare metal)
- Other (open response)

### Which version(s) of Rust do you use?

Select one:

- Current stable version
- Previous stable version
- Some other specific version of stable Rust
- Beta release
- Latest nightly
- A specific version of nightly
- Custom fork
- I don't know
- Other (open response)

### When I upgrade to a new **stable** version of the compiler...

Select one:

- I am confident my code will continue to compile and be idiomatic.
- I am confident my code will continue to compile but it may be unidiomatic.
- There's a chance my code may no longer compile.
- I am confident my code will break somehow.

> **justification**
>
> When want to get an impression of how stable the language feels.
>
> TODO: many times code stops compiling for reasons outside of the
> Rust stability guarantee (e.g., a new warning is introduced and
> the code uses `#![deny(warnings)]`). How can we capture that?

### If your code has ever broken when upgrading to a new **stable** version of the compiler, how difficult was the upgrade?

Select one:

- Very difficult
- Difficult
- Medium difficulty
- Easy enough
- Trivial

### When I upgrade to a new **nightly** version of the compiler...

Select one:

- I am confident my code will continue to compile and be idiomatic.
- I am confident my code will continue to compile but it may be unidiomatic.
- There's a chance my code may no longer compile.
- I am confident my code is likely to break somehow.
- I don't use nightly

> **justification**
>
> When want to get an impression of how stable even the nightly compiler is.
>
> TODO: many times code stops compiling for reasons outside of the
> Rust stability guarantee (e.g., a new warning is introduced and
> the code uses `#![deny(warnings)]`). How can we capture that?

### If your code has ever broken when upgrading to a new **nightly** version of the compiler, how difficult was the upgrade?

Select one:

- Very difficult
- Difficult
- Easy enough
- Trivial
- I don't use nightly

### When I upgrade to a new minor version of a crate...

Select one:

- I am confident my code will continue to compile and be idiomatic.
- I am confident my code will continue to compile but it may be unidiomatic.
- There's a chance my code may no longer compile.
- I am confident my code is likely to break somehow.

> **justification**
>
> When want to get an impression of how stable crates tend to be.

### If you use nightly, why?

Select all that apply:

- I don't use nightly
- Out of habit
- For a particular language feature or set of language features I need
- To help test the nightly version for bugs
- For testing in CI
- A dependency I use requires it
- Other (open response)

> **justification**
>
> We'd like to know what are the common reasons people use nightly
> so that we can better understand where testers are coming from.

### If you use beta, why?

Select all that apply:

- I don't use beta
- Out of habit
- To adopt stabilized language features as early as possible
- To help test the beta version for bugs
- For testing in CI
- Other (open response)

> **justification**
>
> Same justification as the question about nightly but for beta.

### What ways do you install Rust?

Select all that apply:

- rustup
- Linux distribution package
- Homebrew
- Official rust-lang.org tarballs
- Official Windows .msi installers
- Official macOS .pkg installers
- From source
- Other (open response)

### In your opinion, how do you find the following aspects of Rust?

Options:

- Great
- Good enough
- Could be better
- Seriously lacking

Aspects:

- Compile times
- Binary size
- Disk space (e.g., the size of `target` folder)
- The number of internal compiler errors (ICEs)
- IDE experience
- Available tools and support
- Async programming
- GUI development
- Rust language and standard library documentation

### In your opinion, have the following aspects of Rust gotten better or worse over the past year?

Options:

- Much better
- Better  
- Remained the same  
- Worse
- Much Worse
- Unsure

Aspects:

- Compile times
- Binary size
- Disk space (e.g., the size of `target` folders)
- The number of internal compiler errors (ICEs)
- IDE experience
- Available tools and support
- Async programming
- GUI development
- Rust language and standard library documentation


### Please indicate how vital to your workflow each of the following tools are when programming with Rust:

Options:

- Essential
- Somewhat important
- Not important
- I have no experience with this tool

Tools:

- clippy
- cargo
- rustdoc
- rustup
- play.rust-lang.org
- miri
- rustfmt
- bindgen

### Which editor or IDE setup do you use on a regular basis?

Select all the apply:

- VS Code
- vi/vim/neovim
- IntelliJ Rust
- Emacs
- Sublime
- Visual Studio
- Xcode
- Atom
- CLion
- Other (open response)

> **justification**
>
> It is good to know which editor is the most preferred for Rust development. This
> can change investment strategies for further IDE development.
>
> Note: previously this question included different 'drivers' of the Rust IDE
> experience (e.g., racer, rls, rust-analyzer). Development has consolidated on
> rust-analyzer, and so it's not necessary to find out which is being used.
> If we are curious how far along adoption of rust-analyzer is, we can ask that
> in a separate question, though this is likely easier to find out through download
> numbers.


### In which of the following ways have you participated in the Rust community in the last 6 months:

Select all that apply:

- I have produced informational content about Rust (e.g., blogged, live streamed, made a YouTube video, etc.).
- On several occasions I have consumed informational content about Rust (e.g., blogs, live streams, YouTube videos, etc.).
- On several occasions I have read *comments* about Rust content on "news" sites (e.g., Hacker News, reddit.com/r/rust, lobste.rs/t/rust, etc.)
- On several occasions I have *commented* on Rust content on "news" sites (e.g., Hacker News, reddit.com/r/rust, lobste.rs/t/rust, etc.)
- On several occasions I have read official Rust communication channels (e.g., This Week in Rust, the official Rust blog, the Rust Twitter account, etc.)
- On several occasions I have participated in conversations about Rust on social media (Twitter, Facebook, LinkedIn, etc.)
- I have participated in Rust community forums or chats (e.g., users.rust-lang.org, Rust Discord, a local Rust chat community, etc.)
- I have attended a Rust meetup or conference (virtual or in-person).

> **justification**
>
> We'd like to get a picture of _how_ people participate in the Rust community. In
> particular we can use this information to do cohort analysis on highly "active"
> community members in comparison to less active community members.

### Roughly how often do you actively contribute to the Rust project?

Options:

- Comment on, contribute to discussion of, or provide edits to an open RFC
- Create a new thread or comment on internals.rust-lang.org
- Discuss Rust project  in an official chat (either Zulip or Discord)
- Open an issue on any repo in the rust-lang GitHub org
- Contribute code changes (including tests) to the Rust compiler (rust-lang/rust)
- Contribute code changes (including tests) to any other project in the rust-lang GitHub org
- Contribute non-code changes (documentation, comments, etc.) to any project in the rust-lang GitHub org.

Select one:

- Daily
- Weekly
- Monthly
- Less frequently than monthly
- Never but have tried to
- Never and have never tried to

> **justification**
>
> We want to understand the nature of contribution to the Rust project both
> to better understand the shape of community involvement and for cohort analysis.

### How many open-source and non-personal Rust projects do you currently maintain?

Non-personal: at least one other person also contributes and the project is meant for others and not just yourself.
Maintain: you have review and merge privileges

- 0
- 1
- 2-4
- 5-10
- More than 10

> **justification**
>
> We would like to know the rough make up of those who are using Rust in general
> vs those who actively participate in development of open source Rust projects.

### How many open-source and non-personal Rust projects do you currently contribute to (not including those you maintain)?

Non-personal: at least one other person also contributes and the project is meant for others and not just yourself.
Contribute: you regularly provide code, tests, documentation, issues, etc.

- 0
- 1
- 2-4
- 5-10
- More than 10

> **justification**
>
> We would like to know the rough make up of those who are using Rust in general
> vs those who actively participate in development of open source Rust projects.

> **Follow-up: How difficult was it to complete [task]?**
>
> **Justification** Captures not just those who tried and failed, but those who tried and succeeded.
> Shows failure/difficulty rate compared to success rate.
> Also overall engagement / attempted engagement in these ways.

### How welcome do you feel when interacting with the Rust community in the following ways?

- rust-lang GitHub organization
- Rust community GitHub projects
- internals.rust-lang.org, Rust Discord, or Rust Zulip
- users.rust-lang.org, Rust questions on stack overflow
- r/rust
- Other social media (Twitter, Facebook, WeChat, and other sites 'outside' the Rust project, e.g., r/programming, Hacker News)
- Rust conferences
- Local Rust events, e.g., meetups

> **Survey Flow** If they indicated feeling unwelcome above:

### You indicated that you did not feel welcome in the Rust community. Are there any details about your experience that you would like to share with us?

Free form.

## Rust at work

> This section is largely in service of the [contexts](./design/contexts.md) design document.

### Are you using Rust at work?

Select one:

- Yes, for the majority of my coding
- Yes, it's one of a number of languages I use and I use it regularly
- Yes, but I only use it occasionally
- No

> **justification**
>
> We want to establish what percentage of those who could possibly use Rust in a professional setting
> are using Rust in a professional setting. This is most interesting over time. 
> Answers to this question should be combined with whether the respondent has ever used Rust.

### To what extent is Rust currently being used by your company?

Select one:

- My company uses Rust for a large portion of production projects.
- My company uses Rust for a small portion of production projects.
- My company uses Rust only for non-production projects (e.g., tooling).
- My company has actively experimented with Rust
- My company has seriously considered, but not experimented with, using Rust.
- My company has not seriously considered Rust for any use.
- I am unsure whether my company has considered using or currently uses Rust.
- I don't work for a company or my company does not develop software of any kind.

> **justification**
>
> We want to establish how reliant companies are on Rust.

### In what technology domains is Rust used at your company?

Select as many as apply:

- Server-side application
- Desktop application
- Mobile application
- Web application
- Embedded application
- Other (open response)

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

### Approximately how many total developers does your company employ?

- Under 10
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

### Is your company planning on hiring Rust developers in the next year?

Select one:

- Yes
- No
- I don't know or I don't work at company that would hire software developers.

> This question assess hiring sentiment. Although there is intrinsic uncertainty, it is easy to answer and forward looking.
> It will also be interesting to see what the demand for Rust skills from companies is over time.

## Rust in education

> This section is largely in service of the [contexts](./design/contexts.md) design document.

### Have you taken in the past year or are you currently taking a course or training which uses or teaches Rust?

Select one:

- Yes [`NEXT`](#where-is-the-course-or-activity-taught)
- No [`NEXT`](#what-is-your-biggest-worry-for-the-future-of-rust)

> **justification**
>
> This question is primarily used to funnel respondents into the more specific questions about the kinds of educational activities they've been a part of.

### Where is the course or activity taught?

Select one:

- University or other tertiary institute
- High school or secondary school
- Bootcamp or other vocational-focussed educational institute (paid for by you)
- A short training course offered by your employer or a contracted third party (paid for by your employer, not by you or the government)

### Which best describes your course or activity?

- A course teaching exclusively how to program in Rust
- A course teaching how to program in Rust and other languages
- A computer science course (e.g., operating systems, algorithms, etc.) course which uses Rust (and potentially other languages)
- Other type of course where Rust was used

### Is Rust mandated for your course or activity, or did you choose it yourself?

- Rust was mandated
- I choose to use Rust

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
- Other (open response)
- I'm not worried

> Alternative: could rephrase as a 'select all that apply' question
>
> **justification**
>
> Would be useful for leadership to understand the community's fears.

### In your opinion, how easy is it for qualified applicants to find a Rust job?

Select one:

- Very easy
- Easy
- Doable
- Challenging
- Extremely challenging
- I'm not sure

> **justification**
>
> The flip side of the question asking whether the respondent's company plans on hiring Rust developers, we
> want to know how high respondents sense demand for Rust jobs is.

## Demographics

> For methodological purposes, the bulk of the demographics should be at the end of the survey (unless acting as filter/flow questions above)
> They're both easy to complete (beneficial at the end) and somewhat personal (but at this point folks are invested and we've built 'trust')
> Can also be problematic at start if we're asking all easy, personal questions and then get to the harder ones - easy to drop out.

## About you

See [who](./design/who.md).

The following are primarily for cohort analysis, secondarily for understanding the shape of the community.

### Do you consider yourself a member of an underrepresented or marginalized group in technology?

Please share only what you are comfortable sharing. This will help us better serve underrepresented and marginalized groups, better understand how well our outreach efforts are going, and more.

Optional - Select all that apply.

- No
- Yes, but I prefer not to say which
- Cultural beliefs
- Disabled or person with disability (including physical, mental, and other)
- Educational background
- Language
- Lesbian, gay, bisexual, queer or otherwise non-heterosexual
- Non-binary gender
- Older or younger than the average developers I know
- Political beliefs
- Racial or ethnic minority
- Religious beliefs
- Trans
- Woman or perceived as a woman
- Other (open response)

> **FLOW** skip the next question if answered "no"

### Do you feel your belonging to an underrepresented group in technology makes it difficult for you to participate in the Rust community?

Select one:

- Yes
- No
- Maybe

#### If you find it difficult to participate in the Rust community, and feel comfortable giving more details, please tell us what makes it difficult

Free form.

### Are you a full- or part-time student?

Select one:

- yes
- no

> TODO Does it matter in what field? Do we want a follow-up question like in employment?

### Are you employed full- or part-time (including paid internships)?

> Optional

Select one:

- Yes
- No

### If you are employed, which category best describes the domain in which *you* work?

> TODO - server networking, desktop application, mobile application, web application, embedded, etc.

### Do you write or design software in your work?

- Yes, primarily as an individual contributor (i.e., non-manager).
- I primarily manage others who do.
- No

> **FLOW** Only for those who say yes/manage above

### If you write or design software, or manage others who do so, how long have you done so professionally?

Select one:

- <= 5 years
- 5 - 10 years
- 10 - 15 years
- 15 - 20 years
- > 20 years

### Excluding Rust, which programming languages are you experienced with?

Select all that apply:

- Assembly language of any variety
- C or C++
- Java, Go, Objective C, C#, or similar object-oriented language
- Haskell, Lisp, ML, or other functional language
- Scala, Swift, Kotlin, or other modern, strongly-typed language
- Javascript, Ruby, Python, or other dynamically-typed language

> TODO are these the right categories?
> TODO Second questions for each asking level of experience?

### How long have you been programming (in any language, for any reason)?

Select one:

- < 1 year
- < 3 years
- < 5 years
- < 10 year
- > 10 years

### Where do you live?

Select one:

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

### What is your preferred language(s) for technical communication

Select all that apply:

- English
- Chinese
- Hindi
- Spanish
- Russian
- Japanese
- German
- Other (open response)

> TODO other questions to understand the community
> TODO ask community and core team, foundation
> TODO other questions for cohort analysis?
