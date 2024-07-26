# Micro surveys

The Rust community survey team can run micro-surveys for members of the Rust Project. This document explains how do these micro-surveys work. If you want to run a micro-survey, please create a topic on the survey team [Zulip stream](https://rust-lang.zulipchat.com/#narrow/stream/402479-t-community.2Frust-survey)
and check out the [guide](#how-to-create-a-new-micro-survey) below.

## What is a micro survey?

A small survey which is very low cost (in both time and cognitive load) to complete (and prepare). They should be focused on a single topic (possibly with a first question to get context on the respondent for cohort analysis), should take fewer than ten minutes to complete and ideally contain a reasonable amount of questions (e.g. up to ten, but it is not a hard limit). See [below](#examples) for some examples.

There are two intended target audiences of these micro-surveys (each survey can target one or the other):

- Members of the Rust community. This gives the Rust Project a way to quickly gauge the opinions of the community about a very targeted topic, concerning e.g. usage of Rust or the development of new features.
- Members of the Rust Project (Rust maintainers). This gives the Rust Project leadership a way to learn more about the "mood" inside the Project, and ask various meta questions about the development of Rust and its inner workings.

To reduce the latency of their creation and evaluation, micro-surveys will be published only in the English language by
default. However, we can also publish the survey in a different language if it makes sense (e.g. if we wanted to
primarily address members of the community in a specific geographic region).

The community survey team will design and manage micro-surveys. Data will be managed, processed, and distributed in the same way as the annual survey, i.e. raw data will be kept private, some data may be shared publicly in a blog post, processed data will be distributed to relevant teams.

Note that the micro-surveys should not need to ask any [PII](https://en.wikipedia.org/wiki/Personal_data) or [DEI](https://en.wikipedia.org/wiki/Diversity,_equity,_and_inclusion) questions, to avoid dealing with potential privacy issues and allowing lightweight handling of the data.

The survey team will accept requests for micro-survey topics and questions from Rust teams. We don't anticipate needing outside help with data processing, except in exceptional circumstances. Ideally, we should have the creation and analysis of the survey as automated as possible, to make these micro-surveys easier to manage.

## Why are we doing this?

As always with surveys, we want to better understand our users. Conducting small surveys lets us sample our user base more directly than social media, which has strong network bias, and more frequently than the annual survey.

The primary goal of micro-surveys is to provide very low-latency feedback to Rust Project members that are designing a feature or trying to find out pain points of the current state of some area of Rust, or to gauge interest in new ideas or features. In this way, we can be more responsive to teams' needs to understand users, letting our teams iterate more effectively on their work.

## Examples

These are just strawman examples, the language of the questions is unpolished.

### Project-specific sentiment analysis: debugging

We could run this survey to find out what pain points do Rust user have with debugging Rust programs.

* On average, how often in a week do you use a debugger when working with Rust code?
    - Never
    - Once or less
    - 2-4 times
    - 5-10 times
    - > 10 times

* How satisfied are you with the experience of debugging Rust code? (Horrible, not great, ok, good, fantastic)

* Do you typically succeed when using a debugger or give up?
    - Usually succeed
    - Sometimes succeed, sometimes fail
    - Usually fail

### One-off language questions: GATs

We could run this survey to find out how Rust users use a specific feature.

* Have you written a trait using GATs? (Yes, no, not sure)

* Have you implemented or used a trait which used GATs (Yes, no, not sure)

* If you've written a trait using a lifetime-GAT, did you use the lifetime as a bound on Self (`Self: 'a`)? (Yes, no, I haven't written a lifetime-GAT)

### Maintainer survey: review capacity

We could run this survey to find out how do Rust maintainers feel and should we prioritize
something in the project management.

* Do you review pull requests on any rust-lang repository? (Yes, no)

* Do you feel overwhelmed by the amount of reviews assigned to you? (Yes, no, sometimes, not sure)

* Would you like to switch to a different PR assignment logic, e.g. a pull-based model? (Yes, no)


## How to create a new micro-survey?
Send a PR against this repository, with a new Markdown file describing the questions of the survey, in the `surveys/micro/<name-of-survey>` directory.

The format of the Markdown file is described [here](surveys/notes/reference.md).
