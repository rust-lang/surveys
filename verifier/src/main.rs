use crate::api::Question;
use crate::render::render_questions;
use anyhow::Context;
use std::io::ErrorKind;
use std::path::PathBuf;
use structopt::StructOpt;

mod api;
mod markdown;
mod render;

fn main() -> anyhow::Result<()> {
    env_logger::init();
    let args = Args::from_args();
    let online_data = fetch_surveyhero_data(args)?;

    let base_path = PathBuf::from("../surveys/2024-annual-survey");
    let mut pairs = vec![(base_path.join("questions.md"), online_data.main)];
    for (language, questions) in online_data.secondary_languages {
        pairs.push((
            base_path
                .join("translations")
                .join(language)
                .with_extension("md"),
            questions,
        ));
    }

    for (path, questions) in pairs {
        println!("-----\nChecking {}\n-----\n", path.display());

        let markdown = match std::fs::read_to_string(&path) {
            Ok(markdown) => markdown,
            Err(error) if error.kind() == ErrorKind::NotFound => {
                eprintln!(
                    "{} not found, creating it with data from SurveyHero",
                    path.display()
                );
                render_questions(&questions, &path)?;
                std::fs::read_to_string(&path)?
            }
            Err(e) => return Err(e.into()),
        };
        let markdown_questions = markdown::parse(&markdown)
            .with_context(|| format!("Cannot parse {} as Markdown", path.display()))?;
        check_questions(&markdown_questions, &questions);
    }

    Ok(())
}

fn check_questions(markdown_questions: &[markdown::Question], sh_questions: &[Question]) {
    for (online, markdown) in markdown_questions.iter().zip(sh_questions.iter()) {
        let comparison = online.compare(markdown);
        if !matches!(comparison, Comparison::Equal) {
            println!("Q: '{}'", online.text);
            println!("  {:#?}", comparison);
        }
    }

    if markdown_questions.len() > sh_questions.len() {
        println!(
            "Missing questions in the online version:\n{}",
            markdown_questions[sh_questions.len()..]
                .iter()
                .map(|q| q.text)
                .collect::<Vec<_>>()
                .join("\n-")
        );
    }
    if sh_questions.len() > markdown_questions.len() {
        println!(
            "Missing questions in the markdown version:\n-{}",
            sh_questions[markdown_questions.len()..]
                .iter()
                .map(|q| q.text())
                .collect::<Vec<_>>()
                .join("\n-")
        );
    }
}

impl markdown::Question<'_> {
    fn compare(&self, other: &Question) -> Comparison {
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
            (markdown::Answers::SelectOne(answers), Question::ChoiceList { choice_list, .. })
                if other.is_select_one() =>
            {
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
            (markdown::Answers::SelectMany(answers), Question::ChoiceList { choice_list, .. })
                if other.is_select_many() =>
            {
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
                Question::ChoiceTable { choice_table, .. },
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

#[allow(dead_code)]
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

impl<'a> From<&'a Question> for QuestionType {
    fn from(q: &Question) -> Self {
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

fn fetch_surveyhero_data(args: Args) -> anyhow::Result<SurveyData> {
    let mut client = api::Client::new(args.username, args.password);
    let surveys = client.fetch_surveys()?;
    let survey_name = args.survey_name;
    let survey = surveys
        .iter()
        .find(|s| s.title == survey_name)
        .ok_or_else(|| {
            anyhow::anyhow!(
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
    let languages = client.fetch_secondary_languages(survey.survey_id)?;

    let main = client.fetch_questions(survey.survey_id, None)?;
    let secondary_languages = languages
        .into_iter()
        .map(|l| {
            let questions = client.fetch_questions(survey.survey_id, Some(l.code.clone()))?;
            let language = l.code.clone();
            Ok::<_, anyhow::Error>((language, questions))
        })
        .collect::<Result<_, _>>()?;

    Ok(SurveyData {
        main,
        secondary_languages,
    })
}

#[derive(Debug)]
struct SurveyData {
    main: Vec<Question>,
    secondary_languages: Vec<(String, Vec<Question>)>,
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
