# Survey report scripts
This directory contains scripts that automate the generation of charts, reports and Rust Blog posts that analyse
surveys created in SurveyHero.

Note that these scripts are intended to be used as a library, so you will need to write your own script to leverage them.
It is best to take a look at their usage from previous surveys, and start with that. The scripts will change over time, they are only kept compatible with the latest version of the annual survey. If you need to re-render the reports from an older survey, you should use an older version of these scripts from the corresponding year.

# Build and install

First install system dependencies, the development packages for `libxml2`, `libxslt1`, `zlib1g`, `libjpeg` and python3. For Debian is for example:
``` bash
sudo apt install libxml2-dev libxslt1-dev zlib1g-dev libjpeg-dev libpython3-dev
```

Ensure you have Python 3.8 installed (last minor release is 3.8.20). Specifically an old version of the `lxml` library is used and due to [this bug](https://bugs.launchpad.net/lxml/+bug/1973155) an accordingly old version of Python is required. If your distribution does not ship anymore with Python 3.8.x you'll have to compile it yourself ([instructions](https://stackoverflow.com/a/62831268)).

To use the scripts, you should install their dependencies first:
```bash
$ python3 -m venv venv
$ source venv/venv/bin/activate
(venv) $ pip install -U setuptools wheel pip
(venv) $ pip install -r requirements.txt
```

Also ensure to install the Pillow library (this step fixes a ValueError "WordCloud Only Supported for TrueType fonts")
```bash
(venv) $ pip install -U pillow
```

and then add this directory to the `PYTHONPATH` of your main Python script, and then use e.g. `from surveyhero.parser import parse_surveyhero_report`.

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
