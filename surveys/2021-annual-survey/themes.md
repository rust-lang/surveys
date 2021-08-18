## NOTE: This file is a scratchpad for ideas and will be removed soon
# Themes

## Who is using Rust?

* Demographic information: 
  * We aim to collect demographic information such that we can group survey takers into various cohorts which we can perform corhort analysis comparing how different cohorts differ. The cohorts should include:
     * Current user of Rust, former user of Rust, non-user of Rust
     * Types of programming languages used (i.e., extensive and current use of a programming language that fits into a given category):
       * Systems programming (C, C++) 
       * Strongly typed "modern" language (Haskell, Scala, Swift, Kotlin, etc.)
       * OO Languages (Java, Objective-C, C#)
       * "Scripting" languages (Ruby, JavaScript, Python)
     * Identifies with an underrepresented group in technology 
     * Industry (e.g., general software, banking, transportation, etc.)
     * Current stack (server networking, desktop application, mobile application, web application, embedded, etc.)
  * Other demographic information can be collected just to better understand the shape of Rust community:
    * Location
    * Preferred human language for technical communication 

## Where and how Rust is used

* Rust in Education
  * Is Rust being used in education? 
  * Is such usage growing over time? 
  * What type of courses or educational activities are using Rust?
* Rust at Work
  * Is usage of Rust at work growing?
  * What type of workloads are using Rust? (internal tooling, customer facing applications, etc.)
  * How reliant are companies on Rust (i.e., if Rust were to disappear, how impactful would that be on businesses?)
  * What prevents adoption of Rust at work?
* Rust as an employable skill
  * How hard is it to find a job in Rust? Does this change over time?
  * How valuable are Rust skills in the job market?
* Domains
  * What types of domains is Rust being used? (This is distinct from tech stack and even industry)
	* Examples: aviation, logistics, cloud computing infrastructure, scientific computing, etc.

## Why is Rust being used?

* Reasons for using Rust
  * Why did developers pick Rust over another language?

## The Rust programming experience (compiler, lang, core tooling)

"Core tooling" is a bit hard to define since what's really meant is core tooling from the user's perspective. This obviously changes from user to user. While basically everyone would agree cargo is a core tool (probably even the small subset of users who don't use it!), would everyone agree that clippy is a core tool? Clippy is indispensible for a group of users while many others don't use it.

* Stability of the language
  * Do people feel that their code is being broken?
  * How often and what is the severity of this breakage?
  * In general, do people feel like Rust's stability guarantees are upheld?
* The Rust compiler as a productive tool
  * Is the perception of {compile times, binary size, artifact disk space (i.e., the target folder)} getting better or worse over time?
* What are "core tools" for users (i.e., they are an indispensible part of the Rust programming experience?)
* How reliable is the core tooling and how happy are people in general with the user experience?
* How often do people *need* to reach for nightly for the compiler or core tooling?
* Do people find the edition experience relatively uneventful?
* Does Rust work well for the platform they are targeting (i.e., the compile target)?

## The Rust programming experience (third party tools and libraries)

Third party tooling is essentially everything not encompassed by "core tooling"

* How is the IDE experience with Rust?
* Can people usually find the library their looking for? If not, what domains seemed to be the most underserved?

## Other 

* Non-Users
  * We want to better understand the perspective of non-users of Rust. 
  * Questions: this group is very unlikely to be representative of the entire population of Rust. What can we learn from them?
* Learning Rust 
  * How does the perception of Rust's learning curve change over time?
  * Do people feel like Rust's learning curve is worth it?
  * Questions: while it's _interesting_ to learn about people's perceptions of how difficult it is to learn Rust or certain parts of Rust, how actionable is this information?
* Improving the language
  * Question: we have open lines for communication with users for feature requests and improvements. The survey is unlikely to be a productive place to gather feedback on what users want out of the language. Perhaps the best thing to ask is if users feel their opinions and desires are listened to and acted up. 

## Metadata

* Can we de-bias responses?
  - Non-users section
  - Can we estimate population info from survey?
* Data for cohort analysis (Users)

## Users

Who are Rust users? How many? Demographic info. Experience, history, etc.

* Demographics
* Using Rust
* Open source
* Participation
* conferences
* Rust news

## Usage

What is Rust used for? Where is it used? How is it used?

* Rust at work
* Rust at school
* Platform support
* Library support

## Experience

What experience do users have with Rust? What is good/bad, or strong/weak?

* Learning Rust
* Improving the language
* Stability
* Compiler and tools sections
* Non-users

### Perceptions

More subjective end of the experience spectrum

* The future

## Community experience

Similar to experience theme, but specifically the community rather than the software 'product'.

* Inclusivity
* Participation


# By audience

For most of these questions, want to know change year on year as well as absolute values.

## Implementers

* What should be worked on?
  - What are people's blockers?
  - Sources of friction?
  - Popularity of platforms/domains/tools/etc.
* Is work that has been done having a positive impact?

## Potential users

Individuals or decision makers. Primary purpose of survey is supplying evidence

* Is Rust mature? (I.e., are there many users in a particular domain/organisational context/etc)
* Are Rust users happy?
* Are Rust users being successful?
* What problems/risks should one be aware of?

## Rust leadership

* Understand composition of user base and potential users
* Are we attracting and retaining users?
* Is effort expended leading to success?
* Are resources being correctly allocated?
* Are our assumptions correct? (Are there scenarios or groups of (potential) users that are underserved?)
* Is the community meeting its goals?
  - Are people able to participate?
  - Are there biases relative to all users/wider industry/global population?

## Sponsors

Evidence that Rust is a project worth being involved with

* Number of users and demographic info.
* How is Rust being used?
