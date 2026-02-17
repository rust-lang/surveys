use clap::Parser;
use typst_pdf::PdfOptions;

mod cli;
// mod markdown;
mod question_parser;
mod typst_wrapper;

fn main() -> anyhow::Result<()> {
    let cli = cli::Cli::parse();
    match &cli.command {
        cli::Command::Typst {
            question_path,
            report_path,
            template_path,
        } => {
            let markdown = std::fs::read_to_string(question_path)?;
            let typst = question_parser::TypstWriter::typst_from_markdown(&markdown)?;
            let dist = std::env::current_dir()?.join("dist");
            let mut template = std::fs::read_to_string(template_path)?;
            std::fs::create_dir_all(&dist)?;
            std::fs::write(dist.join("output.typ"), &typst)?;
            let main_doc = std::fs::read_to_string(report_path.canonicalize()?)?;
            template.push_str(&main_doc);
            template.push_str(&typst);
            std::fs::write(dist.join("main.typ"), &template)?;
            let world = typst_wrapper::Typst::new(
                template_path
                    .parent()
                    .unwrap_or(&std::env::current_dir()?)
                    .to_path_buf(),
                &template,
            );
            let doc = typst::compile(&world).output.unwrap();
            let pdf = typst_pdf::pdf(&doc, &PdfOptions::default()).expect("Error exporting PDF");
            std::fs::write(dist.join("main.pdf"), &pdf)?;
        }
    }
    Ok(())
}
