import dash_core_components as dcc
import dash_html_components as html
import utils

layout = html.Div(
    [
        html.H1("Les formulaires"),
        html.H3("Toolbar"),
        utils.toolbar(
            [
                html.Div(
                    [
                        dcc.Dropdown(
                            options=[
                                {"label": f"Value {i}", "value": f"v{i}"}
                                for i in range(20)
                            ],
                            multi=True,
                            value=["v0" "v1", "v2", "v3" "v4", "v5", "v6" "v7", "v8"],
                        )
                    ],
                    className="col-12",
                )
            ]
        ),
        html.H3("Input"),
        html.Div(
            [
                html.Label("Text label", className="form-label"),
                dcc.Input(placeholder="Placeholder", className="form-input"),
            ],
            className="form-group",
        ),
        html.Div(
            [
                html.Label("Disabled", className="form-label"),
                dcc.Input(
                    placeholder="Placeholder", className="form-input", disabled=True
                ),
            ],
            className="form-group",
        ),
        html.H3("Textarea"),
        html.Div(
            [
                html.Label("Text label", className="form-label"),
                dcc.Textarea(placeholder="Placeholder", className="form-input"),
            ],
            className="form-group",
        ),
        html.H3("Select"),
        dcc.Dropdown(
            options=[{"label": f"Value {i}", "value": f"v{i}"} for i in range(20)],
            multi=False,
            value="v0",
        ),
        html.Br(),
    ]
)
