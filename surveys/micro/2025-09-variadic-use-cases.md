# Survey questions

This survey is meant to both measure interest in variadic generics and gather data about how they might be used once implemented.

You can think of variadic generics as “being able to implement a trait for tuples with an arbitrary number of fields”.

Variadics in Rust might look like this (placeholder syntax):

```rust
impl<...Ts: SomeTrait> SomeTrait for (...Ts) {
    fn do_stuff(&self) -> u32 {
        let mut sum = 0;
        for member in ...self {
            // The trait bounds ensure each member has a do_stuff() method
            sum += member.do_stuff();
        }
        sum
    }
}

let value: u32 = (0, 0.5, "hello", Some("hello"), false).do_stuff();
```

See [Analysing variadics, and how to add them to Rust](https://poignardazur.github.io/2021/01/30/variadic-generics/) for a full overview of features associated with variadic generics, and possible use-cases.

This survey is fully anonymous. The Rust survey team will go through the answers and release a summary on the Rust blog after the survey is complete. It's fairly short and should take less than 10 minutes to complete.


### How long have you been using Rust?

Type: select one (optional)

    Never
    Zero to two years
    Two to four years
    Four to six years
    More than six years


### Have you heard about variadic generics before?

Type: select all that apply

- Yes, through Pre-RFCs and discussions on [`internals.rust-lang.org`](https://internals.rust-lang.org).
- Yes, through discussions on Reddit.
- Yes, through blog posts on [`poignardazur.github.io`](https://poignardazur.github.io/2025/07/09/variadic-generics-dead-ends/).
- Yes, through other programming languages.
- Yes, through other means: (open response)
- No.


### Are there cases where variadic generics would have made your project easier?

If you knew about variadics, are there cases where you've wanted them to be implemented in Rust?
If you haven't heard about variadics before, are there cases where you've wanted to be able to iterate over lists of different types?

Type: select one

- Yes
- No [`NEXT`](#variadic-type-mappings)

### Can you give more details about the project?

Please write a description of the project and what you would have needed variadics for.
Be as detailed as you like, more detail is better.

Type: free text


## Variadic type mappings

The following section refers to "mappings" of variadic generics.

In this context, variadic mappings refer to code that takes N-tuples of types as generic parameters, and refers to N-tuples of types derived from those parameters, where each type in the tuple is transformed in the same way.

For example:

```rust
impl<...Ts> UnwrapAll for (Option<...Ts>) {
    type Unwrapped = (...Ts);
    fn unwrap_all(self) -> Self::Unwrapped {
        for option in ...self {
            option.unwrap()
        }
    }
}

let my_gift_boxes = (Some(1), Some(true), Some("hello"));
let opened_gifts = my_gift_boxes.unwrap_all();
assert_eq!(opened_gifts, (1, true, "hello"));
```

In that example, the trait `UnwrapAll` maps `u32, bool, &str` to `Option<u32>, Option<bool>, Option<&str>`.

### Are there cases where variadic mappings would have made your project easier?

Type: select one

- Yes (same project as above)
- Yes (another project)
- No [`NEXT`](#non-linear-variadic-generics)

### Can you give more details about the project?

Be as detailed as you like, more detail is better.

If it's the same project as before, you can include more details about how you would have used variadic mappings specifically.

Type: free text (optional)


## Non-linear variadic generics

The following section refers to "non-linear" variadic generics.

"Linear" variadics generics, in this context, means generics that only map over types in a fixed order, and otherwise preserve a one-to-one correspondence between type parameters and derived types.

All the examples so far have been linear variadics.

"Non-linear" variadics generics mean things like filtering a tuple of types to only keep those that implement a trait, or reversing a tuple of types, or finding the first type in a tuple that implements a trait.

```rust
fn get_children<...Ts>(parents: (...Ts)) -> (for <T of ...Ts where T: Parent> T::Child) {
    for parent in ...parents where parent: Parent {
        parent.child()
    }
}
```

### Are there cases where non-linear variadic generics would have made your project easier?

Type: select one

- Yes (same project as above)
- Yes (another project)
- No [`NEXT`](#how-high-a-priority-would-you-say-variadics-are-for-you)

### Can you give more details about the project?

Be as detailed as you like, more detail is better.

If it's the same project as before, you can include more details about how you would have used non-linear variadics specifically.

Type: free text (optional)


## How high a priority would you say variadics are for you?

Type: select one

- It should be the highest priority feature.
- Very important.
- Moderately important.
- Nice to have.
- I don't care.
- I don't want Rust to have variadics.
