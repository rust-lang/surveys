use std::error::Error;

use structopt::StructOpt;

mod api;
mod markdown;

fn main() -> Result<(), Box<dyn Error>> {
    env_logger::init();
    let args = Args::from_args();
    let markdown = std::fs::read_to_string("../surveys/2024-annual-survey/questions.md")?;
    let markdown_questions = markdown::parse(&markdown)?;
    let online_questions = fetch_online_questions(args)?;

    for (online, markdown) in markdown_questions.iter().zip(online_questions.iter()) {
        let comparison = online.compare(markdown);
        if !matches!(comparison, Comparison::Equal) {
            eprintln!("Q: '{}'", online.text);
            eprintln!("  {:#?}", comparison);
        }
    }

    if markdown_questions.len() > online_questions.len() {
        eprintln!(
            "Missing questions in the online version:\n{}",
            markdown_questions[online_questions.len()..]
                .iter()
                .map(|q| q.text)
                .collect::<Vec<_>>()
                .join("\n-")
        );
    }
    if online_questions.len() > markdown_questions.len() {
        eprintln!(
            "Missing questions in the markdown version:\n-{}",
            online_questions[markdown_questions.len()..]
                .iter()
                .map(|q| q.text())
                .collect::<Vec<_>>()
                .join("\n-")
        );
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
                let mismatched = choice_list.mismatched_answers(&answers);
                if !mismatched.is_empty() {
                    return Comparison::AnswersDiffer(
                        mismatched
                            .into_iter()
                            .map(|(s1, s2)| (s1, s2.to_string()))
                            .collect(),
                    );
                }
            }
            (
                markdown::Answers::SelectMany(answers),
                api::Question::ChoiceList { choice_list, .. },
            ) if other.is_select_many() => {
                let mismatched = choice_list.mismatched_answers(&answers);
                if !mismatched.is_empty() {
                    return Comparison::AnswersDiffer(
                        mismatched
                            .into_iter()
                            .map(|(s1, s2)| (s1, s2.to_string()))
                            .collect(),
                    );
                }
            }
            (
                markdown::Answers::Matrix {
                    answers1, answers2, ..
                },
                api::Question::ChoiceTable { choice_table, .. },
            ) => {
                let mismatched_rows = choice_table.mismatched_rows(&answers1);
                if !mismatched_rows.is_empty() {
                    return Comparison::MatrixAnswersDiffer(
                        mismatched_rows
                            .into_iter()
                            .map(|(s1, s2)| (s1, s2.to_string()))
                            .collect(),
                    );
                }
                let mismatched_columns = choice_table.mismatched_columns(&answers2);
                if !mismatched_columns.is_empty() {
                    return Comparison::MatrixAnswersDiffer(
                        mismatched_columns
                            .into_iter()
                            .map(|(s1, s2)| (s1, s2.to_string()))
                            .collect(),
                    );
                }
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
    AnswersDiffer(Vec<(String, String)>),
    MatrixAnswersDiffer(Vec<(String, String)>),
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
