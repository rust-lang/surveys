# Survey questions

## About you

See [who](./design/who.md).

The following are primarily for cohort analysis, secondarily for understanding the shape of the community.

Are you a Rust user

- I have used for Rust for any reason in the past three months
- I have used Rust in the past, but not in the past three months
- I have never used Rust

TODO is three months the right amount of time
TODO move to section about Rust?

Do you identify with an underrepresented group in the technology industry?

- yes
- no
- I prefer not to say (could just be an optional question)

TODO should we ask which group? 

Are you a full- or part-time student?

- yes
- no

Are you employed in full- or part-time work (including paid internships)?

- yes, in tech
- yes, in finance
- yes, in government
- yes, in education
- yes, other
- no

If you are work, which category best describes the domain in which *you* work?

- server networking, desktop application, mobile application, web application, embedded, etc.

TODO categories

Do you write or design software in your work?

- yes, primarily as an IC
- I primarily manage others who do
- no

If you write or design software, or manage others who do so, how long have you done so professionally?

- <= 5 years
- <= 10 years
- <= 15 years
- <= 20 years
- > 20 years

Excluding Rust, which programming languages are you experienced with (TODO define level of experience)

- Assembly language of any variety
- C or C++
- Java, Go, Objective C, C#, or similar object-oriented language
- Haskell, Lisp, ML, or other functional language
- Scala, Swift, Kotlin, or other modern, strongly-typed language
- Javascript, Ruby, Python, or other dynamically-typed language

TODO are these the right categories?

How long have you been programming (in any language, for fun, learning, work, any reason)?

- < 1 year
- < 3 years
- < 5 years
- < 10 year
- > 10 years


Which operating systems do you use regularly for software development (not just Rust)?

- *nix
- Windows
- Mac OS
- other

Which operating systems do you develop software for?

- *nix (desktop or server)
- Windows
- Mac OS
- embedded platforms
- other

TODO should we ask if people develop for cross-platform vs a specific platform?


Where do you live?

- North America
- Central America
- South America
- Europe
- Middle East
- Africa
- West, central, or south Asia
- east or south-east Asia
- Australasia or the pacific

TODO are these the categories we care about? Do we want to separate China from east asia given the distinct communities?

Level of English (select all which apply)

- Can have a technical conversation
- Can understand most technical documentation
- Can understand a technical talk (e.g., at a conference or meetup)
- Some everyday English

What is your preferred language for technical communication

- English
- Chinese
- Hindi
- Spanish
- Russian
- Japanese
- Other

TODO other questions to understand the community
  - ask community and core team, foundation
TODO other questions for cohort analysis?

## Your Rust experience

Which operating systems do you use regularly for Rust development?

- *nix
- Windows
- Mac OS
- other

Which operating systems do you develop Rust software for?

- *nix (desktop or server)
- Windows
- Mac OS
- embedded platforms
- other

TODO should we ask if people develop for cross-platform vs a specific platform?

Which tools do you use (at least once per month), either directly or in CI when doing Rust development

- an IDE or editor with plugin doing more than syntax highlighting
- debugger
- println debugging
- profiler
- clippy
- rustfmt
- Cargo
- Rustup (TODO regualar updates vs advanced use like switching channels?)
- code coverage
- rustdoc


TODO lots more in this section:

* Stability of the language
  * Do people feel that their code is being broken?
  * How often and what is the severity of this breakage?
  * In general, do people feel like Rust's stability guarantees are upheld?
  * How often do people *need* to reach for nightly for the compiler or core tooling?
* The Rust compiler as a productive tool
  * Is the perception of {compile times, binary size, artifact disk space (i.e., the target folder)} getting better or worse over time?
* What are "core tools" for users (i.e., they are an indispensable part of the Rust programming experience?)
* How is the IDE experience with Rust?
* How reliable is tooling and how happy are people in general with the user experience?
* Do people find the edition experience relatively uneventful?
* Does Rust work well for the platform they are targeting (i.e., the compile target)?
* Can people usually find the library their looking for? If not, what domains seemed to be the most underserved?
* Questions which gauge attitudes to potential new features.


Which of the following apply to you (TODO possibly multiple questions for past month, past year, ever, + would you like to do ):

- I have contributed (in any way) to a crate published on crates.io TODO separate issues from PRs/other productive stuff?
- I am maintainer of a Rust project outside of the core project
- I have contributed (in any way) to a core Rust project (part of the rust-lang GH org)
- I'm a member of a Rust team or WG
- I've read the Rust blog
- I've read TWiR
- I've read GH rust-lang org/Zulip/Discord/internals/users/r/rust (separate answers or one answer?)
- I've written a comment/post on GH rust-lang org/Zulip/Discord/internals/users/r/rust (separate answers or one answer?)
- Attended a meetup (including virtual)
- participated in a private Rust community (e.g., work Slack, private messages)

Have you tried but failed to complete any of the following?

- GH issue (Rust)
- GH PR (Rust)
- discuss an RFC
- write an RFC
- discuss Rust on GH rust-lang org/Zulip/internals/Discord
- publish a crate

How welcome do you feel when interacting with the Rust community in the following ways? (1/2/3/NA?) TODO in the last year

- other social media (twitter, facebook, other sites 'outside' core Rust, e.g., r/programming, HN - TODO one or two answers)
- rust-lang GH
- other GH Rust project
- Zulip/internals/Discord
- users/stack overflow
- r/rust
- Rust conferences
- Local Rust events, e.g., meetups

TODO anything more objective like asking about particular incidents or kinds of incidents?
TODO ask about blockers for participation?

## Rust at work

TODO see previous surveys

Are you using Rust at work

- yes, >90% of my coding
- yes, it's one of a number of languages I use and I use it regularly
- yes, but I only use it occasionally
- no, but it is likely in the future
- no

Is Rust used in the company where you work?

- yes by > 100 devs
- yes < 100
- yes < 50
- yes < 20
- yes < 10
- yes < 5

How reliant on Rust is your company?

- It's the companies main language tech
- It's a large part
- It's a small part
- We're experimenting
- No use

And/or

- Used in production across multiple projects
- Used in production
- Being actively developed
- Experimented with
- Being considered

In what domains is Rust used at your company

- server networking, desktop application, mobile application, web application, embedded, etc.



## Rust in education

Are you taking a course which uses or teaches Rust, or have you in the past year, or are you enrolled for one in the coming year?

Where is the course or activity taught?

- University or other tertiary institute
- Bootcamp or other vocational-focussed educational institute
- A short training course offered by your employer or a contracted third party

TODO are the latter two sufficiently differentiated?

Which best describes your course or activity?

- A programming course which only teaches Rust
- A programming course which teaches Rust amongst other languages
- An operating systems course which uses Rust with or without other languages
- Other course which uses Rust
- Individual project
- Group project
- Other activity

Is Rust mandated for your course or activity, or did you choose it yourself?

- Compulsory
- Optional (but suggested in some way)
- Optional (completely driven by you)


## Challenges and feedback

### What do you feel are the biggest challenges or problems for the Rust project? What could we do to improve adoption?

Free form

> **REMOVED**
>
> Vague, not useful

### What new things related to the Rust project are you most excited about in 20XX?

Free form

> **REMOVED**
>
> Vague, not useful

### Anything else you'd like to tell us?

Free form

> **REMOVED**
>
> Vague, not useful

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


