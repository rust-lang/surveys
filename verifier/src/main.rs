use reqwest::blocking::Client;
use std::error::Error;

mod markdown;
mod api;

fn main() -> Result<(), Box<dyn Error>> {
    let markdown = std::fs::read_to_string("../surveys/2021-annual-survey/questions.md")?;
    let questions = markdown::parse(&markdown);
    println!("{:#?}", questions);
    let client = Client::new();
    let response = client
        .get("https://api.surveyhero.com/v1/surveys")
        .basic_auth("", Some(""))
        .send()?
        .error_for_status()?;
    let surveys: api::Surveys = response.json()?;
    println!("{:#?}", surveys);

    let name = std::env::args().skip(1).next().expect("No name arg given");
    let survey = surveys
        .surveys
        .iter()
        .find(|s| s.title == name)
        .expect("No survey");
    let id = &survey.survey_id;

    let response = client
        .get(format!(
            "https://api.surveyhero.com/v1/surveys/{}/elements",
            id
        ))
        .basic_auth("", Some(""))
        .send()?
        .error_for_status()?;

    let elements: api::Elements = response.json()?;
    println!("{:#?}", elements.questions().collect::<Vec<_>>());

    Ok(())
}

