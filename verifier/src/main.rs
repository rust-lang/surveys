use std::error::Error;

use structopt::StructOpt;

mod api;
mod markdown;

fn main() -> Result<(), Box<dyn Error>> {
    env_logger::init();
    let args = Args::from_args();
    let markdown = std::fs::read_to_string("../surveys/2021-annual-survey/questions.md")?;
    let markdown_questions = markdown::parse(&markdown)?;
    let online_questions = fetch_online_questions(args)?;

    for (_online, _markdown) in markdown_questions.iter().zip(online_questions.iter()) {
        // TODO: compare questions
    }

    Ok(())
}

fn fetch_online_questions(args: Args) -> Result<Vec<api::Question>, Box<dyn Error>> {
    let client = api::Client::new(args.username, args.password);
    let surveys = client.fetch_surveys()?;
    let survey_name = args.survey_name;
    let survey = surveys
        .iter()
        .find(|s| s.title == survey_name)
        .ok_or_else(|| {
            format!(
                "no survey with the name '{}' in the account. Available surveys: {}",
                survey_name,
                surveys.iter().map(|s| &s.title).cloned().collect::<Vec<_>>().join(", ")
            )
        })?;
    client.fetch_questions(survey.survey_id)
}

#[derive(structopt::StructOpt)]
struct Args {
    #[structopt(short, long)]
    username: String,
    #[structopt(short, long)]
    password: String,
    #[structopt(short, long)]
    survey_name: String,
}
