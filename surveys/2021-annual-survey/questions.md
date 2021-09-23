# Survey questions

Whether or not you use Rust Programming Language <https://rust-lang.org> today, we want to hear from you!

The Rust Community Team has created this survey to help us gauge how we're doing, what can be improved, and how we can best engage with all of you as we move forward.

This is your chance to have a say in the development priorities for Rust.

Unless you choose to enter your email, your answers will be anonymous. Any personal data you submit as a part of this survey will be handled in accordance with our policy as described in our Frequently Asked Questions:

https://github.com/rust-community/team/wiki/State-of-the-Rust-Language-Community-Survey-FAQ

We estimate it will take about 10-15 minutes to complete.

> TODOs:
>
> - Improve the data collection policy
> - Ensure that the survey actually takes 10-15 minutes

## Rust Usage

### Do you use Rust?

Select one:

- Yes, I have used Rust [NEXT](#your-rust-experience)
- No, I don't use Rust, but I have in the past [NEXT](#for-previous-rust-users)
- No, I have never used Rust [NEXT](#for-non-rust-users)

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
- Other [open response]

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
- Other [open response]

> **ADDED**
>
> **justification**
>
> Useful in understanding why non-users contribute;

> **SURVEY FLOW**
>
> Skip to `## About You` section

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
>
> **TODO** Given the strong bias in the sample, I'm not sure if this data is actually useful.

### As you have indicated that you have not used Rust, what prompted you to participate in this survey?

Select all that apply:

- I plan to use Rust in the future.
- I consider myself part of the Rust Community.
- Specifically to provide feedback on WHY I do not use Rust.
- Curiosity.
- Other [open response]

> **ADDED**
>
> Useful in understanding why non-users contribute to the survey

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

### How would you rate your Rust expertise?

Select 0-4 (0 = I can't write or read Rust, 1 = I can write simple exercises in Rust, 2 = I can write useful, production-ready code but it is a struggle, 3 = I am productive writing Rust, 4 = I'm an expert)

> **justification**
>
> Useful for cohort analysis, i.e., for other questions we can query if answers are significantly different for beginners vs advanced users.

### How did you get interested in Rust?

Free form.

> **REMOVED**
>
> Not actionable.

### How long have you been working with Rust?

Select one:

> **REMOVED**
>
> While we very much want to understand where someone is in their Rust journey,
> asking in terms of calendar time can give very skewed answers.
>
> **TODO** we should create a question that more appropriately captures how "experienced"
> of a Rustacean the respondent is. This can be difficult to gauge since people with
> different backgrounds will reach different stages of their Rust career at
> different times.
>
> **TODO** There are a few options for this: We can ask how experienced they believe they are;
> how comfortable they are; how productive they feel; how fluent they are.
> Self-report questions like these are probably the most useful here,
> and including more than one will allow us to (potentially) combine them into a multi-item measure (more robust/accurate analysis).

### How long did it take you to become productive in Rust?

Select one:

> **REMOVED**
>
> This is also very prone to wildly different interpretations that make doing something
> with the data very difficult. The goal of this question was likely to get a gauge for
> how difficult the Rust learning curve is, but this question does a very poor job
> capturing that.

### How many other programming languages did you know when you originally started working with Rust?

Select one:

> **REMOVED**
>
> Gauging knowledge through "number of programming languages" and how that relates to
> how easy it is to learn Rust is likely impossible.

### If you summed the size of all Rust projects you work on, how big would it be?

Select one:

- Less than 1,000 lines
- 1,000 to 10,000 lines
- 10,000 to 100,000 lines
- 100,000 to 1,000,000 lines
- more than 1,000,000 lines

> **REMOVED**
>
> This information is not actionable

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
- Other

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
- other [open response]

### On the primary machine you compile Rust code on, how many logical CPU threads do you have?

Please count logical CPUs here, not cores or sockets. To get this number on
Linux, run `nproc`; on macOS, run `sysctl -n hw.ncpu`; on Windows, run
`echo %NUMBER_OF_PROCESSORS%`.

Free form.

### Which operating systems do you develop Rust software for?

Select all that apply:

- *nix (desktop or server)
- Windows
- Mac OS
- iOS
- Android
- embedded platforms (with an operating system)
- embedded platforms (bare metal)
- other

### Which version(s) of Rust do you use for your applications?

Select one:

- Current stable version
- Previous stable version
- Beta release
- Latest nightly
- A specific version of nightly
- Custom fork
- I don't know
- Other

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

Select one:

- I don't use nightly
- Out of habit
- For a particular language feature or set of language features I need
- A dependency I use requires it

> TODO look at other common answers from previous surveys

### What ways do you install Rust?

Select all that apply:

- rustup
- Linux distribution package
- Homebrew
- Official rust-lang.org tarballs
- Official Windows .msi installers
- Official macOS .pkg installers
- From source
- Other

### If you don't use rustup, why not?

Select all that apply:

- I'm prefer using my platform's package installer (yum, apt-get, homebrew, msi installer, etc.)
- I don't trust that rustup provides secure binaries
- I didn't know about it
- The network I'm on does not allow for it (e.g., firewall)
- I tried, but it didn't work
- Other

> TODO: a lot of people previously reported that they *use* rustup but wish they didn't. How can we capture that here?
> TODO: this was previously free form. Do we prefer the multiple choice?

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
- The size of `target` folder
- The number of internal compiler errors (ICEs)

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

- VS Code with the rust-analyzer extension
- VS Code with the rust extension (a.k.a rls)
- VS Code without an extension for Rust
- vim or neovim with rust-analyzer
- vim or neovim with rls
- vim or neovim without specific Rust support (beyond synatx highlighting)
- IntelliJ Rust
- Emacs
- Sublime
- Visual Studio
- Xcode
- Atom
- CLion
- Nano or Pico
- Other

> TODO: do we need to provide racer as an option here?

### How would you rate Rust's IDE or editor experience?

Select one:

- World class!
- Great
- Good enough
- Could be better
- Terrible

> TODO: how can we relate this back to other languages? Presumably C# devs might find Rust's editor experience poor but Ruby devs might like it

### For each of the challenges listed below, please indicate whether you believe there has been any change within the last year

Options:

- Got worse
- No change
- Slight improvement
- Some improvement
- A lot of improvement
- I'm not sure

Challenges:

- Library support
- IDE experience
- Adoption level of Rust
- Available tools and support
- Stable language features and crates
- Async programming options
- GUI development
- Rust language documentation
- Compile times

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
> 
> TODO possibly multiple questions for past month, past year, ever, + would you like to do
> POSSIBLE Approach below:

> **Survey Flow Example** Following question would only appear if indicated "I have read the Rust blog."

### Previously you indicated that you read the Rust blog. How often do you do so?

- [frequency options]

> **Survey Flow Example** Following question would only appear if indicated "I have not read the Rust blog."

### Previously you indicated that you do not read the Rust blog. Why not?

- I see no benefit
- I don't have the time to do so
- [Other options]

### Have you completed or tried to complete any of the following?

- GitHub issue (Rust)
- GitHub PR (Rust)
- Discuss an RFC
- Write an RFC
- Discuss Rust on GH rust-lang org/Zulip/internals/Discord
- Publish a crate

> **Follow-up: How difficult was it to complete [task]?**
>
> **Justification** Captures not just those who tried and failed, but those who tried and succeeded.
> Shows failure/difficulty rate compared to success rate.
> Also overall engagement / attempted engagement in these ways.
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
> **Survey Flow** If they indicated feeling unwelcome above:
> ###You indicated that you did not feel welcome in the Rust community. Are there any details about your experience that you would like to share with us?
>
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
> TODO Should there be something spcifically separating an online bootcamp/automated course from one taught by a person?

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
> - upgrades breaking code (41, 42 from 2020)
> - what is missing from the ecosystem (44 from 2020)
> - do respondents consider Rust to be an employable skill (from contexts.md)
> - Perception of Rust's learning curve? Do people feel like Rust's learning curve is worth it? (from experience.md)

## Demographics

> For methodological purposes, the bulk of the demographics should be at the end of the survey (unless acting as filter/flow questions above)
> They're both easy to complete (beneficial at the end) and somewhat personal (but at this point folks are invested and we've built 'trust')
> Can also be problematic at start if we're asking all easy, personal questions and then get to the harder ones - easy to drop out.

## About you

See [who](./design/who.md).

The following are primarily for cohort analysis, secondarily for understanding the shape of the community.

### Do you consider yourself a member of an underrepresented group in technology?

Optional - Select all that apply. Please share only what you are comfortable sharing. This will help us understand how well our outreach efforts are going.

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
- Others

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

- yes, in tech
- yes, in finance
- yes, in government
- yes, in education
- yes, other
- no

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
- Other

> TODO other questions to understand the community
> TODO ask community and core team, foundation
> TODO other questions for cohort analysis?
