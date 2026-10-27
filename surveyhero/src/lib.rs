pub mod api;
pub mod cli;
pub mod markdown;
pub mod render;
pub mod txt_writer;

use crate::{api::Question, cli::SharedArgs, markdown::Answers};
impl markdown::Question<'_> {
    pub fn compare(&self, other: &Question) -> Comparison {
        if self.text != other.text() {
            return Comparison::TitlesDiffer {
                md: self.text.to_owned(),
                sh: other.text(),
            };
        }

        if self.description() != other.description_text() {
            return Comparison::DescriptionsDiffer {
                question: self.text.to_owned(),
                md: self.description(),
                sh: other.description_text(),
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
                let mismatched = choice_list.mismatched_answers(answers);
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
                let mismatched = choice_list.mismatched_answers(answers);
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
                let mismatched_rows = choice_table.mismatched_rows(answers1);
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
                let mismatched_columns = choice_table.mismatched_columns(answers2);
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
            (markdown::Answers::RatingScale, Question::RatingScale { .. }) => {}
            (markdown::Answers::Ranking(answers), Question::Ranking { ranking, .. }) => {
                let mismatched = ranking.mismatched_answers(answers);
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
            (Answers::InputList(answers), Question::InputList { input_list, .. }) => {
                let mismatched = input_list.mismatched_answers(answers);
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
pub struct AnswerDiff {
    md: String,
    sh: String,
}

#[allow(dead_code)]
#[derive(Debug)]
pub enum Comparison {
    TitlesDiffer {
        md: String,
        sh: String,
    },
    DescriptionsDiffer {
        question: String,
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
pub enum QuestionType {
    FreeForm,
    SelectOne,
    SelectMany,
    Matrix,
    RatingScale,
    Ranking,
    InputList,
}

impl From<&Question> for QuestionType {
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

        match q {
            Question::RatingScale { .. } => QuestionType::RatingScale,
            Question::Ranking { .. } => QuestionType::Ranking,
            Question::InputList { .. } => QuestionType::InputList,
            _ => QuestionType::Matrix,
        }
    }
}

impl From<&markdown::Question<'_>> for QuestionType {
    fn from(q: &markdown::Question<'_>) -> Self {
        match &q.answers {
            markdown::Answers::FreeForm => Self::FreeForm,
            markdown::Answers::SelectOne(_) => Self::SelectOne,
            markdown::Answers::SelectMany(_) => Self::SelectMany,
            markdown::Answers::Matrix { .. } => Self::Matrix,
            markdown::Answers::RatingScale => Self::RatingScale,
            markdown::Answers::Ranking(_) => Self::Ranking,
            markdown::Answers::InputList(_) => Self::InputList,
        }
    }
}

#[derive(Debug)]
struct SHCreds {
    username: String,
    password: String,
}

fn get_creds_from_env() -> SHCreds {
    let username = match std::env::var("SH_API_USER") {
        Ok(v) => v,
        _ => {
            panic!("Please ensure SH_API_USER env var is set.");
        }
    };

    let password = match std::env::var("SH_API_TOKEN") {
        Ok(v) => v,
        _ => {
            panic!("Please ensure SH_API_TOKEN env var is set.");
        }
    };

    SHCreds { username, password }
}

pub fn fetch_surveyhero_data(args: &SharedArgs) -> anyhow::Result<SurveyData> {
    let creds = get_creds_from_env();
    let mut client = api::Client::new(creds.username, creds.password);
    let surveys = client.fetch_surveys()?;
    let survey = surveys
        .iter()
        .find(|s| s.survey_id == args.survey_id)
        .ok_or_else(|| {
            anyhow::anyhow!(
                "no survey with ID {} in the account. Available surveys:\n{}",
                args.survey_id,
                surveys
                    .iter()
                    .map(|s| format!("id= {} name= {}", s.survey_id, &s.title))
                    .collect::<Vec<_>>()
                    .join("\n")
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
pub struct SurveyData {
    pub main: Vec<Question>,
    pub secondary_languages: Vec<(String, Vec<Question>)>,
}
