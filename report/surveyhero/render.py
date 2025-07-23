import dataclasses
import io
import os
import re
import tempfile
import urllib.request
from pathlib import Path
from typing import Union, Tuple, Any

import tqdm
from PIL import Image
from bs4 import BeautifulSoup

from .report import ChartReport, PlotlyRenderer, PngRenderer, ChartRenderer

CHART_MARKER_REGEX = re.compile(r"<!-- chart: ([^ ]*)\s*(\([^)]*\))?\s*-->")


@dataclasses.dataclass(frozen=True)
class RenderedChart:
    script: str
    tag: str
    to_replace: str


def make_rel_path(image_dir: Path, path: Path) -> str:
    path = path.relative_to(image_dir.parent)
    return f"../../../images/{path}"


def render_png(image_dir: Path, renderer: ChartRenderer, chart_id: str) -> Path:
    png_bytes = renderer.to_image_bytes(format="png")
    png_bytes = optimize_png_image(png_bytes)
    png_path = image_dir / f"{chart_id}.png"
    with open(png_path, "wb") as f:
        f.write(png_bytes)
    return png_path


def render_blog_chart(arg) -> RenderedChart:
    (image_dir, report, match) = arg

    fullmatch = match[0]
    chart_id = match[1]
    if chart_id not in report.charts:
        raise Exception(f"Chart with ID `{chart_id}` was not found")
    chart = report.get_chart(chart_id)

    def normalize_arg(key, value) -> Tuple[str, Any]:
        value = int(value)
        if key == "xrange":
            key = "layout_args"
            value = dict(xaxis_range=(-1, value))
        return (key, value)

    # Skip ()
    args = match[2] or ""
    args = args[1:-1]
    args = args.split(",")
    args = dict(normalize_arg(*tuple(arg.split("="))) for arg in args if arg.strip())

    height = args.get("height", 600)

    # Render the chart as PNG and SVG
    png_path = render_png(image_dir=image_dir, renderer=chart, chart_id=chart_id)

    svg_bytes = chart.to_image_bytes(format="svg")
    svg_path = image_dir / f"{chart_id}.svg"
    with open(svg_path, "wb") as f:
        f.write(svg_bytes)

    if isinstance(chart, PlotlyRenderer):
        figure = chart.render_fn(**args)
        chart_type = figure.layout.meta
        element = BeautifulSoup(
            figure.to_html(
                full_html=False,
                include_plotlyjs=None,
                div_id=chart_id,
                config=dict(
                    modeBarButtonsToRemove=[
                        "zoom",
                        "pan",
                        "lasso2d",
                        "select",
                        "autoScale",
                        "toImage",
                    ],
                    displaylogo=False,
                ),
            ),
            features="html.parser",
        ).div
        div = element.find("div")
        div["class"] = chart_type
        div.append(
            BeautifulSoup(
                f"""<noscript>
    <img src="{make_rel_path(image_dir=image_dir, path=png_path)}" height="{height}" alt="{chart_id}" />
</noscript>""",
                "html.parser",
            )
        )

        links = [
            (
                make_rel_path(image_dir=image_dir, path=png_path),
                "Download chart as PNG",
                "PNG",
            ),
            (
                make_rel_path(image_dir=image_dir, path=svg_path),
                "Download chart as SVG",
                "SVG",
            ),
        ]

        wordcloud_id = f"{chart_id}-wordcloud"
        wordcloud = report.get_chart(wordcloud_id)
        if wordcloud is not None:
            wc_png_path = render_png(
                image_dir=image_dir, renderer=wordcloud, chart_id=wordcloud_id
            )
            links.append(
                (
                    make_rel_path(image_dir=image_dir, path=wc_png_path),
                    "Download open answers as wordcloud PNG",
                    "Wordcloud of open answers",
                )
            )

        links = [
            f"""<span>[<a href="{link}" target="_href_" title="{title}">{label}</a>]</span>"""
            for (link, title, label) in links
        ]
        tag = f"""<!-- Chart {chart_id} start -->
<div>
    {div}
    <div style="display: flex; margin-bottom: 10px;">
        {"&nbsp;".join(links)}
    </div>
</div>
<!-- Chart {chart_id} end -->"""

        script = element.find("script")
        assert script is not None

        return RenderedChart(script=script.text.strip(), tag=tag, to_replace=fullmatch)
    elif isinstance(chart, PngRenderer):
        assert False
    else:
        assert False


def render_blog_post(
        template: Path, blog_root: Path, resource_dir: str, report: ChartReport
):
    """
    Render a Rust Blog post containing special placeholders that will render as SurveyHero charts from the given `report`.

    The `template` should contain two things:
    1) A line containing `<!-- chart: <chart-id> -->` for each charts that should be rendered.
    The chart placeholder can contain optional key-value arguments that will be passed to the chart render function:
    ```
    <!-- chart: my-chart-1 (height=400) -->
    ```
    2) A line containing `<!-- scripts -->`, which will be replaced with all the generated JavaScript. It should be ideally
    at the end of the template.

    :param template: Blog post Markdown template. Its filename will be used to name the generated blog post file.
    :param blog_root: Local checkout of the https://github.com/rust-lang/blog.rust-lang.org repository
    :param resource_dir: Name of a directory in <blog_root/static/images> where the rendered charts will be stored.
    :param report: `ChartReport` containing charts that can be rendered.
    """
    output_path = blog_root / "posts" / template.name

    image_dir = blog_root / "static" / "images" / resource_dir
    image_dir.mkdir(parents=True, exist_ok=True)
    script_dir = blog_root / "static" / "scripts" / resource_dir
    script_dir.mkdir(parents=True, exist_ok=True)
    print(
        f"Generating blog post to {output_path}, image directory {image_dir}, scripts directory {script_dir}"
    )

    with open(template) as f:
        document = f.read()

    matches = list(CHART_MARKER_REGEX.finditer(document))

    args = [
        (image_dir, report, (match.group(0), match.group(1), match.group(2)))
        for match in matches
    ]

    import multiprocess as mp

    script_text = ""

    with mp.Pool() as pool:
        for result in tqdm.tqdm(pool.imap(render_blog_chart, args), total=len(args)):
            script_text += f"\n\n{result.script}"
            document = document.replace(result.to_replace, result.tag)

    # Helper JavaScript script that makes charts better visible on mobile phones
    script_text += """
function deepCopy(obj) {
    return JSON.parse(JSON.stringify(obj));
}

// Angle axis ticks and make bar chart labels vertical on small displays
function relayoutCharts() {
    if (window.innerWidth > 800) return;

    console.log("Relayouting charts");
    var bar_charts = document.getElementsByClassName("bar-chart");
    for (var i = 0; i < bar_charts.length; i++) {
        var chart = bar_charts[i];

        // We need to extract and copy the original layout, otherwise it would be lost
        // when relayouting.
        var layout = deepCopy(chart.layout);
        layout.xaxis.tickangle = 90;
        layout.autosize = false;
        layout.width = "100%";
        Plotly.relayout(chart, layout);
        Plotly.restyle(chart, {textangle: 90});
    }
    var matrix_charts = document.getElementsByClassName("matrix-chart");
    for (var i = 0; i < matrix_charts.length; i++) {
        var chart = matrix_charts[i];
        var layout = deepCopy(chart.layout);
        layout.autosize = false;
        layout.width = "100%";
        layout.legend.y = -0.3;
        layout.legend.yanchor = "bottom";
        Plotly.relayout(chart, layout);
    }
}

window.addEventListener("resize", relayoutCharts);
document.addEventListener("DOMContentLoaded", relayoutCharts);
"""
    script_path = script_dir / "charts.js"
    with open(script_path, "w") as f:
        f.write(script_text)

    plotly_script_path = script_dir.parent / "plotly-basic-2.29.0.min.js"
    if not os.path.isfile(plotly_script_path):
        urllib.request.urlretrieve(
            "https://cdn.plot.ly/plotly-basic-2.29.0.min.js", plotly_script_path
        )

    scripts = [
        '<script charset="utf-8" src="../../../scripts/plotly-basic-2.29.0.min.js"></script>',
        f'<script src="../../../scripts/{script_path.relative_to(script_dir.parent)}"></script>',
    ]

    script_marker = "<!-- scripts -->"
    if script_marker not in document:
        raise Exception(
            f"Please add `{script_marker}` to the (end of the) Markdown document"
        )
    script_str = "<!-- Chart scripts -->\n\n" + "\n\n".join(scripts)
    document = document.replace(script_marker, script_str)

    with open(output_path, "w") as f:
        f.write(document)


def render_pdf_page(args) -> Tuple[str, str, Union[str, bytes]]:
    report, name = args
    chart = report.get_chart(name)
    svg_bytes = chart.to_image_bytes(format="svg")
    if svg_bytes is not None:
        with tempfile.NamedTemporaryFile(suffix=".svg", delete=False) as f:
            f.write(svg_bytes)
            path = f.name
        return (name, "svg", path)
    else:
        png_bytes = chart.to_image_bytes(format="png")
        png_bytes = optimize_png_image(png_bytes)
        return (name, "png", png_bytes)


def render_report_to_pdf(
        report: ChartReport, output: Path, title: str, include_labels=False
):
    """
    Renders a PDF report containing all charts from the given `report` into the `output` path.
    """
    import nelsie

    # A4 format
    slides = nelsie.SlideDeck(width=595, height=842)
    slide = slides.new_slide()
    slide.text(title, align="center")

    print("Rendering charts")

    import multiprocess as mp

    args = [(report, name) for name in report.charts.keys()]
    with mp.Pool() as pool:
        for name, format, result in tqdm.tqdm(
                pool.imap(render_pdf_page, args), total=len(args)
        ):
            slide = slides.new_slide()

            if name.endswith("-wordcloud"):
                slide.box(y=150).text(
                    "Wordcloud of open answers for the previous chart:",
                    style=nelsie.TextStyle(size=20),
                )

            if format == "png":
                slide.image((result, "png"), width="90%")
            elif format == "svg":
                slide.image(result, width="90%")
                os.unlink(result)
            else:
                assert False
            if include_labels:
                slide.box(x=5, y=5).text(name, style=nelsie.TextStyle(size=10))
    print("Rendering PDF")
    slides.render(str(output))


def optimize_png_image(image: bytes) -> bytes:
    img = Image.open(io.BytesIO(image))
    img = img.convert("P", palette=Image.ADAPTIVE, colors=256)
    return pillow_to_png_bytes(img)


def pillow_to_png_bytes(image: Image.Image) -> bytes:
    with io.BytesIO() as buffer:
        image.save(buffer, format="png", optimize=True)
        buffer.seek(0)
        return buffer.getvalue()
