use anyhow::Context;
use clap::Parser;
use similar::ChangeTag;
use std::io::ErrorKind;
use std::path::PathBuf;
use surveyhero::api::Question;
use surveyhero::cli::Args;
use surveyhero::render::render_questions;
use surveyhero::{cli::VerifierCmd, fetch_surveyhero_data, markdown, Comparison};

fn main() -> anyhow::Result<()> {
    env_logger::init();

    let args = Args::parse();
    let online_data = fetch_surveyhero_data(args.cmd.shared())?;

    let base_path = PathBuf::from(format!("../surveys/{}", args.cmd.shared().path));
    let pairs = if base_path.is_dir() {
        let mut pairs = vec![(base_path.join("questions.md"), online_data.main)];
        for (language, questions) in online_data.secondary_languages {
            pairs.push((
                base_path
                    .join("translations")
                    .join(language)
                    .with_extension("md"),
                questions,
            ));
        }
        pairs
    } else {
        vec![(base_path, online_data.main)]
    };

    match args.cmd {
        VerifierCmd::Check { .. } => {
            for (path, questions) in pairs {
                println!("-----\nChecking {}\n", path.display());

                let markdown = match std::fs::read_to_string(&path) {
                    Ok(markdown) => markdown,
                    Err(error) if error.kind() == ErrorKind::NotFound => {
                        eprintln!(
                            "{} not found, creating it with data from SurveyHero",
                            path.display()
                        );
                        render_questions(&questions, &path)?;
                        std::fs::read_to_string(&path)?
                    }
                    Err(e) => return Err(e.into()),
                };
                let markdown_questions = markdown::parse(&markdown)
                    .with_context(|| format!("Cannot parse {} as Markdown", path.display()))?;
                check_questions(&markdown_questions, &questions);
            }
        }
        VerifierCmd::Download { .. } => {
            for (path, questions) in pairs {
                // Do not overwrite the English version, as it contains special metadata and
                // comments
                if path
                    .file_name()
                    .map(|p| p != "questions.md")
                    .unwrap_or(true)
                {
                    render_questions(&questions, &path)?;
                }
            }
        }
    }

    Ok(())
}

fn check_questions(markdown_questions: &[markdown::Question], sh_questions: &[Question]) {
    for (online, markdown) in markdown_questions.iter().zip(sh_questions.iter()) {
        let comparison = online.compare(markdown);
        if !matches!(comparison, Comparison::Equal) {
            println!("Q: '{}'", online.text);
            match comparison {
                Comparison::DescriptionsDiffer { md, sh, .. } => {
                    println!("(Old: Markdown, new: SurveyHero)\n");
                    let diff = similar::TextDiff::configure().diff_lines(md, sh);
                    for change in diff.iter_all_changes() {
                        let sign = match change.tag() {
                            ChangeTag::Delete => "-",
                            ChangeTag::Insert => "+",
                            ChangeTag::Equal => " ",
                        };
                        print!("{sign}{change}");
                    }
                }
                c => println!("  {c:#?}"),
            }
        }
    }

    if markdown_questions.len() > sh_questions.len() {
        println!(
            "Missing questions in the online version:\n{}",
            markdown_questions[sh_questions.len()..]
                .iter()
                .map(|q| q.text)
                .collect::<Vec<_>>()
                .join("\n-")
        );
    }
    if sh_questions.len() > markdown_questions.len() {
        println!(
            "Missing questions in the markdown version:\n-{}",
            sh_questions[markdown_questions.len()..]
                .iter()
                .map(|q| q.text())
                .collect::<Vec<_>>()
                .join("\n-")
        );
    }
}
