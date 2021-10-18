use reqwest::blocking::Client as Reqwest;
use serde::Deserialize;

use std::error::Error;

pub struct Client {
    username: String,
    password: String,
    inner: Reqwest,
}

impl Client {
    pub fn new(username: String, password: String) -> Self {
        let inner = Reqwest::new();
        Self {
            username,
            password,
            inner,
        }
    }

    pub fn fetch_surveys(&self) -> Result<Vec<Survey>, Box<dyn Error>> {
        let response = self
            .inner
            .get("https://api.surveyhero.com/v1/surveys")
            .basic_auth(&self.username, Some(&self.password))
            .send()?
            .error_for_status()?;
        let surveys: Surveys = response.json()?;
        Ok(surveys.surveys)
    }

    pub fn fetch_questions(&self, survey_id: usize) -> Result<Vec<Question>, Box<dyn Error>> {
        let response = self
            .inner
            .get(format!(
                "https://api.surveyhero.com/v1/surveys/{}/elements",
                survey_id
            ))
            .basic_auth(&self.username, Some(&self.password))
            .send()?
            .error_for_status()?;

        let elements: Elements = response.json()?;
        Ok(elements.questions().collect())
    }
}

#[derive(Debug, Deserialize)]
pub struct Elements {
    elements: Vec<Element>,
}

impl Elements {
    pub fn questions(self) -> impl Iterator<Item = Question> {
        self.elements.into_iter().filter_map(|e| {
            if let Element::Question { question, .. } = e {
                Some(question)
            } else {
                None
            }
        })
    }
}

#[derive(Debug, Deserialize)]
#[serde(tag = "type")]
pub enum Element {
    #[serde(rename = "question")]
    Question {
        element_id: usize,
        question: Question,
    },
    #[serde(other)]
    Unknown,
}

#[derive(Debug, Deserialize)]
pub struct Question {
    question_text: String,
    #[serde(rename = "type")]
    typ: String,
}

#[derive(Debug, Deserialize)]
pub struct Surveys {
    pub surveys: Vec<Survey>,
}

#[derive(Debug, Deserialize)]
pub struct Survey {
    pub survey_id: usize,
    pub title: String,
}
