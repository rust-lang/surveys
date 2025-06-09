use crate::api::Question;
use crate::render::render_questions;
use anyhow::Context;
use clap::Parser;
use std::io::ErrorKind;
use std::path::PathBuf;

mod api;
mod markdown;
mod render;

fn main() -> anyhow::Result<()> {
    env_logger::init();

    let args = Args::parse();
    let online_data = fetch_surveyhero_data(args.cmd.shared())?;

    let base_path = PathBuf::from(format!("../surveys/{}", args.cmd.shared().path));
    let pairs = if base_path.is_dir() {
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
        pairs
    } else {
        vec![(base_path, online_data.main)]
    };

    match args.cmd {
        VerifierCmd::Check { .. } => {
            for (path, questions) in pairs {
                println!("-----\nChecking {}\n", path.display());

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
        }
        VerifierCmd::Download { .. } => {
            for (path, questions) in pairs {
                // Do not overwrite the English version, as it contains special metadata and
                // comments
                if path
                    .file_name()
                    .map(|p| p != "questions.md")
                    .unwrap_or(true)
                {
                    render_questions(&questions, &path)?;
                }
            }
        }
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
            return Comparison::TitlesDiffer {
                md: self.text.to_owned(),
                sh: other.text().to_owned(),
            };
        }

        match (&self.answers, other) {
            (markdown::Answers::FreeForm, _) => {
                if !other.is_free_form() {
                    return Comparison::QuestionTypesDiffer {
                        question: self.text.to_owned(),
                        md: QuestionType::FreeForm,
                        sh: other.into(),
                    };
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
                            .map(|(s1, s2)| AnswerDiff {
                                sh: s1,
                                md: s2.to_string(),
                            })
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
                            .map(|(s1, s2)| AnswerDiff {
                                sh: s1,
                                md: s2.to_string(),
                            })
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
                            .map(|(s1, s2)| AnswerDiff {
                                sh: s1,
                                md: s2.to_string(),
                            })
                            .collect(),
                    );
                }
                let mismatched_columns = choice_table.mismatched_columns(&answers2);
                if !mismatched_columns.is_empty() {
                    return Comparison::MatrixAnswersDiffer(
                        mismatched_columns
                            .into_iter()
                            .map(|(s1, s2)| AnswerDiff {
                                sh: s1,
                                md: s2.to_string(),
                            })
                            .collect(),
                    );
                }
            }
            _ => {
                return Comparison::QuestionTypesDiffer {
                    question: self.text.to_owned(),
                    md: self.into(),
                    sh: other.into(),
                };
            }
        }

        Comparison::Equal
    }
}

#[allow(dead_code)]
#[derive(Debug)]
struct AnswerDiff {
    md: String,
    sh: String,
}

#[allow(dead_code)]
#[derive(Debug)]
enum Comparison {
    TitlesDiffer {
        md: String,
        sh: String,
    },
    QuestionTypesDiffer {
        question: String,
        md: QuestionType,
        sh: QuestionType,
    },
    AnswersDiffer(Vec<AnswerDiff>),
    MatrixAnswersDiffer(Vec<AnswerDiff>),
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

fn fetch_surveyhero_data(args: &SharedArgs) -> anyhow::Result<SurveyData> {
    let mut client = api::Client::new(args.username.clone(), args.password.clone());
    let surveys = client.fetch_surveys()?;
    let survey_name = &args.survey_name;
    let survey = surveys
        .iter()
        .find(|s| s.title.as_str() == survey_name)
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

    log::debug!("Downloading English version");
    let main = client.fetch_questions(survey.survey_id, None)?;
    let secondary_languages = languages
        .into_iter()
        .map(|l| {
            log::debug!("Downloading {} version", l.code);
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

/// Verify the contents of the Annual Rust Survey on SurveyHero.
#[derive(clap::Parser)]
struct Args {
    #[clap(subcommand)]
    cmd: VerifierCmd,
}

#[derive(clap::Parser, Clone)]
struct SharedArgs {
    /// SurveyHero API key username.
    #[clap(long)]
    username: String,
    /// SurveyHero API key token.
    #[clap(long)]
    password: String,
    /// Name of the survey.
    #[clap(long)]
    survey_name: String,
    /// Survey path. Corresponds to a Markdown file or a directory at `surveys/<path>`.
    #[clap(long)]
    path: String,
}

#[derive(clap::Parser, Clone)]
enum VerifierCmd {
    /// Check that whatever the contents on SurveyHero match the local Markdown files.
    Check {
        #[clap(flatten)]
        shared: SharedArgs,
    },
    /// Create or overwrite local Markdown files with the contents on SurveyHero.
    Download {
        #[clap(flatten)]
        shared: SharedArgs,
    },
}

impl VerifierCmd {
    fn shared(&self) -> &SharedArgs {
        match self {
            VerifierCmd::Check { shared } => shared,
            VerifierCmd::Download { shared } => shared,
        }
    }
}
