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

    for (online, markdown) in markdown_questions.iter().zip(online_questions.iter()) {
        if online.text != markdown.question_text {
            println!(
                "Text doesn't match\n'{}' != '{}'",
                online.text, markdown.question_text
            );
        }
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
        .expect("No survey");
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
