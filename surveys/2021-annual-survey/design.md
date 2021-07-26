# Rust Survey 2021 High-Level Questions

The following are questions we'd like to get answers to from the Rust 2021 survey *data*. While we may ask some of the questions directly to survey takers, the majority are not meant to be asked directly and will only be inferred through the answers to other questions.

##  Trends

It is important to watch year to year trends, so we must make sure that we have compatibility with previous years' questions.

## Demographics 

While demographic information can be interesting on its own, it's even more interesting when used as a basis for cohort analysis.

* Uses Rust (vs never has or has since stopped)
* Location
* Identifies as being part of an underrepresented group in tech
* Preferred language (for communication about technology).
* Programming language background
    * Experience with other languages, paradigms, etc.
* Profession
* Industry 
* Programming stack

**Possible Others:**: age, educational background, systems programming background

## Non-Users

* Why are they filling out this survey? We'd like to better understand what type of sample of non-users we're getting.
* For non-users, we'd really like to better understand why don't use Rust or have stopped using the language.
   * Is there something that they perceive about Rust that's preventing them from using the language?

## Learning Rust

* How much effort do people need to put in to feel comfortable using Rust to solve a problem?
    * Note: we should avoid phrasing this in terms of calendar time since people learn at different paces.
* How much easier is it for a certain programmers to learn Rust vs others:
    * C or C++ programmers vs others
    * Experienced vs inexperienced programmers
    * Programmers who know more modern languages (e.g., Swift) vs those who only know older languages (e.g., Java)
    * Programmers who know lots of languages vs those who only know 1
* Do they feel that the effort is worth it?
* What stands in their way from reaching a higher level of proficiency in the language?
* How many people who have recently learned Rust (last 6 months?) found Rust too difficult to learn?
* Which elements of Rust make it the hardest to learn?
* Which resources helped learners the most?

## Improving the language

* Which language would you most likely want to interop with Rust?
* What are people's frustrations with language, std.
* What problems are you hitting? What problems haven't been solved yet?

## Stability

* How often does updating a compiler break people's code? How easy are breaking changes to deal with?
    * Care should be taken here to address how this changes if the user is using nightly vs stable.
* How stable are people's dependencies?
    * We should not ask this in terms of number of 1.0 dependencies but rather how people perceive the stability of the dependencies they use.
    
## Using Rust

* How long have people been using Rust?
    * We will want to qualify this perhaps ("as the main or one of the main programming languages you use").
* How regularly do you use Rust?
    * Previously this was phrased in terms of time, but we might want to ask in relation to other languages the programmer uses: e.g., "more than any other language", "one of the top languages", etc.
* Do users use any of the following specific kinds of coding? How often?
    - Unsafe Rust
    - Async Rust
    - ...
* What kind of development do you do?
    - OSs
    - Network
    - Games
    - User-facing Apps (GUI or console)
    - Mobile apps
    - Libraries supporting other users
    - Compilers
    - DBMS
    - Other embedded
    - ...
    
## Rust at school

* Are students using Rust in their courses (if such a thing would make sense).

## Rust at work

We'll want to ensure we're only asking those for whom using a programming language at work even makes sense (i.e., they work in software).

* What percentage of people are using Rust at work?
* If not using Rust a work, what is preventing it's adoption? Or if it is used, preventing it being used in more places?
    * Rust was too intimidating, too hard to learn, or too complicated
        * Which parts?
    * Rust didn’t have the libraries I needed
        * Which ones?
    * Rust didn’t have the tools I need
        * Which ones?
    * Rust didn’t have good IDE support
    * Rust seemed too risky to use in production
        * Why?
    * I needed better interoperability between Rust and other languages.
        * Which ones?
* Is Rust seeing increased adoption at people's places of work? 
    * If so, in what areas?
        * domains
        * main product vs experiment vs non-production tooling
* Is the idea of Rust adoption at work become more plausible over time?
    * For those in professional technical leadership roles, how confident do they feel in Rust as a technology to build their business on?
* How hard is it to find a Rust related job if one wants to?
* How much of people's work is in Rust?
    * We both want to know how large Rust projects at work are and what percentage of time people spend using Rust.

## Rust compiler 

* What is the difference between which version of the compiler people use and which version they wish they were using (e.g., are some nightly users wishing they could just use stable?)
* If people are using nightly, why?
    * Do all users even have a reason?
* How many users test out beta themselves?
* How many users run beta or nightly compilers as part of CI validation?
* How do users hear about new versions of Rust and how quickly do they upgrade to them? 
* Compile times:
    * Have compile times improved?
    * How long does your most complex project take to compile from scratch?
        * Do you use incremental compilation? If so, how long does this take?
    * Do compile times lead to a perceived drop in productivity?
    * How easy is it to improve particularly bad compile times?
    * Are bad compile times usually the case in large codebases or also in small ones?
* Which edition are people using?
    * For those who have transitioned editions, how difficult was it?
    * If something went wrong, how long did it take to fix the issue?
    

## Core tooling (cargo, rustdoc, etc.)

* How often does each core tool break when upgraded?
* Do you need to use nightly for any features of core tools? If so, which ones?
* How aware are they of the documentation for these tools? (e.g., doc.rust-lang.org/rustdoc)
* Where do people get their tooling from? (rustup, tarballs, distro package, etc.)


## Other Tools

* Which editors/IDEs do people prefer to use
    * For those using a plugable text editor, which language server engine are they using (racer, RLS, rust-analyzer?)
    * How happy are people with their experience? (Same question for core tools and compiler)
    * What are some areas which need the most improvement?
    * Which features do you have when working with other languages do you miss?
* Which tools do you use? How often? (Tools include crates.io, rustdoc, Rustfmt, Clippy, ...)

## Platform Support

* What platforms are people using to develop (i.e., dev machine) Rust?
    * Specifics: non-Windows 10, macOS m1 vs intel, docker vs native. We likely don't need to be too specific (e.g., Windows 7 vs 8 doesn't really matter)
* How often are devs cross-compiling vs compiling for the host machine?
    * How are they achieving this? Local machine, CI run, docker, etc?
* Which targets are devs compiling for? 
    * We should make sure this is very clearly distinct from the question above as it has caused confusion in the past. 

## New policies 

* The compiler team would like to gauge community perception on an **opt-in** mechanism for users of the Rust compiler to optionally send information to the compiler team on certain compiler health metrics such as number of ICEs (internal compiler errors).
    * **IMPORTANT**: There is concern that merely asking a question like this could cause sufficient commotion within the community. We want to be sensitive to this, and ensure that no data will be collected without explicit user consent.
    * Re: ICEs, we could try figuring out if and how (or how often) people report ICEs
    
## Library support

* How often do people not find a library they need for a project?
* What domains is it particularly difficult to find good libraries for?
* Which libraries are missing?

## Conferences

* Preference of online, in-person, or mixed
* If in conference is in-person, where would you prefer to travel?

## Open source 

* How many people contribute to open source Rust projects and at what level?

## Participation

* How do users participate in the community? Do they participate at all? Do they attend real/virtual meetups, conferences. Use internals.r-l.o, users.r-l.o, Discord, Zulip, twitter, r/rust, read TWiR, ...
* What blocks people from participating in the community or participating more (e.g., contributing to the project)


## The future

* What do you perceive as the biggest opportunity for Rust in the next year?
* What is most likely to prevent you from using Rust in the future? 
    * We want to gauge threats to Rust's future without requiring respondents to predict what is threatening the ecosystem in general.
    
## Rust news

* How do people stay informed about what is happening in the Rust community?
* Do people feel like they are able to keep as up-to-date as they would like to?
    * If not, what are some things that are hard to keep track of?

## Inclusivity

* How welcoming does the Rust community feel to those underrepresented in tech?
* What are some ways the Rust community feels less welcoming or easy to be a part of than other language communities?
* If you do not have a background in low-level programming (perhaps in C or C++), how much does this impact how welcome or confident you feel in the Rust community?