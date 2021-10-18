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
        println!("{:?}", online.compare(markdown));
    }

    Ok(())
}

impl markdown::Question<'_> {
    fn compare(&self, other: &api::Question) -> Comparison {
        if self.text != other.text() {
            return Comparison::TitlesDiffer(self.text.to_owned(), other.text().to_owned());
        }

        match (&self.answers, other) {
            (markdown::Answers::FreeForm, _) => {
                if !other.is_free_form() {
                    return Comparison::QuestionTypesDiffer(
                        self.text.to_owned(),
                        QuestionType::FreeForm,
                        other.into(),
                    );
                }
            }
            (
                markdown::Answers::SelectOne(answers),
                api::Question::ChoiceList { choice_list, .. },
            ) if other.is_select_one() => {
                if !choice_list.contains_all_answers(&answers) {
                    return Comparison::AnswersDiffer(
                        choice_list.to_vec(),
                        answers.iter().map(|&s| s.to_owned()).collect(),
                    );
                }
            }
            (
                markdown::Answers::SelectMany(answers),
                api::Question::ChoiceList { choice_list, .. },
            ) if other.is_select_many() => {
                if !choice_list.contains_all_answers(&answers) {
                    return Comparison::AnswersDiffer(
                        choice_list.to_vec(),
                        answers.iter().map(|&s| s.to_owned()).collect(),
                    );
                }
            }
            (markdown::Answers::Matrix { .. }, _) => {
                println!("Can't compare matrices yet");
            }
            _ => {
                return Comparison::QuestionTypesDiffer(
                    self.text.to_owned(),
                    self.into(),
                    other.into(),
                );
            }
        }

        Comparison::Equal
    }
}

#[derive(Debug)]
enum Comparison {
    TitlesDiffer(String, String),
    QuestionTypesDiffer(String, QuestionType, QuestionType),
    AnswersDiffer(Vec<String>, Vec<String>),
    Equal,
}

#[derive(Debug)]
enum QuestionType {
    FreeForm,
    SelectOne,
    SelectMany,
    Matrix,
}

impl<'a> From<&'a api::Question> for QuestionType {
    fn from(q: &api::Question) -> Self {
        if q.is_select_one() {
            return QuestionType::SelectOne;
        }
        if q.is_select_many() {
            return QuestionType::SelectMany;
        }
        if q.is_free_form() {
            return QuestionType::FreeForm;
        }

        QuestionType::Matrix
    }
}

impl From<&markdown::Question<'_>> for QuestionType {
    fn from(q: &markdown::Question<'_>) -> Self {
        match &q.answers {
            markdown::Answers::FreeForm => Self::FreeForm,
            markdown::Answers::SelectOne(_) => Self::SelectOne,
            markdown::Answers::SelectMany(_) => Self::SelectMany,
            markdown::Answers::Matrix { .. } => Self::Matrix,
        }
    }
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
                surveys
                    .iter()
                    .map(|s| &s.title)
                    .cloned()
                    .collect::<Vec<_>>()
                    .join(", ")
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
