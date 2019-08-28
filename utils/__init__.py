"""Utils functions"""
from typing import Any

import dash_core_components as dcc
import dash_html_components as html

from app import config

__version__ = "1.3.0"
__all__ = (
    "graph",
    "two_graphs",
    "takeaways",
    "simple_table",
    "markdown_content",
    "__version__",
)


def graph(fig: Any, loading=True, **kwargs: Any) -> html.Div:
    """
    Utility function for Plotly graphs.

    :param fig: Plotly/Plotly-express figure (loaded with json/pickle accepted)
    :param loading: Enclose fig in loading component. Should be False for interactive TAK.
    :param kwargs: Keyword arguments passed to dcc.Graph constructor
    :return: Html placeholder for graph
    """
    if loading:
        content = dcc.Loading(
            [dcc.Graph(figure=fig, config=config, **kwargs)],
            color="#fc5b26",
            type="dot",
        )
    else:
        content = dcc.Graph(figure=fig, config=config, **kwargs)

    return html.Div([content], className="graph")


def two_graphs(graph1: html.Div, graph2: html.Div) -> html.Div:
    """
    Utility function for laying side by side two graphs
    :param graph1: result of utils.graph
    :param graph2: result of utils.graph
    :return:
    """
    return html.Div(
        [
            html.Div(
                [dcc.Loading([graph1], color="#fc5b26", type="dot")],
                className="column col-6 col-xl-12",
            ),
            html.Div(
                [dcc.Loading([graph2], color="#fc5b26", type="dot")],
                className="column col-6 col-xl-12",
            ),
        ],
        className="columns col-gapless",
    )


def markdown_content(content: str, class_name: str = "text") -> dcc.Markdown:
    """
    Utility function for textual content.

    This is a simple wrapper for dcc.Markdown with default value for the best aesthetics.

    :param content: Textual markdown content
    :param class_name: css class
    :return: Markdown rendered element
    """
    return dcc.Markdown([content], dangerously_allow_html=True, className=class_name)


def takeaways(content: str, title="Takeaways") -> html.Div:
    """
    Utility function for small emphasized conclusions

    :param content: Textual markdown content
    :return: html placeholder for takeaways
    """
    return html.Div([html.H4([title]), markdown_content(content, "conclusion")])


def simple_table(content: str) -> dcc.Markdown:
    """
    Utility function for simple results table

    :param content: Textual markdown content
    :return: html placeholder for table
    """
    return dcc.Markdown([content], dangerously_allow_html=True, className="table graph")
