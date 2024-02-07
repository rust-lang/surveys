import os
import re
import tempfile
from pathlib import Path

import tqdm
from bs4 import BeautifulSoup

from .report import ChartReport, PlotlyRenderer, MatplotlibRenderer

CHART_MARKER_REGEX = re.compile(r"<!-- chart: ([^ ]*) -->")


def render_blog_post(
        template: Path,
        blog_root: Path,
        output_name: str,
        image_dir: str,
        report: ChartReport
):
    output_path = blog_root / "posts" / output_name

    image_root = blog_root / "static" / "images"
    image_dir = image_root / image_dir
    image_dir.mkdir(parents=True, exist_ok=True)
    print(f"Generating blog post to {output_path}, image directory {image_dir}")

    with open(template) as f:
        document = f.read()

    def make_rel_path(path: Path) -> str:
        path = path.relative_to(image_root)
        return f"../../../images/{path}"

    height = 600

    scripts = ['<script charset="utf-8" src="https://cdn.plot.ly/plotly-2.27.0.min.js"></script>']
    for chart_id in tqdm.tqdm(CHART_MARKER_REGEX.findall(document)):
        if chart_id not in report.charts:
            raise Exception(f"Chart with ID `{chart_id}` was not found")
        chart = report.get_chart(chart_id)

        marker = f"<!-- chart: {chart_id} -->"

        # Render the chart as PNG and SVG
        png_bytes = chart.to_image_bytes(format="png")
        png_path = image_dir / f"{chart_id}.png"
        with open(png_path, "wb") as f:
            f.write(png_bytes)

        svg_bytes = chart.to_image_bytes(format="svg")
        svg_path = image_dir / f"{chart_id}.svg"
        with open(svg_path, "wb") as f:
            f.write(svg_bytes)

        if isinstance(chart, PlotlyRenderer):
            element = BeautifulSoup(chart.render_fn().to_html(full_html=False, include_plotlyjs=None, div_id=chart_id),
                                    features="lxml").div
            div = element.find("div")

            tag = f"""<div>
{div}
<noscript>
    <img src="{make_rel_path(png_path)}" height="{height}" alt="{chart_id}" />
</noscript>
<div style="display: flex">
    <span>[<a href="{make_rel_path(png_path)}">PNG</a>]</span>&nbsp;
    <span>[<a href="{make_rel_path(svg_path)}">SVG</a>]</span>
</div>
</div>"""
            # TODO: handle mobile
            # TODO: better alt text
            # TODO: relative path to the image
            document = document.replace(marker, tag)

            script = element.find("script")
            assert script is not None
            scripts.append(str(script))
        elif isinstance(chart, MatplotlibRenderer):
            assert False
            document = document.replace(marker, f'<img src="{make_rel_path(png_path)}" alt="{chart_id}" />')
        else:
            assert False

    script_marker = "<!-- scripts -->"
    if script_marker not in document:
        raise Exception(f"Please add `{script_marker}` to the (end of the) Markdown document")
    script_str = "<!-- Chart scripts -->\n\n" + "\n\n".join(scripts)
    document = document.replace(script_marker, script_str)

    with open(output_path, "w") as f:
        f.write(document)


def render_report_to_pdf(report: ChartReport, output: Path, title: str, include_labels=False):
    import elsie
    from elsie.render.backends.cairo.backend import CairoBackend

    # A4 format
    slides = elsie.SlideDeck(backend=CairoBackend(), width=595, height=842)
    slide = slides.new_slide()
    slide.box().text(title)

    print("Rendering charts")

    charts = list(report.charts.items())#[:3]
    for (name, chart) in tqdm.tqdm(charts):
        slide = slides.new_slide()

        box = slide.box(width="95%")

        svg_bytes = chart.to_image_bytes(format="svg")
        if svg_bytes is not None:
            with tempfile.NamedTemporaryFile(suffix=".svg", delete=False) as f:
                f.write(svg_bytes)
                path = f.name
            box.image(path)
            os.unlink(path)
        else:
            png_bytes = chart.to_image_bytes(format="png")
            box.image(png_bytes, image_type="png")
        if include_labels:
            slide.box(x=5, y=5).text(name, style=elsie.TextStyle(size=10))
    print("Rendering PDF")
    slides.render(str(output))
