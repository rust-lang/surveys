# Monthly micro surveys

## What is a micro survey?

A small survey which is very low cost (in both time and cognitive load) to complete. They should be focussed on one topic (possibly with a first question to get context on the respondent for cohort analysis), should take fewer than five minutes to complete, be three or fewer questions (all multiple choice rather than free-form, though we might ask a single free-form question instead), not require too much thinking, research, or permission (from employers, etc.), and be fun to answer. See below for some examples.

We should promote the micro surveys in a fairly determined way - in a blog post on the main Rust blog, in official and unofficial tweets, posting in forums, requesting mentions in This Week in Rust and other newsletters, etc.

Micro surveys will only be published in English.

The survey WG will design and manage the survey. Data will be managed, processed, and distributed in the same way as the annual survey. I.e., raw data will be kept private, some data may be shared publicly in a blog post, processed data will be distributed to relevant teams. The survey WG will accept requests for micro-survey topics and questions from Rust teams, but will need to edit and prioritise. We don't anticipate needing outside help with data processing or translation, except in exceptional circumstances.

## What is monthly?

A micro survey will be published and promoted at roughly the same time each month. At most we will publish 11 micro surveys per year (skipping the month in which the annual survey is published). The survey will be open for responses for one week.

## Why are we doing this?

As always with surveys, we want to better understand our users. Conducting regular small surveys lets us sample our user base more directly than social media which has strong network bias, and more frequently than the annual survey. Increased frequency means we can be more responsive to teams' needs to understand users, letting our teams iterate more effectively on their work. Small regular surveys also let us track user sentiment better over time, for example by asking the same questions before and after an initiative.

## Examples

These are strawman examples, I'm not proposing we run actual surveys on these topics or with these questions, and the language of the questions is unpolished.

### Project-specific sentiment analysis: debugging

We could run this survey before starting work to improve debugging and 12 months later, when work is complete and users have had some time to use it.

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


### General user sentiment: Rust jobs

This survey could be repeated every few months.

* How long have you been programming in Rust?
  - less than one year
  - one to two years
  - two to three years
  - more than three years

* How many days in the past week have you used Rust professionaly? (0, 1, 2, 3, 4, 5)

* How confident are you that you could get a job programming mostly in Rust (if you were to leave your current job)? (Not confident, somewhat, very)


### One-off language questions: GATs

* Have you written a trait using GATs? (Yes, no, not sure)

* Have you implemented or used a trait which used GATs (Yes, no, not sure)

* If you've written a trait using a lifetime-GAT, did you use the lifetime as a bound on Self (`Self: 'a`)? (Yes, no, I haven't written a lifetime-GAT)
