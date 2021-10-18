use serde::Deserialize;

#[derive(Debug, Deserialize)]
pub struct Elements {
    elements: Vec<Element>,
}

impl Elements {
    pub fn questions(&self) -> impl Iterator<Item = &Element> {
        self.elements.iter()
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
