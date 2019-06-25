"""Utils functions"""
from typing import Any

import dash_core_components as dcc
import dash_html_components as html

from app import config

__version__ = "1.2.0a"
__all__ = ("graph", "markdown_content", "__version__")


def graph(fig: Any, **kwargs: Any) -> html.Div:
    """
    Utility function for Plotly graphs.

    :param fig: Plotly/Plotly-express figure (loaded with json/pickle accepted)
    :param kwargs: Keyword arguments passed to dcc.Graph constructor
    :return: Html placeholder for graph
    """
    return html.Div([dcc.Graph(figure=fig, config=config, **kwargs)], className="graph")


def markdown_content(content: str, class_name: str = "text") -> dcc.Markdown:
    """
    Utility function for textual content.

    This is a simple wrapper for dcc.Markdown with default value for the best aesthetics.

    :param content: Textual markdown content
    :param class_name: css class
    :return: Markdown rendered element
    """
    return dcc.Markdown([content], dangerously_allow_html=True, className=class_name)


def takeaways(content: str) -> html.Div:
    """
    Utility function for small emphasized conclusions

    :param content: Textual markdown content
    :return: html placeholder for takeaways
    """
    return html.Div([html.H4(["Takeaways"]), markdown_content(content, "conclusion")])


def simple_table(content: str) -> html.Div:
    """
    Utility function for simple results table

    :param content: Textual markdown content
    :return: html placeholder for table
    """
    return dcc.Markdown([content], dangerously_allow_html=True, className="table graph")
