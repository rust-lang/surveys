use crate::api::Question;
use std::io;
use std::io::Write;
use std::path::Path;

#[allow(unused)]
pub fn render_questions(questions: &[Question], file: &Path) -> io::Result<()> {
    eprintln!("Rendering {}", file.display());

    std::fs::create_dir_all(file.parent().unwrap())?;

    let mut file = std::fs::File::create(file)?;
    for question in questions {
        writeln!(file, "### {}\n", question.text())?;
        if !question.description_text().is_empty() {
            writeln!(file, "{}\n", question.description_text())?;
        }
        match question {
            Question::Input { .. } => {
                writeln!(file, "Type: free form")?;
            }
            Question::ChoiceList { choice_list, .. } => {
                if question.is_select_one() {
                    writeln!(file, "Type: select one")?;
                } else {
                    writeln!(file, "Type: select all that apply")?;
                }
                writeln!(file)?;

                for variant in choice_list.as_strs() {
                    writeln!(file, "- {variant}")?;
                }
            }
            Question::ChoiceTable { choice_table, .. } => {
                writeln!(file, "Type: matrix\n")?;
                writeln!(file, "Rows:\n")?;
                for row in choice_table.rows_strs() {
                    writeln!(file, "- {row}")?;
                }
                writeln!(file, "\nColumns:\n")?;
                for col in choice_table.column_strs() {
                    writeln!(file, "- {col}")?;
                }
            }
            Question::RatingScale { .. } => {
                writeln!(file, "Type: rating scale\n")?;
            }
            Question::Ranking { ranking, .. } => {
                writeln!(file, "Type: ranking\n")?;
                for variant in ranking.as_strs() {
                    writeln!(file, "- {variant}")?;
                }
            }
            Question::InputList { input_list, .. } => {
                writeln!(file, "Type: input list\n")?;
                for input in input_list.as_strs() {
                    writeln!(file, "- {input}")?;
                }
            }
        }
        writeln!(file)?;
    }
    Ok(())
}
