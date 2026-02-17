use std::fmt::Write;
use surveyhero::markdown::{Answers, parse};

const FONT_PRELUDE: &str = r#"
#set text(
  font: "TeX Gyre Pagella",
)
"#;

pub struct TypstWriter;

impl TypstWriter {
    pub fn typst_from_markdown(markdown: &str) -> anyhow::Result<String> {
        let questions = parse(markdown)?;
        let mut buf = String::new();
        buf.write_str(FONT_PRELUDE)?;
        Self::write_md(&questions, &mut buf)?;
        Ok(buf)
    }
    pub fn write_md(
        questions: &[surveyhero::markdown::Question],
        buf: &mut impl Write,
    ) -> anyhow::Result<()> {
        writeln!(buf, "= Survey Questions and Answers\n")?;
        for question in questions {
            Self::write_md_question(question, buf)?;
        }
        Ok(())
    }
    fn write_md_question(
        question: &surveyhero::markdown::Question,
        buf: &mut impl Write,
    ) -> anyhow::Result<()> {
        writeln!(buf, "== {}\n", question.text)?;
        match &question.answers {
            Answers::Matrix {
                label1,
                answers1,
                answers2,
            } => {
                writeln!(buf, "Type: matrix\n")?;
                writeln!(buf, "Tag: {label1}")?;
                writeln!(buf, "Rows:\n")?;
                for row in answers1 {
                    writeln!(buf, "- {row}")?;
                }
                writeln!(buf, "\nColumns:\n")?;
                for col in answers2 {
                    writeln!(buf, "- {col}")?;
                }
            }
            Answers::FreeForm => {
                writeln!(buf, "Type: free form")?;
            }
            Answers::SelectOne(variants) => {
                writeln!(buf, "Type: select one")?;
                for variant in variants {
                    writeln!(buf, "- {variant}")?;
                }
            }
            Answers::SelectMany(variants) => {
                writeln!(buf, "Type: select all that apply")?;
                for variant in variants {
                    writeln!(buf, "- {variant}")?;
                }
            }
            Answers::RatingScale { .. } => {
                writeln!(buf, "Type: rating scale\n")?;
            }
            Answers::Ranking(rankings) => {
                writeln!(buf, "Type: ranking\n")?;
                for variant in rankings {
                    writeln!(buf, "- {variant}")?;
                }
            }
            Answers::InputList(inputs) => {
                writeln!(buf, "Type: input list\n")?;
                for input in inputs {
                    writeln!(buf, "- {input}")?;
                }
            }
        }
        writeln!(buf)?;
        Ok(())
    }
}
