use crate::api::{normalize_surveyhero_text, Question};
use std::io;
use std::io::Write;
use std::path::Path;

#[allow(unused)]
pub fn render_questions(questions: &[Question], file: &Path) -> io::Result<()> {
    eprintln!("Rendering {}", file.display());

    std::fs::create_dir_all(file.parent().unwrap())?;

    let mut file = std::fs::File::create(file)?;
    for question in questions {
        writeln!(file, "### {}\n", normalize_surveyhero_text(question.text()))?;
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
                writeln!(file, "Rows\n\n")?;
                for row in choice_table.rows_strs() {
                    writeln!(file, "- {row}")?;
                }
                writeln!(file, "\nColumns\n\n")?;
                for col in choice_table.column_strs() {
                    writeln!(file, "- {col}")?;
                }
            }
        }
        writeln!(file)?;
    }
    Ok(())
}
