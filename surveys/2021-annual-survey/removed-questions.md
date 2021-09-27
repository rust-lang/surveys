# Removed Questions

This document attempts to capture questions that were removed from previous iterations of the survey as well as the justifications for their removal.

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

### Please provide any additional details on why you never used Rust.

Free form.

> **REMOVED**
>
> Vague.

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
> The level of detail in this question is off and so it has been replaced with
> "To what extent is Rust currently being used by your company?" which gets more
> at the heart of how important Rust is to companies.

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

### What resources do you use to keep up with the Rust ecosystem?

Select all that apply:

> **REMOVED**
>
> Integrated with 'How do you participate in the community' question

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
> Conference organizers tend to have a location in mind, rather than be looking for a location.

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


### If you don't use rustup, why not?

Select all that apply:

- I'm prefer using my platform's package installer (yum, apt-get, homebrew, msi installer, etc.)
- I don't trust that rustup provides secure binaries
- I didn't know about it
- The network I'm on does not allow for it (e.g., firewall)
- I tried, but it didn't work
- Other

> **REMOVED**
>
> We don't necessarily want everyone to use Rustup. If we do want this kind of information, we should ask more
> specific and actionable questions. We might want to ask such questions for other tools too - there is no
> indication that Rustup maintainers are more in need of this info than others.
>
> TODO: a lot of people previously reported that they *use* rustup but wish they didn't. How can we capture that here?
> TODO: this was previously free form. Do we prefer the multiple choice?
