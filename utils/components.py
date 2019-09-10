import csv
from pathlib import Path
from typing import Any, Union

import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from heva_theme import config


def graph(fig: Any, loading=True, **kwargs: Any) -> html.Div:
    """Utility function for Plotly graphs.

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
    """Utility function for laying side by side two graphs.

    :param graph1: result of utils.graph
    :param graph2: result of utils.graph
    :return: html layout for side by side graphs
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
    """Utility function for textual content.

    This is a simple wrapper for dcc.Markdown with default value for the best aesthetics.

    :param content: Textual markdown content
    :param class_name: css class
    :return: Markdown rendered element
    """

    return dcc.Markdown([content], dangerously_allow_html=True, className=class_name)


def takeaways(content: str, title="À retenir") -> html.Div:
    """Utility function for small emphasized conclusions.

    :param content: Textual markdown content
    :param title: Section title
    :return: html placeholder for takeaways
    """

    return html.Div([html.H4([title]), markdown_content(content, "conclusion")])


def table_from_md(content: str) -> dcc.Markdown:
    """Utility function for simple results table.

    :param content: Textual markdown content
    :return: Markdown rendered table
    """

    return dcc.Markdown([content], dangerously_allow_html=True, className="table graph")


def table_from_csv(path: Union[str, Path]) -> dcc.Markdown:
    """Generate markdown table from csv content.

    :param path: File path
    :return: Markdown rendered table
    """

    lines = []
    with open(path, "r", encoding="utf-8", newline="") as f:
        dialect = csv.Sniffer().sniff(f.read(1024))
        f.seek(0)
        reader = csv.reader(f, dialect)
        header = next(reader)
        nb_cols = len(header)
        lines.append(f"| {' | '.join(header)} |")
        lines.append(f"|-- {'|--:' * (nb_cols-1)} |")
        for row in reader:
            lines.append(f"| {' | '.join(row)} |")

    content = "\n".join(lines)
    return dcc.Markdown([content], dangerously_allow_html=True, className="table graph")


def table_from_df(df: pd.DataFrame) -> dcc.Markdown:
    """Generate markdown table from dataframe.

    :param df: DataFrame
    :return: Markdown rendered table
    """

    lines = [f"| {' | '.join(df.columns)} |", f"|-- {'|--:' * (len(df.columns) - 1)} |"]
    for row in df.itertuples(index=False):
        row_as_str = (f"{cell}" for cell in row)
        lines.append(f"| {' | '.join(row_as_str)} |")

    content = "\n".join(lines)
    return dcc.Markdown([content], dangerously_allow_html=True, className="table graph")