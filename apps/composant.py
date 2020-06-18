import dash_html_components as html
import utils
from dash_table import DataTable


datatable = DataTable(
    columns=[
        {"name": ["", "Year"], "id": "year"},
        {"name": ["City", "Montreal"], "id": "montreal"},
        {"name": ["City", "Vancouver"], "id": "vancouver"},
        {"name": ["Climate", "Temperature"], "id": "temp"},
        {"name": ["Climate", "Humidity"], "id": "humidity"},
    ],
    data=[
        {
            "year": i,
            "montreal": i * 10,
            "vancouver": i * 5,
            "temp": "text",
            "humidity": i * -100,
        }
        for i in range(30)
    ],
    merge_duplicate_headers=True,
    export_format="csv",
    sort_action="native",
    style_cell_conditional=[{"if": {"column_id": "temp"}, "text-align": "left"}],
    cell_selectable=False,
    page_action="native",
    page_size=10
)

layout = html.Div(
    [
        html.H1("Les composants"),
        utils.toolbar([]),
        html.H3("Popin"),
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.Button("×", className="notifier-close"),
                                        html.P(
                                            html.Span(
                                                "Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
                                                "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
                                            )
                                        ),
                                    ],
                                    className="notifier-note",
                                )
                            ],
                            className="plotly-notifier",
                        ),
                    ],
                    className="col col-4",
                )
            ],
            className="columns",
        ),
        html.H3("Code"),
        utils.markdown_content(
            """
    ```
    import foo
    foo.bar()
    ```"""
        ),
        html.H3("Table simple & data table"),
        datatable,
    ]
)
