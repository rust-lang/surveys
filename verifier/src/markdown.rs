pub fn parse<'a>(markdown: &'a str) -> Vec<Question<'a>> {
    let mut questions = Vec::new();
    #[derive(Debug)]
    enum State<'a> {
        None,
        Text(&'a str),
        Question(Question<'a>),
    }
    let mut state = State::None;
    for line in markdown
        .lines()
        .map(|l| l.trim())
        .filter(|l| !l.is_empty())
        .filter(|l| !l.starts_with(">"))
    {
        if line.starts_with("###") {
            assert!(
                matches!(state, State::None)
                    || matches!(state, State::Question(ref q) if !q.is_empty()),
                "illegal state: {:?}",
                state
            );
            let old_state = std::mem::replace(&mut state, State::Text(&line[3..].trim()));
            if let State::Question(q) = old_state {
                questions.push(q);
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
                    State::Question(Question {
                        text,
                        answers: Answers::Matrix(vec![], vec![]),
                    })
                } else {
                    panic!("Illegal type: {}", typ);
                }
            } else {
                panic!("Illegal state: {:?}", state);
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
                    answers: Answers::Matrix(ref mut a, ref mut b),
                    ..
                }) => {
                    a.push(line[1..].trim());
                    b.push(line[1..].trim());
                }
                _ => {}
            }
        } else if line.starts_with("*Same answers as above*") {
            println!("TODO: Handle same answers as above");
            state = State::None;
        } else {
            println!("Unhandled line: {}", line);
        }
    }
    questions
}

#[derive(Debug)]
pub struct Question<'a> {
    text: &'a str,
    answers: Answers<'a>,
}

impl<'a> Question<'a> {
    fn is_empty(&self) -> bool {
        self.answers.is_empty()
    }
}

#[derive(Debug)]
enum Answers<'a> {
    FreeForm,
    SelectOne(Vec<&'a str>),
    SelectMany(Vec<&'a str>),
    Matrix(Vec<&'a str>, Vec<&'a str>),
}

impl Answers<'_> {
    fn is_empty(&self) -> bool {
        match self {
            Self::SelectOne(a) => a.is_empty(),
            Self::SelectMany(a) => a.is_empty(),
            Self::Matrix(a, b) => a.is_empty() || b.is_empty(),
            Self::FreeForm => false,
        }
    }
}
