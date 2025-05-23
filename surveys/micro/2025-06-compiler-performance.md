# Survey questions

The goal of this survey is to figure out how much do Rust users struggle with compilation times and which compilation workflows are the most relevant for them. We would like to use this data so that we can focus the efforts of Rust compiler contributors on the areas of compilation performance that matter the most to our users.

Your feedback is much appreciated. This survey is fully anonymous. The Rust survey team will go through the answers and release a summary on the Rust blog after the survey is complete.

## User classification

### Do you use Rust?

Type: select one

- Yes, I use Rust [`NEXT`](#do-you-code-in-rust-at-a-company)
- No, I don't currently use Rust, but I have in the past [`NEXT`](#were-long-compilation-times-the-primary-reason-why-you-stopped-using-rust)
- No, I have never used Rust [`NEXT`](#other)

### Were long compilation times the primary reason why you stopped using Rust?

Type: select one

- Yes
- No, but it was one of the reasons why I stopped using Rust
- No

### Which operating systems do you use regularly for Rust development?

**Note**: this is specifically about which systems you personally use for development, *not* all the
systems you target.

Type: select all that apply (optional)

- Linux
- Windows
- Windows Subsystem for Linux
- macOS
- Other (open response)

### Do you code in Rust at a company?

If yes, what is the approximate size of the company?

Type: select one (optional)

- No, I do not code in Rust in a company
- Yes (1-50 employees)
- Yes (51-500 employees)
- Yes (501-5000 employees)
- Yes (more than 5000 employees)

## Workflows

### How do you build your Rust projects?

Type: select all that apply (optional)

- I use Cargo
- I use some other build system
- I combine Cargo and another build system
- If you use other build system(s), which ones do you use? (open response)

### Which compilation workflows are the most important to you?

Please rate how important are the following compilation workflows to you, and how much do you currently struggle with their performance currently.

Type: matrix (optional)

Workflows:

- Unoptimized rebuild (change code, rebuild without optimizations)
- Optimized rebuild (change code, rebuild with optimizations)
- Workspace rebuild (change a crate which causes multiple other crates in your workspace to be rebuilt)
- Clean unoptimized build (build a crate graph from scratch)
- Clean optimized build (build a crate graph from scratch)
- Build in a CI workflow

Priority:

- Not so important for me
- Important, compile times are acceptable for me
- Important, compile times are a blocker for me

### Do you have any other compilation workflow that you would like to mention?

Type: open response (optional)

### How do you primarily examine compilation errors in your code?

Type: select all that apply (optional)

- Using code editor (e.g. inline annotations)
- Using terminal commands (e.g. `cargo check`)
- Other (open response)

### If you use Cargo, how often do you use the following commands after each change to Rust code?

Type: matrix (optional)

Commands:

- `cargo check`
- `cargo clippy`
- `cargo test`
- `cargo run` / `cargo build`

Frequency:

- After every code change
- Only after I have resolved other issues
- Only after I am done (e.g. before creating a commit or pushing to a remote branch)
- Never

### How long do you need to wait for the compiler to rebuild your code after making a change?

Please select the longest duration range amongst the projects that you regularly work on.

This question focuses on local development workflows, not CI or remote builds. If you do not compile your Rust code locally, please skip this question.

Type: select one (optional)

- Less than a second
- Between 1 and 5 seconds
- Between 5 and 10 seconds
- Between 10 and 30 seconds
- Between 30 seconds and 1 minute
- Between 1 and 5 minutes
- More than 5 minutes

### Which of the following problems do you most struggle with?

Type: matrix (optional)

Commands:

- Waiting for a rebuild after making a small change
- Waiting for CI workflows that build Rust code
- `cargo check` and `cargo build` not sharing compilation cache
- `cargo check` and `cargo clippy` not sharing compilation cache
- Waiting for an IDE to show me inline error/warning annotations
- `cargo` rebuilding everything from scratch and I do not understand why

Priority:

- Not a problem for me
- Could be improved
- Big blocker for me

## Workarounds

### Have you used any of the following mechanisms to improve compilation performance?

Please select only mechanisms/workarounds that you have used **primarily** in order to improve compilation performance, not for other reasons.

Type: select all that apply (optional)

- Disable (or reduce) debuginfo (e.g. set `debug = 0` in `Cargo.toml`)
- Parallel compiler frontend (pass `-Zthreads=<N>` to the compiler)
- Cranelift codegen backend (e.g. set `codegen-backend = "cranelift"` in `Cargo.toml`)
- Alternative linker (e.g. `lld`/`mold`/`wild`)
- Caching compiler wrapper (e.g. `sccache`)
- Share `target` directory amongst multiple projects (with `CARGO_TARGET_DIR`)
- Split crates into smaller crates
- Reduce the amount of dependencies
- Disable default Cargo features of dependencies
- Create a Cargo feature that makes certain dependencies (or their features) optional
- Reduce usage of procedural macros
- Reduce usage of generic code (e.g. by converting it to use `dyn Trait` instead)
- Merge integration tests into a single binary
- Something else (open response)

### If you use an alternative linker, which one do you use?

Type: select all that apply (optional)

- gold
- lld
- mold
- wild
- Other (open response)

### Do you use a global `config.toml` override?

You can create a `config.toml` file in your `CARGO_HOME` directory (e.g. `~/.cargo/config.toml`) which can be used to apply certain compilation settings (e.g. using a faster linker) across all Cargo projects on your computer.

Type: select one (optional)

- Yes
- No

### Do you use a nightly compiler to achieve better compilation performance?

Please answer `Yes` if you use the `nightly` toolchain primarily for achieving better compilation performance, not for other reasons.

Type: select one (optional)

- Yes
- No [`NEXT`](#debugging)

### How does using the nightly compiler help you achieve better compilation performance?

Type: open answer (optional)

## Debugging

### How often do you use a debugger to debug your Rust code?

Type: select one (optional)

- Never or very rarely
- Sometimes (e.g. once per week or less)
- Often (e.g. multiple times per day)
- Almost always (e.g. after almost every build)

### How often do you use a profiler to profile your Rust code?

Type: select one (optional)

- Never or very rarely
- Sometimes (e.g. once per week or less)
- Often (e.g. multiple times per day)
- Almost always (e.g. after almost every build)

### Do you require unoptimized builds to be debuggable by default?

`cargo build` with the default `dev` profile produces full debug information (debuginfo) by default. This enables debugging using a debugger, but it can also make compilation times slower (by varying amounts, e.g. 30%). In order to improve compilation performance, this debuginfo could be lowered e.g. to `line-tables-only` by default, which still enables rich backtrace information, but does not allow proper debugging.

Type: select one (optional)

- Yes, I want full debuginfo by default
- No, I would prefer faster compilation with less debuginfo by default

## Other

### Is there anything else related to Rust compiler performance that you would like to tell us?

Type: free text (optional)
