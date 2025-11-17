use regex::Regex;
use reqwest::blocking::Client as Reqwest;
use serde::Deserialize;
use std::sync::LazyLock;
use std::time::{Duration, SystemTime};

pub struct Client {
    username: String,
    password: String,
    inner: Reqwest,
    last_request: Option<SystemTime>,
}

impl Client {
    pub fn new(username: String, password: String) -> Self {
        let inner = Reqwest::new();
        Self {
            username,
            password,
            inner,
            last_request: None,
        }
    }

    pub fn fetch_surveys(&mut self) -> anyhow::Result<Vec<Survey>> {
        self.rate_limit();
        let response = self
            .inner
            .get("https://api.surveyhero.com/v1/surveys")
            .basic_auth(&self.username, Some(&self.password))
            .send()?;
        let status = response.status();
        if !status.is_success() {
            let text = response.text()?;
            return Err(anyhow::anyhow!(
                "HTTP error status {status} while fetching surveys:\n{text}"
            ));
        }
        let surveys: Surveys = response.json()?;
        Ok(surveys.surveys)
    }

    pub fn fetch_secondary_languages(&mut self, survey_id: usize) -> anyhow::Result<Vec<Language>> {
        self.rate_limit();
        let response = self
            .inner
            .get(format!(
                "https://api.surveyhero.com/v1/surveys/{survey_id}/languages"
            ))
            .basic_auth(&self.username, Some(&self.password))
            .send()?
            .error_for_status()?;
        let surveys: Languages = response.json()?;
        Ok(surveys
            .languages
            .into_iter()
            .filter(|l| !l.is_default && l.is_active)
            .collect())
    }

    pub fn fetch_questions(
        &mut self,
        survey_id: usize,
        language: Option<String>,
    ) -> anyhow::Result<Vec<Question>> {
        self.rate_limit();
        let response = self
            .inner
            .get(format!(
                "https://api.surveyhero.com/v1/surveys/{}/questions{}",
                survey_id,
                language.map(|l| format!("?lang={l}")).unwrap_or_default()
            ))
            .basic_auth(&self.username, Some(&self.password))
            .send()?
            .error_for_status()?;

        let text = response.text()?;
        let elements: Elements = serde_json::from_str(&text).map_err(|e| {
            anyhow::anyhow!("Cannot deserialize questions from:\n{text}\nError:{e:?}")
        })?;
        Ok(elements.questions().collect())
    }

    // TODO: Get all elements from survey
    // filter "text" and "question" type
    fn fetch_elements(
        &mut self,
        survey_id: usize,
        language: Option<String>,
    ) -> anyhow::Result<Vec<Element>> {
        self.rate_limit();
        let response = self
            .inner
            .get(format!(
                "https://api.surveyhero.com/v1/surveys/{}/elements{}",
                survey_id,
                language.map(|l| format!("?lang={l}")).unwrap_or_default()
            ))
            .basic_auth(&self.username, Some(&self.password))
            .send()?
            .error_for_status()?;

        let elements: Elements = response.json()?;

        let elements = vec![Element::Text {
            text: "TODO".to_string(),
        }];
        Ok(elements)
    }

    // Try to avoid 429 errors by rate limiting the client
    fn rate_limit(&mut self) {
        if let Some(last) = self.last_request {
            let elapsed = last.elapsed().unwrap();
            let limit = Duration::from_secs(1);
            if elapsed < limit {
                std::thread::sleep((limit - elapsed) + Duration::from_millis(100));
            }
        }
        self.last_request = Some(SystemTime::now());
    }
}

#[derive(Debug, Deserialize)]
struct Languages {
    languages: Vec<Language>,
}

#[derive(Debug, Deserialize)]
pub struct Language {
    pub code: String,
    is_default: bool,
    is_active: bool,
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
    #[serde(rename = "text")]
    Text { text: String },
    #[serde(rename = "question")]
    Question { question: Question },
    #[serde(other)]
    Unknown,
}

#[derive(Debug, Deserialize)]
#[serde(tag = "type")]
pub enum Question {
    #[serde(rename = "choice_list")]
    ChoiceList {
        question_text: String,
        description_text: String,
        choice_list: ChoiceList,
    },
    #[serde(rename = "input")]
    Input {
        question_text: String,
        description_text: String,
    },
    #[serde(rename = "choice_table")]
    ChoiceTable {
        question_text: String,
        description_text: String,
        choice_table: ChoiceTable,
    },
    #[serde(rename = "rating_scale")]
    RatingScale {
        question_text: String,
        description_text: String,
    },
    #[serde(rename = "ranking")]
    Ranking {
        question_text: String,
        description_text: String,
        ranking: RankingChoices,
    },
    #[serde(rename = "input_list")]
    InputList {
        question_text: String,
        description_text: String,
        input_list: InputListInputs,
    },
}

impl Question {
    pub fn text(&self) -> String {
        normalize_surveyhero_text(match self {
            Self::ChoiceList { question_text, .. } => question_text,
            Self::Input { question_text, .. } => question_text,
            Self::ChoiceTable { question_text, .. } => question_text,
            Self::RatingScale { question_text, .. } => question_text,
            Self::Ranking { question_text, .. } => question_text,
            Self::InputList { question_text, .. } => question_text,
        })
    }

    pub fn description_text(&self) -> String {
        normalize_surveyhero_text(match self {
            Self::ChoiceList {
                description_text, ..
            } => &description_text,
            Self::Input {
                description_text, ..
            } => description_text,
            Self::ChoiceTable {
                description_text, ..
            } => description_text,
            Self::RatingScale {
                description_text, ..
            } => description_text,
            Self::Ranking {
                description_text, ..
            } => description_text,
            Self::InputList {
                description_text, ..
            } => description_text,
        })
    }

    pub fn is_free_form(&self) -> bool {
        matches!(self, Self::Input { .. })
    }

    pub fn is_select_many(&self) -> bool {
        match self {
            Self::ChoiceList { choice_list, .. } => choice_list.settings.allows_multiple_choices,
            Self::Ranking { .. } => true,
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
    pub settings: Settings,
}

impl ChoiceList {
    pub fn as_strs(&self) -> impl Iterator<Item = String> + '_ {
        self.choices
            .iter()
            .map(|c| normalize_surveyhero_text(c.label.as_str()))
    }

    pub fn mismatched_answers<'a>(&'a self, answers: &'a [&str]) -> Vec<(String, &'a str)> {
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

    pub fn mismatched_rows<'a>(&'a self, labels: &[&'a str]) -> Vec<(String, &'a str)> {
        self.rows_strs()
            .zip(labels.iter().map(|s| normalize_markdown_text(s)))
            .filter(|(s1, s2)| s1 != s2)
            .collect()
    }

    pub fn mismatched_columns<'a>(&'a self, choices: &'a [&str]) -> Vec<(String, &'a str)> {
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
pub struct RankingChoices {
    choices: Vec<ChoiceWithLabel>,
}

impl RankingChoices {
    pub fn as_strs(&self) -> impl Iterator<Item = String> + '_ {
        self.choices
            .iter()
            .map(|c| normalize_surveyhero_text(c.label.as_str()))
    }

    pub fn mismatched_answers<'a>(&'a self, answers: &'a [&str]) -> Vec<(String, &'a str)> {
        self.as_strs()
            .zip(answers.iter().map(|s| normalize_markdown_text(s)))
            .filter(|(s1, s2)| s1 != s2)
            .collect()
    }
}

#[derive(Debug, Deserialize)]
pub struct ChoiceWithLabel {
    label: String,
}

#[derive(Debug, Deserialize)]
pub struct InputListInputs {
    inputs: Vec<ChoiceWithLabel>,
}

impl InputListInputs {
    pub fn as_strs(&self) -> impl Iterator<Item = String> + '_ {
        self.inputs
            .iter()
            .map(|c| normalize_surveyhero_text(c.label.as_str()))
    }

    pub fn mismatched_answers<'a>(&'a self, answers: &'a [&str]) -> Vec<(String, &'a str)> {
        self.as_strs()
            .zip(answers.iter().map(|s| normalize_markdown_text(s)))
            .filter(|(s1, s2)| s1 != s2)
            .collect()
    }
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

pub fn normalize_surveyhero_text(text: &str) -> String {
    static LINK_REGEX: LazyLock<Regex> =
        LazyLock::new(|| Regex::new(r#"<a href="(?<link>.*?)".*?>(?<text>.*?)</a>"#).unwrap());
    static ITALICS_REGEX: LazyLock<Regex> =
        LazyLock::new(|| Regex::new(r"<em>(?<text>.*?)</em>").unwrap());
    static BOLD_REGEX: LazyLock<Regex> =
        LazyLock::new(|| Regex::new(r"<strong>(?<text>.*?)</strong>").unwrap());

    let text = text
        .replace("&quot;", "\"")
        .replace("&amp;", "&")
        .replace("&nbsp;", " ")
        .replace("&lt;", "<")
        .replace("&gt;", ">")
        // Note: we leave manually inserted newlines
        // Unwanted newlines should be fixed on SurveyHero
        .replace("<br>", "\n")
        .replace("\u{202f}", " ")
        .replace("\u{200b}", "")
        .replace("&#39;", "’");

    // Replace <a href="$link" ...>$text</a> with [$text]($link)
    let text = LINK_REGEX.replace_all(&text, "[$text]($link)");

    // Replace <em>$text</em> with *$text* and
    // Replace <strong>$text</strong> with **$text**
    let text = ITALICS_REGEX.replace_all(&text, "*$text*").to_string();
    BOLD_REGEX.replace_all(&text, "**$text**").to_string()
}

fn normalize_markdown_text(text: &str) -> &str {
    // Remove (open response) from the end of the Markdown text
    text.strip_suffix("(open response)")
        .map(|t| t.trim_end())
        .unwrap_or(text)
}
