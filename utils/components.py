import csv
import re
from collections import Counter
from itertools import islice
from pathlib import Path
from typing import Any, Optional, Union

import dash_core_components as dcc
import dash_html_components as html
import heva_theme
import pandas as pd


class MarkdownReader:
    """Convenient reader with splits.

    This class makes it easy to access various parts of the content.
    You may delimit sections in your file with

    .. code-block:: md

        [//]: # (section)

    """

    def __init__(self, content: str) -> None:
        self.sections = list(re.compile("\n\[//\]: # \(section\)\n").split(content))

    def __getitem__(self, section):
        if isinstance(section, slice):
            content = "".join(self.sections[section])
        else:
            content = self.sections[section]
        return markdown_content(content)

    def __iter__(self):
        return iter(self.sections)

    def full(self):
        """Get the full rendered markdown content"""
        return markdown_content("".join(self.sections))


def graph(fig: Any, loading=True, config=None, **kwargs: Any) -> html.Div:
    """Utility function for Plotly graphs.

    :param fig: Plotly/Plotly-express figure (loaded with json/pickle accepted)
    :param loading: Enclose fig in loading component. Should be False for interactive TAK.
    :param config: Plotly figure configuration (export size, modebar buttons, etc.)
    :param kwargs: Keyword arguments passed to dcc.Graph constructor
    :return: Html placeholder for graph
    """

    graph_config = config if config else heva_theme.config

    if loading:
        content = dcc.Loading(
            [dcc.Graph(figure=fig, config=graph_config, **kwargs)],
            color="#fc5b26",
            type="dot",
        )
    else:
        content = dcc.Graph(figure=fig, config=graph_config, **kwargs)

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
        className="columns two-graphs",
    )


def markdown_content(content: str, class_name: str = "text") -> dcc.Markdown:
    """Utility function for textual content.

    This is a simple wrapper for dcc.Markdown with default value for the best aesthetics.

    :param content: Textual markdown content
    :param class_name: css class
    :return: Markdown rendered element
    """

    return dcc.Markdown(
        [content],
        dangerously_allow_html=True,
        className=class_name,
        highlight_config={"theme": "dark"},
    )


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

    return dcc.Markdown(
        [content.rstrip()],
        dangerously_allow_html=True,
        className="table table-hover graph",
    )


def table_from_csv(path: Union[str, Path], title: Optional[str] = None) -> html.Div:
    """Generate HTML table from csv content.

    :param path: File path
    :param title: Optional table title
    :return: HTML rendered table
    """

    table = html.Table([], className="table table-hover")

    with open(path, "r", encoding="utf-8", newline="") as f:
        dialect = csv.Sniffer().sniff(f.read().rstrip())
        f.seek(0)
        reader = csv.reader(f, dialect)
        header = next(reader)

        # Add header
        table.children = [html.Thead(html.Tr([html.Th([cell]) for cell in header]))]

        # Add all rows
        body = html.Tbody([])
        for row in reader:
            body.children.append(html.Tr([html.Td([cell]) for cell in row]))

    table.children.append(body)

    content = [table]
    if title:
        content.insert(0, html.H4(title))

    return html.Div(content, className="graph")


def table_from_df(
    df: pd.DataFrame, title: Optional[str] = None, orient_vertically: bool = True
) -> html.Div:
    """Generate HTML table from dataframe.

    This function is able to regroup common index columns/rows.

    :param df: DataFrame
    :param title: Optional table title
    :param orient_vertically: Table orientation, header is first row, else first column. Default True
    :return: HTML rendered table
    """
    regroup = False
    if "flag" in df.columns:
        df = df.drop(columns=["flag"])
        regroup = True

    if orient_vertically:
        if regroup:
            table = _make_v_regrouped_table(df)
        else:
            table = _make_v_table(df)
    else:
        if regroup:
            table = _make_h_regrouped_table(df)
        else:
            table = _make_h_table(df)

    content = []
    if title:
        content.append(html.H4(title))
    content.append(table)
    return html.Div(content, className="graph")


def _make_v_table(df: pd.DataFrame) -> html.Table:
    """Generate a long HTML table.

    This is the simplest case:

    - DataFrame column names become table header
    - No regrouping

    :param df: DataFrame
    :return: HTML table
    """
    table = html.Table([], className="table table-hover")

    # Add header
    table.children = [html.Thead(html.Tr([html.Th([col]) for col in df.columns]))]
    body = html.Tbody([])
    # Add all rows
    for row in df.itertuples(index=False):
        body.children.append(html.Tr([html.Td([cell]) for cell in row]))
    table.children.append(body)
    return table


def _make_v_regrouped_table(df: pd.DataFrame) -> html.Table:
    """Generate a long HTML table with the 1st column regrouped

    This generation is a bit complex:

    - 1st row is the header
    - for each grouping the 1st cell is larger
    - then we add the n-1 cells remaining for the following rows

    :param df: DataFrame
    :return: HTML table
    """
    table = html.Table([], className="table table-hover")

    # Add header
    table.children = [html.Thead(html.Tr([html.Th([col]) for col in df.columns]))]

    body = html.Tbody([])

    # For each group, we trace the first row with the proper height
    # then we add the following row minus the first cell
    for name, group in df.groupby(df.columns[0], sort=False):
        rowspan = len(group)
        row_iterator = group.itertuples(index=False)

        # First row need to define the `rowspan` of the 1st cell
        first_row = next(row_iterator)
        group_table_rows = [
            html.Tr(
                [
                    html.Td([first_row[0]], rowSpan=rowspan),
                    *[html.Td(cell) for cell in first_row[1:]],
                ]
            )
        ]

        # Then we add the following rows
        for row in row_iterator:
            group_table_rows.append(html.Tr([html.Td([cell]) for cell in row[1:]]))
        body.children.extend(group_table_rows)

    table.children.append(body)
    return table


def _make_h_table(df: pd.DataFrame) -> html.Table:
    """Generate a wide HTML table

    Note: 1st column is the header

    :param df: DataFrame
    :return: HTML table
    """
    table = html.Table([], className="table table-hover")

    # Transpose dataframe & iterate on row; first attribute is the header
    df = df.T

    # Add all rows with first cell as header
    for row in df.itertuples():
        table.children.append(
            html.Tr([html.Th([row[0]]), *[html.Td(cell) for cell in row[1:]]])
        )
    return table


def _make_h_regrouped_table(df: pd.DataFrame) -> html.Table:
    """Generate a wide HTML table with 1st row regrouped

    Here is the most complex table generation:

    - 1st column is the header
    - 2nd column should not have the vertical separator
    - all others column should be regrouped with a separator

    :param df: DataFrame
    :return: HTML table
    """
    table = html.Table([], className="table table-hover")
    df = df.T

    # We will need a counter to place the separators
    row_iterator = df.itertuples()
    first_row = next(row_iterator)
    first_row_counter = Counter(first_row[1:])

    # Add header with columns grouped
    first_row_cells = [
        html.Td(k, colSpan=v, className="bordered-cell")
        for k, v in first_row_counter.items()
    ]
    first_row_cells[0].className = None
    table.children = [html.Tr([html.Th([first_row[0]]), *first_row_cells])]

    # Add each line with the proper grouping
    for row in row_iterator:

        th = html.Th([row[0]])

        # Group cells by agregations
        tds = []
        slices = first_row_counter.values()
        iter_cells = iter(row[1:])
        groups_cells = (islice(iter_cells, sl) for sl in slices)

        # Do not put a separator for the 1st column
        first_group = next(groups_cells)
        cells = [html.Td(cell) for cell in first_group]
        tds.extend(cells)

        for group in groups_cells:
            cells = [html.Td(cell) for cell in group]
            cells[0].className = "bordered-cell"
            tds.extend(cells)

        table.children.append(html.Tr([th, *tds]))

    return table
