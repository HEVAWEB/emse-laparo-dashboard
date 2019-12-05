import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pandas as pd

import utils

df_iris = pd.read_csv("builds/iris.csv")
table = dash_table.DataTable(
    columns=[{"name": i, "id": i} for i in df_iris.columns],
    data=df_iris.to_dict(orient="records"),
    export_format="csv",
    sort_action="native",
    style_table={"overflowX": "scroll"},
    style_cell={"minWidth": "120px"},
)

layout = html.Div(
    [
        html.H3("Zone 51 👽"),
        html.H4("Titres et emphases"),
        html.Hr(),
        html.H1("Titre H1"),
        html.H2("Titre H2"),
        html.H3("Titre H3"),
        html.H4("Titre H4"),
        html.H5("Titre H5"),
        html.H6("Titre H6"),
        utils.markdown_content("*Emphase simple* et **emphase double**"),
        html.A("Ceci est un lien qui ne mène à rien"),
        html.Hr(),
        html.H4("Listes"),
        html.Ul(
            [html.Li("New York City"), html.Li("Montréal"), html.Li("San Francisco")]
        ),
        html.Ol(
            [html.Li("New York City"), html.Li("Montréal"), html.Li("San Francisco")]
        ),
        html.Hr(),
        html.H4("Code"),
        utils.markdown_content(
            """
        ```python
        import foo

        foo.bar()
        ```
        """
        ),
        html.Hr(),
        html.H4("Quote"),
        utils.markdown_content(
            "> Il ne faut pas croire tout ce qu'on lit sur Internet. Albert Einstein, 1928"
        ),
        html.Hr(),
        html.H4("Intro"),
        html.Div(
            "Il y a bien longtemps, dans une galaxie lointaine, très lointaine...",
            className="intro",
        ),
        html.Hr(),
        html.H4("Conclusion"),
        utils.takeaways(
            "David Bowie est bien mieux que Michael Jackson, sans aucun doute."
        ),
        html.Hr(),
        html.H4("Tabs"),
        dcc.Tabs(
            id="tabs",
            value="tab-1",
            children=[
                dcc.Tab(
                    label="Tab1",
                    value="tab-1",
                    className="custom-tab",
                    selected_className="custom-tab--selected",
                ),
                dcc.Tab(
                    label="Tab2",
                    value="tab-2",
                    className="custom-tab",
                    selected_className="custom-tab--selected",
                ),
                dcc.Tab(
                    label="Tab3",
                    value="tab-3",
                    className="custom-tab",
                    selected_className="custom-tab--selected",
                ),
            ],
            parent_className="custom-tabs",
            className="custom-tabs-container",
        ),
        html.H4("Table simple"),
        utils.table_from_df(df_iris),
        html.H4("Data table"),
        table,
        html.H4("Toolbar"),
        html.Div(
            [
                html.Form(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.Label(
                                            ["Indicateur"], className="form-label"
                                        )
                                    ],
                                    className="col-3 col-sm-12",
                                ),
                                html.Div(
                                    [
                                        dcc.Dropdown(
                                            options=[
                                                {"label": "Label1", "value": 0},
                                                {"label": "Label2", "value": 1},
                                                {"label": "Label3", "value": 2},
                                            ],
                                            value=0,
                                            searchable=False,
                                            clearable=False,
                                            multi=True,
                                            id="ind-dropdown",
                                        )
                                    ],
                                    className="col-9 col-sm-12",
                                ),
                                html.Div(
                                    [
                                        html.Label(
                                            ["Granularité"], className="form-label"
                                        )
                                    ],
                                    className="col-3 col-sm-12",
                                ),
                                html.Div(
                                    [
                                        dcc.RadioItems(
                                            options=[
                                                {"label": "Régionale", "value": "reg"},
                                                {
                                                    "label": "Départementale",
                                                    "value": "dep",
                                                },
                                            ],
                                            value="reg",
                                            id="gran-dropdown",
                                        )
                                    ],
                                    className="col-9 col-sm-12",
                                ),
                                html.Div(
                                    [html.Label(["Année"], className="form-label")],
                                    className="col-3 col-sm-12",
                                ),
                                html.Div(
                                    [
                                        dcc.Slider(
                                            min=2017,
                                            max=2019,
                                            marks={
                                                2017: "2017",
                                                2018: "2018",
                                                2019: "2019",
                                            },
                                            value=2019,
                                            id="year-slider",
                                        )
                                    ],
                                    className="col-4 col-sm-12",
                                ),
                            ],
                            className="form-group",
                        )
                    ],
                    className="form-horizontal",
                )
            ],
            className="tools",
        ),
        html.H4(["Dropdown"]),
        dcc.Dropdown(
            options=[
                {"label": "New York City", "value": "NYC"},
                {"label": "Montréal", "value": "MTL"},
                {"label": "San Francisco", "value": "SF"},
            ],
            value="MTL",
        ),
        html.Hr(),
        html.H4(["Slider"]),
        dcc.Slider(
            min=0, max=9, marks={i: "Label {}".format(i) for i in range(10)}, value=5
        ),
        html.Br(),
        dcc.Slider(
            min=0,
            max=9,
            marks={i: "Disabled" for i in range(10)},
            value=5,
            disabled=True,
        ),
        html.Hr(),
        html.H4(["Range Slider"]),
        dcc.RangeSlider(count=1, min=-5, max=10, step=0.5, value=[-3, 7]),
        html.Hr(),
        html.H4(["Simple Input"]),
        dcc.Input(placeholder="Enter a value...", type="text", value=""),
        dcc.Input(placeholder="Disabled", type="text", disabled=True),
        html.Hr(),
        html.H4(["Dropdown"]),
        dcc.Dropdown(
            options=[
                {"label": "Label1", "value": 0},
                {"label": "Label2", "value": 1},
                {"label": "Label3", "value": 2},
            ],
            value=0,
            searchable=False,
            clearable=False,
            multi=True,
        ),
        html.Hr(),
        html.H4(["Textarea"]),
        dcc.Textarea(
            placeholder="Enter a value...",
            value="This is a TextArea component",
            style={"width": "100%"},
        ),
        dcc.Textarea(
            placeholder="Enter a value...",
            value="Disabled",
            style={"width": "100%"},
            disabled=True,
        ),
        html.Hr(),
        html.H4(["Checklist"]),
        dcc.Checklist(
            options=[
                {"label": "New York City", "value": "NYC"},
                {"label": "Montréal", "value": "MTL"},
                {"label": "Disabled", "value": "SF", "disabled": True},
            ],
            value=["MTL", "SF"],
        ),
        html.Hr(),
        html.H4(["Radio items"]),
        dcc.RadioItems(
            options=[
                {"label": "New York City", "value": "NYC"},
                {"label": "Montréal", "value": "MTL"},
                {"label": "Disabled", "value": "SF", "disabled": True},
            ],
            value="MTL",
        ),
        html.Hr(),
        html.H4(["Button"]),
        html.Button("Default"),
        html.Button("Disabled", disabled=True),
    ]
)
