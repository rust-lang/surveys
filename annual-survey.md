# Rust annual survey guide
This document describes a brief guide on how to prepare the yearly Rust annual survey. It is probably not complete, but
it should nevertheless be helpful as a guide.

1. Copy survey from last year and perform basic modifications
   - Create `surveys/<year>-annual-survey/questions.md` and copy questions from the last year into it
   - Change basic time information, e.g. bump years
   - Change Rust versions (usually they move forward by ~10 versions, based on the 6-week schedule)
   - See [#234](https://github.com/rust-lang/surveys/pull/234) for an example PR
2. Go through the [issue tracker](https://github.com/rust-lang/surveys/issues) and try to resolve issues from the last year
   - Try to find issues that could be applicable, and modify the questions accordingly via PRs to this repo
3. Ask for general feedback for question/answer additions/modifications
   - Ideally, ask in the [#rust-survey](https://rust-lang.zulipchat.com/#narrow/stream/402479-t-community.2Frust-survey) or
   [#general](https://rust-lang.zulipchat.com/#narrow/stream/122651-general) Zulip streams, and also try to ask the individual
   top level teams (`t-compiler`, `t-lang`, `t-cargo` etc.).
4. Finalize the questions/answers for the given year (ideally by **end of September**)
5. Put the survey questions to SurveyHero
   - This needs collaboration with the Rust foundation, please ask in the [#rust-survey](https://rust-lang.zulipchat.com/#narrow/stream/402479-t-community.2Frust-survey)
   Zulip stream for assistance.
6. Find translator volunteers
   - Either for translating the survey, or for reviewing auto-generated translations.
   - You can ask around on the `#rust-survey` or `#general` Zulip streams for assistance.
7. Double-check the survey flow in SurveyHero
   - Go through all the possible paths through the survey, and check that the questions and answers in SurveyHero are
   the same as in `questions.md`.
   - Possible problems:
     - Missing answers or questions
     - Wrong survey flow (questions being skipped, or not being skipped, when they should be)
     - Radio buttons instead of checkboxes for exclusive answers
     - Typos
   - Optionally, the [`verifier`](verifier) binary can also be used to check this, if you are able to get access to the
   SurveyHero API for the survey.
8. Prepare a PR to https://blog.rust-lang.org/ with a blog post notifying about the survey
   - See [this PR](https://github.com/rust-lang/blog.rust-lang.org/pull/1178) for an example
   - Make sure to communicate the deadline of the survey, and include the survey link multiple times in the blog post!

## After the survey finishes
See [this issue](https://github.com/rust-lang/surveys/issues/247).
