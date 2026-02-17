use std::path::PathBuf;

#[derive(clap::Parser, Clone)]
pub struct Cli {
    #[clap(subcommand)]
    pub command: Command,
}

#[derive(clap::Subcommand, Clone)]
pub enum Command {
    /// Generate typst from markdown
    Typst {
        /// Path to markdown file
        #[clap(long, short)]
        question_path: PathBuf,

        /// Path to textual report .typst file
        #[clap(long, short)]
        report_path: PathBuf,

        #[clap(long, short)]
        template_path: PathBuf,
    },
}
