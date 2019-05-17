"""Utils functions"""
from typing import Any

import dash_core_components as dcc
import dash_html_components as html

from app import config

__all__ = ("graph", "markdown_content")


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
