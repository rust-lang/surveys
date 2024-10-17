use regex::Regex;
use reqwest::blocking::Client as Reqwest;
use serde::Deserialize;
use std::sync::LazyLock;
use std::time::{Duration, SystemTime};

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
    pub fn fetch_surveys(&mut self) -> anyhow::Result<Vec<Survey>> {
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
    pub fn fetch_questions(
        &mut self,
        survey_id: usize,
    ) -> anyhow::Result<Vec<Question>> {
        let response = self
            .inner
            .get(format!(
                "https://api.surveyhero.com/v1/surveys/{}/questions",
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
#[serde(tag = "type")]
pub enum Question {
    #[serde(rename = "choice_list")]
    ChoiceList {
        question_text: String,
        choice_list: ChoiceList,
    },
    #[serde(rename = "input")]
    Input { question_text: String },
    #[serde(rename = "choice_table")]
    ChoiceTable {
        question_text: String,
        choice_table: ChoiceTable,
    },
}

impl Question {
    pub fn text(&self) -> &str {
        match self {
            Self::ChoiceList { question_text, .. } => question_text,
            Self::Input { question_text, .. } => question_text,
            Self::ChoiceTable { question_text, .. } => question_text,
        }
    }

    pub fn is_free_form(&self) -> bool {
        matches!(self, Self::Input { .. })
    }

    pub fn is_select_many(&self) -> bool {
        match self {
            Self::ChoiceList { choice_list, .. } => choice_list.settings.allows_multiple_choices,
            _ => false,
        }
    }

    pub fn is_select_one(&self) -> bool {
        match self {
            Self::ChoiceList { choice_list, .. } => !choice_list.settings.allows_multiple_choices,
            _ => false,
        }
    }
}

#[derive(Debug, Deserialize)]
pub struct ChoiceList {
    choices: Vec<Choice>,
    settings: Settings,
}

impl ChoiceList {
    pub fn as_strs(&self) -> impl Iterator<Item = String> + '_ {
        self.choices
            .iter()
            .map(|c| normalize_surveyhero_text(c.label.as_str()))
    }

    pub fn mismatched_answers<'a>(&'a self, answers: &'a [&str]) -> Vec<(String, Cow<str>)> {
        self.as_strs()
            .zip(answers.iter().map(|s| normalize_markdown_text(s)))
            .filter(|(s1, s2)| s1 != s2)
            .collect()
    }
}

#[derive(Debug, Deserialize)]
pub struct ChoiceTable {
    rows: Vec<Row>,
    choices: Vec<Choice>,
}

impl ChoiceTable {
    pub fn column_strs(&self) -> impl Iterator<Item = String> + '_ {
        self.choices
            .iter()
            .map(|c| normalize_surveyhero_text(c.label.as_str()))
    }

    pub fn rows_strs(&self) -> impl Iterator<Item = String> + '_ {
        self.rows
            .iter()
            .map(|c| normalize_surveyhero_text(c.label.as_str()))
    }

    pub fn mismatched_rows<'a>(&'a self, labels: &[&'a str]) -> Vec<(String, Cow<str>)> {
        self.rows_strs()
            .zip(labels.iter().map(|s| normalize_markdown_text(s)))
            .filter(|(s1, s2)| s1 != s2)
            .collect()
    }

    pub fn mismatched_columns<'a>(&'a self, choices: &'a [&str]) -> Vec<(String, Cow<str>)> {
        self.column_strs()
            .zip(choices.iter().map(|s| normalize_markdown_text(s)))
            .filter(|(s1, s2)| s1 != s2)
            .collect()
    }
}
#[derive(Debug, Deserialize)]
pub struct Row {
    label: String,
}

#[derive(Debug, Deserialize)]
pub struct Choice {
    label: String,
}

#[derive(Debug, Deserialize)]
pub struct Settings {
    allows_multiple_choices: bool,
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

fn normalize_surveyhero_text(text: &str) -> String {
    static LINK_REGEX: LazyLock<Regex> =
        LazyLock::new(|| Regex::new(r#"<a href="(?<link>.*?)".*?>(?<text>.*?)</a>"#).unwrap());

    let text = text
        .replace("&amp;", "&")
        .replace("&nbsp;", " ")
        .replace("&lt;", "<");

    // Replace <a href="$link" ...>$text</a> with [$text]($link)
    LINK_REGEX.replace_all(&text, "[$text]($link)").to_string()
}

fn normalize_markdown_text(text: &str) -> Cow<str> {
    static ITALICS_REGEX: LazyLock<Regex> =
        LazyLock::new(|| Regex::new(r"(\*(?<text>\w+)\*)").unwrap());

    // Remove (open response) from the end of the Markdown text
    let answer = text
        .strip_suffix("(open response)")
        .map(|t| t.trim_end())
        .unwrap_or(text);

    // Replace *foo* with <em>foo</em>
    ITALICS_REGEX.replace_all(answer, "<em>$text</em>")
}
