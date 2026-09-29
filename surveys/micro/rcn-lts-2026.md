# Survey questions

The goal of this survey is to gauge expectations around a potential first-party Rust LTS offering. The results will help inform a potential initiative if the demand is there.

## Background

### In what capacity do you currently use Rust Stable?

Type: select all that apply

- Unpaid open source
- Sponsored open source
- Employed open source
- Contracted proprietary
- Employed proprietary
- Other (open response)

> **justification**
We want to be able to understand how LTS expectations differ depending on the domains Rust is used in.

### In what capacity would you use Rust LTS instead of Rust Stable?

Type: select all that apply

- Unpaid open source
- Sponsored open source
- Employed open source
- Contracted proprietary
- Employed proprietary
- Other (open response)

> **justification**
We want to be able to understand how LTS expectations differ depending on the domains Rust is used in.

## Defining Rust LTS

### In your opinion, what is the purpose of using Rust LTS instead of Rust Stable?

Rust Stable today offers a very strong stability guarantees, and will be supported by the Rust Project indefinitely. What makes Rust LTS different from Rust Stable that would bring someone to choose Rust LTS?

[api-evolution]: https://rust-lang.github.io/rfcs/1105-api-evolution.html

Type: free form

> **justification**
This is the "what is 'Rust LTS'" question.

### How important are these potential properties of Rust LTS?

Type: matrix

Properties:

- Rust LTS is provided by the Rust Project
- Rust LTS vendors are vetted by the Rust Project
- Rust LTS is discoverable from the rust-lang.org website
- Rust LTS is available through Rustup
- Rust LTS is available without building it from source
- Rust LTS has strongly defined and documented end-of-life dates
- Rust LTS supports all the targets Rust Stable does
- LTS updates do not introduce new unstable language features
- LTS updates do not stabilize existing unstable language features
- LTS updates do not introduce new unstable stdlib API
- LTS updates do not stabilize existing unstable stdlib API
- LTS updates do not refactor compiler implementation details
- LTS updates do not refactor stdlib implementation details
- LTS updates do not change Rust binary artifact compatibility
- LTS updates do not change the observed behavior of code with Undefined Behavior
- LTS updates do not change the host tools' system requirements
- LTS updates do not change the runtime's system requirements
- LTS receives fixes for impactful issues with assigned CVEs
- LTS receives fixes for impactful issues without assigned CVEs
- LTS receives fixes for known soundness holes in the language
- LTS receives performance improvements
- Ecosystem library updates do not require newer Rust than LTS

Importance:

- Undesirable
- Immaterial
- Desirable
- Mandatory

> **justification**
This objectively measures some of what goes into answering the previous question, based on properties people have suggested LTS should have in the past. Some properties are incompatible.

### How long do you expect a Rust LTS release to receive support?

**Please specify units in your answer.**

Type: free form

> **justification**
This is the second of the two main LTS axes; we want to gauge the expectation of how long LTS users expect to be able to stay on one LTS release before being *required* to upgrade. We deliberately do not say what units to respond in to avoid priming. Note that both the absolute support duration and the ratio to release frequency are both meaningful insights.

### How often do you expect a new Rust LTS release?

A "new release" means a new 1.X version. There is a new Rust Stable 1.X release version every six weeks.

**Please specify units in your answer.**

Type: free form

> **justification**
This is the first of the two main LTS axes; we want to gauge the expectation of how frequently LTS users expect an LTS update to be available. We deliberately do not say what units to respond in to avoid priming.

### What components do you expect support for as part of Rust LTS?

If you don't recognize a component by name, leave it unselected.

Type: select all that apply

- cargo
- cc
- clippy
- libc
- libm
- llvm-tools
- log
- miri
- rand
- regex
- rust-analyzer
- rust-std
- rustc
- rustfmt
- rustup
- syn
- Other (open response)

> **justification**
What "Rust LTS" means in terms of support burden isn't obvious; is it "security patches and critical bug fixes" for the compiler, the standard library, and/or the rest of the toolchain? Do some people expect it to cover "extended batteries" from crates outside std? The straightforward answer would be extending whatever support we give the stable toolchain on whichever targets we provide LTS for. We want to gauge if this matches prospective LTS user expectations.

## Funding Rust LTS

### How much do you expect to pay for Rust LTS as you defined it?

**Please specify currency/units in your answer.**

Type: free form

> **justification**
Enterprise users should be paying for that extended support. We avoid specifying units like "USD/user/month" or "USD/release" or "USD/project/year" to avoid priming expectations, even though this risks unitless answers.

### How much would you expect to pay for extended Rust LTS support durations?

**Please specify currency/units in your answer.**

Type: free form (optional)

> **justification**
A lot of LTS schemes have baseline support and then extended support for an additional cost. This question covers that scenario. (Units deliberately unspecified at risk of unitless answers.)

### How much would you expect to pay for extended Rust LTS support coverage of select ecosystem crates from crates.io?

**Please specify currency/units in your answer.**

Type: free form (optional)

> **justification**
Rust's standard library is deliberately minimal, so "batteries" from the ecosystem are required for most applications. It would be great if there were a way to broker ecosystem LTS through the Rust Project; the biggest contributor to the funding problem in OSS is connecting users who want to throw money at the problem to the maintainers in a way that satisfies administrative expectations. (Units deliberately unspecified at risk of unitless answers.)

## Feedback

### Is there anything else you would like us to know?

We appreciate your time filling out this survey. Thank you!

Type: free form (optional)
