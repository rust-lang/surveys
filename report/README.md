# Survey report scripts
This directory contains scripts that automate the generation of charts, reports and Rust Blog posts that analyse
surveys created in SurveyHero.

Note that these scripts are intended to be used as a library, so you will need to write your own script to leverage them.
It is best to take a look at their usage from previous surveys, and start with that. The scripts will change over time, they are only kept compatible with the latest version of the annual survey. If you need to re-render the reports from an older survey, you should use an older version of these scripts from the corresponding year.

Requirement to run these scripts are the CSV files with the survey actual data:
- The `summary.csv` in `./data/data-YYYY.csv`
- The `responses.csv` in `./data/data-full-YYYY.csv`

# Build and install
Install [uv](https://docs.astral.sh/uv/getting-started/installation/).

Then run `uv sync` to initialize a virtual environment, and add this directory to the `PYTHONPATH` of your main Python script, and then use e.g. `from surveyhero.parser import parse_surveyhero_report`.

You can then execute your analysis scripts using `uv run <script>`.

Here's a practical list of commands to run:
```
$ cd report
$ uv venv --clear
$ source .venv/bin/activate
(report) $ uv sync
(report) $ cd ../surveys/2025/annual-survey/report
(report) $ python3 main.py [ --skip-pdf ]
```

The parameter `--skip-pdf` will skip creating the PDF report and will only build the blog post.

Note: the blog post will embed Plotly Basic v2.29 (downloaded when you run the `main.py` script). Upgrading this library is not supported and may cause breaking changes.
Documentation for the Plotly Python library (used in `report/surveyhero/chart.py`): https://plotly.com/python-api-reference
Documentation for the Plotly JavaScript library: https://plotly.com/javascript

## Useful functions
First, you will probably want to export data from SurveyHero into two CSV files - one containing the aggregated data from
the report, and a second one that contains the individual answers from all the respondents.

Then you should use `parser.py:parse_surveyhero_report` to parse the report CSV, and `parser.py:parse_surveyhero_answers`
to parse the full answer CSV (if needed). Once you do that, you can start to build a `ChartReport` (located in `report.py`),
by adding various charts to it with the provided helper methods. The charts are created out of `Question`s that you can
access from the parsed CSVs.

Once you create fill a `ChartReport` with charts, you can use it to render a PDF report using the `render.py:render_report_to_pdf`
function, or to render a Rust Blog post template using the `render.py:render_blog_post` function. See the documentation
of these two functions for more details.
