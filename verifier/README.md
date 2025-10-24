# Verifier

This tool is used to verify that surveys in this repo match the surveys on our survey hosting platform to prevent drift between the two.

## Usage

Set the env variables (`SH_API_USER` and `SH_API_TOKEN`) with the SurveyHero credentials. Generate them from the SurveyHero [developer API console](https://www.surveyhero.com/user/account/api).

Run `cargo run -- --help` to see the available subcommands.

- First run `cargo run -- download --survey-id SURVEY_ID --path YYYY/<SURVEY_NAME>` to create local Markdown files from the SurveyHero contents.
- Then run `cargo run -- check --survey-id SURVEY_ID --path YYYY/<SURVEY_NAME>` to test if the SurveyHero contents (question set and translations) match with the local Markdown files.

Example:
```
cd verifier
cargo run -- download --survey-id 1234567 --path 2025/annual-survey/
```

If you're unsure about the survey ID, enter any number and a list of the available surveys will be returned.

If the `check` command returns discrepancies, they will be shown as:
```
Q: 'What is the oldest version of Rust you use for any development task?'
  AnswersDiffer(
    [
        AnswerDiff {
            md: "1.92 (nightly), and then every version from 1.91 to 1.0 in descending order, and \"a pre-1.0 version\"",
            sh: "1.92 (nightly)",
        },
    ],
)
```

The `md` item is your local copy, the `sh` is what currently is on Surveyhero.

> [!IMPORTANT]
> Our **git repository** is authoritative so the changes should be applied on Survery Hero.
