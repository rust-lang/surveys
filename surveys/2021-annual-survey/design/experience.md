# What is the experience of Rust like?

## The Rust programming experience (compiler, lang, tooling)

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
* Questions which gauge attitudes to potential new features.

Useful for implementers to know where to focus their work and for leadership to be aware of any major problems which need more resources.

The following are questions that have been asked before or may seem relevant but that we do not ask about.

* Do people find the edition experience relatively uneventful?
  * Editions are supposed to be uneventful, and the number of bug reports we get about editions is a better proxy for how well we've achieved that goal.
* Does Rust work well for the platform they are targeting (i.e., the compile target)?
  * New targets for Rust are best asked about in the issue tracker. Using the survey for gathering this information is unlikely to be successful.
* Can people usually find the library their looking for? If not, what domains seemed to be the most underserved?
  * There are so many different domains and different needs within domains that it is extremely difficult to find *actionable* ways to address this question. For example, graphics programming is an extremely large topic. For some, a good wrapper around Skia may be all they need, while others may need much more. Teasing this apart is just too difficult.

## Community experience

Try to understand how inclusive the Rust community is and is perceived to be. We want to know if people feel welcomed or excluded by the community (particularly interesting when analyzed in conjunction with demographic data or participation level). We might ask about specific incidents or experiences to try and get more objective data, though this area is inherently subjective.

Try to understand the level of participation in the community, current, past, and future (intentions). Consider team membership, contributions (PRs (code, tests, docs, ...), filing issues, meetings, triage) to the core project and crates, communication (watch meetings, participate/lurk in forums like Zulip, internals, users, r/rust), attended meetups/conferences, read news, participate in private communities (e.g., Rust interest groups or Slack channels at work). Might want to understand if people would like to participate more or why people participate or don't participate.

Useful for Rust leadership to assist with community building. Potential users to gauge the strength of the community and potential for their participation.

## Learning Rust

Rust has a reputation for being difficult to learn. While it would be useful to know if this reputation is supported by data about users and if this is changing over time, this is often quite hard to find out. There are many confounding factors that make the information not very actionable.