from typing import Dict, Optional, List

from .chart import make_bar_chart, make_pie_chart, make_wordcloud, make_matrix_chart
from .survey import Question, normalize_open_answers, MatrixQuestion


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
            render_args["scale"] = 2
        return self.render_fn(**kwargs).to_image(format=format, **render_args)


class PngRenderer(ChartRenderer):
    def __init__(self, name: str, render_fn):
        super().__init__(name, render_fn)

    def to_image_bytes(self, format="png", **kwargs) -> Optional[bytes]:
        if format != "png":
            return None
        return self.render_fn(**kwargs)


def join(a, b):
    a = dict(a)
    a.update(b)
    return a


class ChartReport:
    """
    Container that aggregates charts under IDs (string names).
    It can be used to render these charts to a PDF report or a blog post (see `render.py`).
    """
    def __init__(self):
        self.charts: Dict[str, ChartRenderer] = {}

    def add_bar_chart(self, name: str, question: Question, *baselines: Question, **kwargs):
        questions = [question] + list(baselines)

        def render_fn(**args):
            return make_bar_chart(questions=questions, **join(kwargs, args))

        self.add_renderer(name, PlotlyRenderer(name=name, render_fn=render_fn))

    def add_pie_chart(self, name: str, question: Question, **kwargs):
        assert question.is_simple()
        assert question.is_single_answer()

        def render_fn(**args):
            return make_pie_chart(question=question, **join(kwargs, args))

        self.add_renderer(name, PlotlyRenderer(name=name, render_fn=render_fn))

    def add_matrix_chart(self, name: str, question: Question, **kwargs):
        assert isinstance(question.kind, MatrixQuestion)

        def render_fn(**args):
            return make_matrix_chart(question=question, **join(kwargs, args))

        self.add_renderer(name, PlotlyRenderer(name=name, render_fn=render_fn))

    def add_wordcloud(self, name: str, answers: List[str], **kwargs):
        answers = normalize_open_answers(answers)

        def render_fn(**args):
            return make_wordcloud(answers, **join(kwargs, args))

        self.add_renderer(name, PngRenderer(name=name, render_fn=render_fn))

    def get_chart(self, name: str) -> Optional[ChartRenderer]:
        return self.charts.get(name)

    def add_renderer(self, name: str, renderer: ChartRenderer):
        assert name not in self.charts
        self.charts[name] = renderer
