from io import BytesIO
from typing import Dict, Optional, List

from .chart import make_bar_chart, make_pie_chart, make_wordcloud, make_matrix_chart
from .survey import Question, normalize_open_answers


class ChartRenderer:
    def __init__(self, name: str, render_fn):
        self.name = name
        self.render_fn = render_fn

    def to_image_bytes(self, format: str, **kwargs) -> Optional[bytes]:
        raise NotImplementedError


class PlotlyRenderer(ChartRenderer):
    def __init__(self, name: str, render_fn):
        super().__init__(name, render_fn)

    def to_image_bytes(self, format: str, **kwargs) -> Optional[bytes]:
        render_args = dict()
        if format == "png":
            render_args["scale"] = 4
        return self.render_fn(**kwargs).to_image(format=format, **render_args)


class MatplotlibRenderer(ChartRenderer):
    def __init__(self, name: str, render_fn):
        super().__init__(name, render_fn)

    def to_image_bytes(self, format="png", **kwargs) -> Optional[bytes]:
        if format != "png":
            return None
        buffer = BytesIO()
        self.render_fn(**kwargs).savefig(buffer, format=format)
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()
        return image_png


def join(a, b):
    a = dict(a)
    a.update(b)
    return a


class ChartReport:
    def __init__(self):
        self.charts: Dict[str, ChartRenderer] = {}

    def add_bar_chart(self, name: str, question: Question, baseline: Optional[Question] = None, **kwargs):
        questions = [question]
        if baseline is not None:
            questions.append(baseline)

        def render_fn(**args):
            return make_bar_chart(questions=questions, **join(kwargs, args))

        self.add_renderer(name, PlotlyRenderer(name=name, render_fn=render_fn))

    def add_pie_chart(self, name: str, question: Question, **kwargs):
        def render_fn(**args):
            return make_pie_chart(question=question, **join(kwargs, args))

        self.add_renderer(name, PlotlyRenderer(name=name, render_fn=render_fn))

    def add_matrix_chart(self, name: str, question: Question, **kwargs):
        def render_fn(**args):
            return make_matrix_chart(question=question, **join(kwargs, args))

        self.add_renderer(name, PlotlyRenderer(name=name, render_fn=render_fn))

    def add_wordcloud(self, name: str, answers: List[str], **kwargs):
        answers = normalize_open_answers(answers)

        def render_fn(**args):
            return make_wordcloud(answers, **join(kwargs, args))

        self.add_renderer(name, MatplotlibRenderer(name=name, render_fn=render_fn))

    def get_chart(self, name: str) -> ChartRenderer:
        assert name in self.charts
        return self.charts[name]

    def add_renderer(self, name: str, renderer: ChartRenderer):
        assert name not in self.charts
        self.charts[name] = renderer
