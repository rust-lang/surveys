use std::{error::Error, vec};

pub fn parse<'a>(markdown: &'a str) -> Result<Vec<Question<'a>>, Box<dyn Error>> {
    let mut questions = Vec::new();
    #[derive(Debug)]
    enum State<'a> {
        // We are starting from nothing
        None,
        // We have the question text and now need answers
        Text(&'a str),
        // building up the question with answers
        Question(Question<'a>),
        // Got the text for a matrix question
        HalfMatrixText(&'a str),
        // On the first half of a matrix question
        HalfMatrix {
            text: &'a str,
            label: &'a str,
            answers: Vec<&'a str>,
        },
    }
    let mut state = State::None;
    macro_rules! bail {
        ($($args : tt) *) => {
            return Err(format!("markdown error: {}", format_args!($($args)*)).into())
        };
    }
    for line in markdown
        .lines()
        .map(|l| l.trim())
        .filter(|l| !l.is_empty())
        .filter(|l| !l.starts_with(">"))
    {
        if line.starts_with("###") {
            let old_state = std::mem::replace(&mut state, State::Text(&line[3..].trim()));
            match old_state {
                State::Question(q) if !q.is_empty() => questions.push(q),
                State::None => {}
                State::Text(q) => bail!("question without answers '{}'", q),
                State::Question(q) => bail!("question without answers '{}'", q.text),
                State::HalfMatrixText(q) => {
                    bail!("question without answers '{}'", q)
                }
                State::HalfMatrix {
                    answers, text: q, ..
                } if answers.is_empty() => {
                    bail!("question without answers '{}'", q)
                }
                State::HalfMatrix { text: q, .. } => {
                    bail!("matrix question without second half of answers '{}'", q)
                }
            }
        } else if line.starts_with("Type: ") {
            if let State::Text(text) = state {
                let typ = &line[6..].trim();
                state = if typ.starts_with("select one") {
                    State::Question(Question {
                        text,
                        answers: Answers::SelectOne(vec![]),
                    })
                } else if typ.starts_with("free form") {
                    State::Question(Question {
                        text,
                        answers: Answers::FreeForm,
                    })
                } else if typ.starts_with("select all that apply") {
                    State::Question(Question {
                        text,
                        answers: Answers::SelectMany(vec![]),
                    })
                } else if typ.starts_with("matrix") {
                    State::HalfMatrixText(text)
                } else {
                    bail!("illegal question type: type='{}' question='{}'", typ, text);
                }
            } else {
                bail!(
                    "illegal parser state: found type when state is '{:?}'",
                    state
                );
            }
        } else if line.starts_with("-") {
            match &mut state {
                State::Question(Question {
                    answers: Answers::SelectOne(ref mut a),
                    ..
                }) => a.push(line[1..].trim()),
                State::Question(Question {
                    answers: Answers::SelectMany(ref mut a),
                    ..
                }) => a.push(line[1..].trim()),
                State::Question(Question {
                    answers:
                        Answers::Matrix {
                            ref mut answers2, ..
                        },
                    ..
                }) => {
                    answers2.push(line[1..].trim());
                }
                State::HalfMatrix { answers, .. } => {
                    answers.push(line[1..].trim());
                }
                _ => {
                    //     bail!("illegal state. found answer when state is {:?}", state)
                }
            }
        } else if line.starts_with("REPEAT") {
            let previous = questions.last().ok_or_else(|| {
                format!(
                    "question repeats previous answer but there is no previous question '{}'",
                    "TODO"
                )
            })?;
            state = match (state, &previous.answers) {
                (
                    State::HalfMatrixText(q),
                    Answers::Matrix {
                        label1, answers1, ..
                    },
                ) => State::HalfMatrix {
                    text: q,
                    label: label1,
                    answers: answers1.clone(),
                },
                (
                    State::HalfMatrix {
                        text,
                        label,
                        answers,
                    },
                    Answers::Matrix {
                        label1, answers1, ..
                    },
                ) if answers.is_empty() && *label1 == label => State::HalfMatrix {
                    text,
                    label,
                    answers: answers1.clone(),
                },
                (
                    State::Question(Question {
                        text,
                        answers: Answers::SelectMany(a1),
                    }),
                    new,
                ) if a1.is_empty() => State::Question(Question {
                    text,
                    answers: new.clone(),
                }),
                (state, _) => bail!(
                    "unexpected placement of the REPEAT keyword. State={:?}",
                    state
                ),
            };
        } else if line.ends_with(":") {
            state = match state {
                State::HalfMatrixText(q) => State::HalfMatrix {
                    text: q,
                    label: line,
                    answers: vec![],
                },
                State::HalfMatrix {
                    text,
                    label,
                    answers,
                } if !answers.is_empty() => State::Question(Question {
                    text,
                    answers: Answers::Matrix {
                        label1: label,
                        label2: line,
                        answers1: answers,
                        answers2: vec![],
                    },
                }),
                State::HalfMatrix { text, .. } => {
                    bail!("matrix question has no answers in first section '{}'", text)
                }
                _ => state,
            };
        } else {
            log::warn!("Unhandled line: {}", line);
        }
    }
    Ok(questions)
}

#[derive(Debug)]
pub struct Question<'a> {
    pub text: &'a str,
    pub answers: Answers<'a>,
}

impl<'a> Question<'a> {
    fn is_empty(&self) -> bool {
        self.answers.is_empty()
    }
}

#[derive(Debug, Clone)]
pub enum Answers<'a> {
    FreeForm,
    SelectOne(Vec<&'a str>),
    SelectMany(Vec<&'a str>),
    Matrix {
        label1: &'a str,
        answers1: Vec<&'a str>,
        label2: &'a str,
        answers2: Vec<&'a str>,
    },
}

impl Answers<'_> {
    fn is_empty(&self) -> bool {
        match self {
            Self::SelectOne(a) => a.is_empty(),
            Self::SelectMany(a) => a.is_empty(),
            Self::Matrix {
                answers1, answers2, ..
            } => answers1.is_empty() || answers2.is_empty(),
            Self::FreeForm => false,
        }
    }
}
