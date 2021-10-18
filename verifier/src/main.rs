use std::error::Error;

use structopt::StructOpt;

mod api;
mod markdown;

fn main() -> Result<(), Box<dyn Error>> {
    let args = Args::from_args();
    let markdown = std::fs::read_to_string("../surveys/2021-annual-survey/questions.md")?;
    let questions = markdown::parse(&markdown);
    println!("{:#?}", questions);
    let client = api::Client::new(args.username, args.password);
    let surveys = client.fetch_surveys()?;
    println!("{:#?}", surveys);

    let survey_name = args.survey_name;
    let survey = surveys
        .iter()
        .find(|s| s.title == survey_name)
        .expect("No survey");

    let questions = client.fetch_questions(survey.survey_id)?;
    println!("{:#?}", questions);

    Ok(())
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
