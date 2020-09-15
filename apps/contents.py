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
    page_action="native",
    page_size=10,
    fixed_columns=dict(headers=True, data=1),
    style_table=dict(minWidth="100%"),
    style_cell=dict(minWidth="100px"),
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
        html.Br(),
        html.H3("Figures"),
        html.Div(
            [
                html.Div(
                    [
                        html.Figure(
                            [
                                html.Img(
                                    src="https://source.unsplash.com/user/pawel_czerwinski",
                                    className="img-responsive",
                                ),
                                html.Figcaption(
                                    "Random image from Unsplash.com",
                                    className="figure-caption text-center",
                                ),
                            ]
                        )
                    ],
                    className="column col-6",
                ),
                html.Div(
                    [
                        html.Figure(
                            [
                                html.Img(
                                    src="https://source.unsplash.com/user/pawel_czerwinski",
                                    className="img-responsive",
                                ),
                                html.Figcaption(
                                    "Random image from Unsplash.com", id="bli"
                                ),
                            ]
                        )
                    ],
                    className="column col-6",
                ),
            ],
            className="columns col-gapless",
        ),
        html.Br(),
        html.H3("Cards"),

        html.Div(
            [html.P("ceci est une carte en cours de création")], className="card-artemis"
        ),
        html.Br(),
        html.H3("Table simple & data table"),
        datatable,
    ]
)
