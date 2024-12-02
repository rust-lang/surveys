# Verifier

This tool is used to verify that surveys in this repo match the surveys on our survey hosting platform to prevent drift between the two.

## Usage
Run `cargo run -- --help` to see the available subcommands.

- You can use `cargo run -- check` to test if the SurveyHero contents match the local Markdown files.
- You can use `cargo run -- download` to create local Markdown files from the SurveyHero contents.

The username and password flags are the names provided by the SurveyHero [developer API console](https://www.surveyhero.com/user/account/api) after creating an API key.
