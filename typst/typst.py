#!/usr/bin/env python3

import argparse
import os
import subprocess
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "command",
        choices=[
            "typst",
        ],
    )
    parser.add_argument(
        "--question-path",
        type=str,
    )
    parser.add_argument(
        "--report-path",
        type=str,
    )
    parser.add_argument(
        "-o",
        "--output-dir",
        type=str,
        default="dist",
    )

    parser.add_argument(
        "--template-path",
        type=Path,
        default=Path.cwd().joinpath("template/template.typ"),
    )

    args = parser.parse_args()
    if args.command == "typst":
        if not args.question_path:
            print("Error: question-path is required")
            sys.exit(1)
        if not args.report_path:
            print("Error: report-path is required")
            sys.exit(1)

        pandoc_out_dir = os.path.join(args.output_dir, "pandoc")
        os.makedirs(pandoc_out_dir, exist_ok=True)
        subprocess.run(
            [
                "pandoc",
                args.report_path,
                "--output",
                os.path.join(pandoc_out_dir, "report.typ"),
            ],
            check=True,
        )
        typst_gen_path = os.getenv("TYPST_GEN_PATH", "./typst_gen/")
        cargo_out = subprocess.run(
            [
                "cargo",
                "build",
                "--release",
                "--manifest-path",
                typst_gen_path + "Cargo.toml",
            ]
        )
        if cargo_out.returncode != 0:
            sys.exit(cargo_out.returncode)
        typst_gen_target = typst_gen_path + "target/release/typst_gen"
        subprocess.run(
            [
                typst_gen_target,
                "typst",
                "--question-path",
                args.question_path,
                "--report-path",
                os.path.join(pandoc_out_dir, "report.typ"),
                "--template-path",
                args.template_path,
            ]
        )


if __name__ == "__main__":
    main()
