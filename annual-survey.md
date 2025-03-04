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
6. Translate the questionnaire
   - SurveyHero can generate the questionnaire in other languages, uses some machine translation which often leaves a bit to desire
   - Find translators for reviewing the survey and the auto-generated translations
   - You can ask around on the `#rust-survey` or `#general` Zulip streams for assistance.
   - Be aware that the SurveyHero export feature is currently broken (breaks non Latin alphabets) and importing the translations is not allowed. Correcting the translations is therefore a manual work both for the translator and for the operator that has access to the SurveyHero backoffice.
   - Translators can take advantage of [this small guide](https://rust-lang.zulipchat.com/#narrow/stream/402479-t-community.2Frust-survey/topic/Translation.20guide/near/406836813)
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
1. Analyze the results and publish a blog post
   - There is a dedicated section about this [below](#analysing-survey-results)
2. Add a link to the previous survey announcement blog post pointing to the blog post with survey results
3. Update [FAQ](documents/Community-Survey-FAQ.md) with a link to the results blog post.
4. Post a link to the results to [This Week in Rust](https://this-week-in-rust.org/)

### Analysing survey results
After the survey finishes, we should generate a PDF with a report and a blog post that will be published on https://blog.rust-lang.org/.

To do that, we first need to get the filtered data from the Rust Foundation staff. This comes in the form of two CSV files (one with aggregated answer counts per each question, and another that contains the specific answers per each respondent).

To generate the PDF report and the blog post we use a Python script (e.g. `surveys/2023-annual-survey/report/main.py`) that extracts data from the CSV files and renders charts using the [`report`](report) Python library. You will thus need a Python environment:

```bash
$ python3.8 -m venv venv
$ source venv/bin/activate
(venv) $ pip install -r report/requirements.txt
(venv) $ pip install -U pillow # this might be needed if the code fails
```

#### Blog post
To generate the blog post, copy the `main.py` file from the previous year, go through all questions and patch up the question IDs to match the contents of the actual survey (questions can move around, be added or removed, so it needs manual analysis). After the questions are patched, run the python script. Optionally with `--skip-pdf` to skip the PDF report generation.

The way it works is that we use a template Markdown file (e.g. `surveys/2023-annual-survey/report/2024-02-19-2023-Rust-Annual-Survey-2023-results.md`) with the contents of the blog post, which is rendered by the `main.py` script. The render process adds charts to the blog post and copies all the used image files and the final rendered Markdown file into a checkout of the [blog repository][blog repository], which you must have somewhere at your filesystem.

To test the contents of the rendered blog post, you have to run the `main.py` script, then run `cargo run` in the blog repository directory and open the built HTML file in your browser of choice. Note that for faster feedback, I would recommend commenting out the rendering of the PDF in `main.py` (which is relatively slow) when making frequent changes to the blog post template.

The blog post should contain a link to the prepared PDF report. For that, the `surveys` PR with the PDF report should be merged, and the PDF report should thus be in the `surveys` repository at a stable location, so that we can link to it from the blog post.

After the blog post is prepared, send a PR to the [blog repository][blog repository] and ask others for feedback. Note that you will need to add the image and script directories (that were created and populated by the Python script) to the git commit with the blog post. See [this PR](https://github.com/rust-lang/blog.rust-lang.org/pull/1455) for an example.

You will then also need to update the blog template in the `surveys` repo, but that can be done asynchronously.

[blog repository]: https://github.com/rust-lang/blog.rust-lang.org

#### PDF report
To also generate the PDF report, run the python script without additional parameters.

After the PDF report is prepared, send a PR to the [surveys](https://github.com/rust-lang/surveys) repository.
