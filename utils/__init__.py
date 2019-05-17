"""Utils functions"""

import dash_core_components as dcc
import dash_html_components as html

from app import config

__all__ = ("graph", "markdown_content")


def graph(fig):
    return html.Div([dcc.Graph(figure=fig, config=config)], className="graph")


def markdown_content(content, class_name="text"):
    return dcc.Markdown([content], dangerously_allow_html=True, className=class_name)
