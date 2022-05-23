# Survey questions
One of the [compiler team's focuses for
2022](https://blog.rust-lang.org/inside-rust/2022/02/22/compiler-team-ambitions-2022.html)
is to improve the experience of debugging Rust code. We'd like to better
understand your experiences when debugging Rust - what's been good, what's been
bad and how your experience debugging Rust could be better.

Any personal data you submit as a part of this survey will be handled in
accordance with our policy:

https://github.com/rust-lang/surveys/blob/main/documents/data-sharing-annual-community-survey.md

We estimate it will take about ? minutes to complete.

## General demographics

### Which operating systems do you use regularly for Rust debugging?
Note: this is specifically about which operating systems you debug Rust on

Type: select all that apply (optional)

- Linux
- Windows
- Windows Subsystem for Linux
- Mac OS
- Embedded devices
- Other (open response)

> *Justification:* Cohort analysis
>
> Debuggers are often platform-specific and various improvements that the
> compiler team could make could only benefit a subset of all platforms, so
> knowing what users are using is valuable.

### How would you rate your Rust expertise?
Type: select one

- I am a beginning Rust user
- I am a intermediate Rust user
- I am a advanced Rust user

> *Justification:* Cohort analysis
>
> Users with different levels of experience are likely to face different
> challenges.

## General debugging experience

### What forms of debugging do you typically use with Rust?
Type: select all that apply

- `println!`/`log`/`tracing`/`dbg!`
- Stack traces (printed by `panic!()`/`backtrace-rs`)
- Traditional stepping debuggers (gdb/lldb/WinDbg/Visual Studio)
- Record/replay debuggers (rr/WinDbg or Visual Studio with Time Travel Debugging)
- High-level tracing (`dtrace`/`ebpf`/`ETW`)

> *Justification:*
>
> Understand how users are debugging Rust code.

### What uses of Rust are you debugging?
Type: select all that apply (optional)

- Single-threaded application
- Multi-threaded application
- Rust applications using `async`/`await` or futures
- Pure Rust application
- Mixed Rust and other language application
- Crash dumps
- Cloud/server-side application
- Embedded hardware
- WebAssembly

> *Justification:*
>
> Some debugger use cases are very different from "standard" debugging.

### Do you debug Rust remotely?
i.e. are you debugging something that's running on an another computer (where
you are connecting to that remote machine where the debugger and executable are
running, or the debugger is running locally but the executable is on a remote
machine)

Type: select all that apply

- Yes, debugger on the host (e.g. `gdbserver` or wired connection to embedded device)
- Yes, debugger on the device (e.g. an SSH session with a debugger running)
- No

> *Justification:*
>
> Remote debugging will have a different user experience that might be better
> or worse.

### What tasks do you use a debugger for?
Type: select all that apply

- Fixing a crash/panic/access violation
- Fixing a logic bug
- Fixing a misbehaving program
- Investigating a crash dump
- Learning how a well-behaving program works
- Profiling
- Understand a third-party library's behaviour

> *Justification:*
>
> Different motivations for debugging will benefit from different features from
> debuggers and might have a better or worse experience.

## Debugging other languages

### How would you rate your expertise with debuggers (with other programming languages)?
Type: select one

- I have never used a debugger
- I am uncomfortable using a debugger [`NEXT`](#why-are-you-uncomfortable-using-a-debugger-with-other-programming-languages)
- I am comfortable using a debugger

> *Justification:*
>
> Users who are more familiar with debuggers will face different problems than
> users who are not.

### Why are you uncomfortable using a debugger (with other programming languages)?
Type: select all that apply

- Unfamiliar (i.e. I don't know how to use a debugger)
- Reliability (i.e. Don't expect debugger to work well enough)
- Ease-of-use (i.e. I know how to use a debugger but it is too difficult)
- Lack of documentation with Rust

> *Justification:*
>
> Why aren't users comfortable with debuggers is useful.

### Do you often use a debugger with other programming languages (anything but Rust)?
Type: select one

- Daily or nearly so
- Weekly or nearly so
- Monthly or nearly so
- Rarely

> *Justification:*
>
> If a user regularly uses a debugger for other languages but not for Rust then
> it would be interesting to know that.

### Which programming language(s) do you regularly use a debugger with?
Type: select all that apply

- C
- C++
- Java
- JavaScript
- Python
- Go
- C#
- Other

> *Justification:*
>
> Debugging experiences vary widely by language - debugging a interpreted
> language like Python is very different from a compiled language like C/C++ -
> this will inform user expectations with Rust debuggers.

### How does debugging in language X compare to Rust?
Type: freeform text

> *Justification:*
>
> What can Rust's debugging experience learn from other languages.

## Debugging Rust

### How would you rate your expertise with debuggers (with Rust)?
Type: select one

- I have never used a debugger
- I am uncomfortable using a debugger [`NEXT`](#why-are-you-uncomfortable-using-a-debugger-with-rust)
- I am comfortable using a debugger
- I am very comfortable using a debugger

> *Justification:*
>
> Users who are more familiar with debuggers will face different problems than
> users who are not.

### Why are you uncomfortable using a debugger (with Rust)?
Type: select all that apply

- Unfamiliar (i.e. I don't know how to use a debugger)
- Reliability (i.e. Don't expect debugger to work well enough)
- Ease-of-use (i.e. I know how to use a debugger but it is too difficult)
- Lack of documentation with Rust

> *Justification:*
>
> Why aren't users comfortable with debuggers is useful.

### How do you start a debugger (when debugging Rust)?
Type: select all that apply

- Core dumps
- Attaching to a process
- Launching executable
- From an IDE

> *Justification:*
>
> User experience for starting a debugger in either of these ways could be
> improved if they were particularly common or uncommon.

### What debuggers do you use with Rust?
Type: select all that apply

- `gdb`
- `lldb`
- Visual Studio
- WinDbg
- `rr`
- Other

> *Justification:*
>
> Debuggers that are actually used is useful.

### What debuggers have you heard of?
Type: select all that apply

- `gdb`
- `lldb`
- Visual Studio
- WinDBG
- `rr`
- Other

> *Justification:*
>
> If users aren't aware of certain types of debugger than raising awareness or
> making it easier to start these debuggers might be valuable.

### Do you often use a debugger with Rust?
Type: select one

- Daily or nearly so
- Weekly or nearly so
- Monthly or nearly so
- Rarely

> *Justification:*
>
> Knowing how often a debugger is used with Rust is valuable, but need to know
> whether that is because of the quality of the experience or because it
> is/isn't often needed.

### Which debugger interfaces do you use with Rust?
Type: select all that apply

- Editor/IDE extension (e.g. `termdebug`)
- Built-in IDE debugger
- Terminal line interface (e.g. `gdb`)
- Terminal UI (e.g. `gdb`'s TUI)
- Web interface (e.g. Pernosco)
- Other

> *Justification:*
>
> Interface used for a debugger materially changes the experience of using a
> debugger and the advantages/disadvantages of it.

### What pain points have you experienced using a debugger with Rust?
Type: select all that apply

- Cannot print variables (i.e. optimized-out code)
- Conditional breakpoints don't trigger
- Current line number jumps around unexpectedly
- Difficult to trace dataflow
- Don't have a source view of the current line being run
- Expression parser doesn't support expressions that you want to write
- Incorrect information displayed (i.e. line numbers, variable values)
- Often step too many times and need to restart from scratch
- Too much detail/irrelevant information (i.e. assembly views)
- Unintuitive interface/errors
- Sub-optimal representations of values (e.g. `Vec<T>` is shown as a pointer,
  length and capacity rather than the elements)

> *Justification:*
>
> It might be possible for us to address these - or they might be the result of
> the compiler's debuginfo output.


### Does your Rust debugging typically cross language boundaries?
Type: yes/no

> *Justification:*
>
> If lots of users are using debuggers when doing cross-language interop, then
> support for this could be improved.

### Which programming language(s) do you debug across (with Rust)?
Type: select all that apply

- C
- C++
- Java
- JavaScript
- Python
- ...

> *Justification:*
>
> Debugging Rust + C is very different from Rust + Python and the quality of
> the experience is likely very different too.

## Debugging advanced Rust features

### Have you ever used a debugger on macro-generated code in Rust?
Type: yes/no/not sure (if no/not sure: [`NEXT`](#have-you-ever-used-a-debugger-on-a-rust-procedural-macro))

> *Justification:*
>
> Macros are frequently used in Rust and has unique challenges for debugging.

### What are your experiences using a debugger on macro-generated code in Rust?
Type: free-form text

> *Justification:*
>
> Macros are frequently used in Rust and has unique challenges for debugging.

### Have you ever used a debugger on a Rust procedural macro?
Procedural macros are defined in separate crates, not using `macro_rules!`.
Type: yes/no/not sure (if no/not sure: [`NEXT`](#have-you-ever-used-a-debugger-with-async-rust))

> *Justification:*
>
> Macros are frequently used in Rust and has unique challenges for debugging.

### What are your experiences using a debugger on a Rust procedural macro?
Type: free-form text

> *Justification:*
>
> Macros are frequently used in Rust and has unique challenges for debugging.

### Have you ever used a debugger with async Rust?
Type: yes/no/not sure (if no/not sure: [`NEXT`](#have-you-ever-used-a-debugger-with-third-party-code-stdcratesioetc))

> *Justification:*
>
> async Rust is frequently used and has unique challenges for debugging.

### What are your experiences using a debugger on async Rust?
Type: free-form text

> *Justification:*
>
> async Rust is frequently used and has unique challenges for debugging.

### Have you ever used a debugger with third-party code (std/crates.io/etc)?
Type: yes/no/not sure (if no/not sure: end survey)

> *Justification:*
>
> Debugging third-party code might pose unique challenges for debugging.

### What are your experiences using a debugger on third-party code (std/crates.io/etc)
Type: free-form text

> *Justification:*
>
> Debugging third-party code might pose unique challenges for debugging.

## Maintainer questions

### Have you ever written a visualization for a debugger (with Rust)?
Type: select all that apply (optional)

- `gdb`
- `lldb`
- `NatVis`
- WinDbg (not `NatVis`)
- Visual Studio (not `NatVis`)

> *Justification:*
>
> Part of high-quality debugger support is things like type visualizations that
> could be shipped by libraries, knowing what experience Rust users have with
> writing these visualizations would be valuable.
