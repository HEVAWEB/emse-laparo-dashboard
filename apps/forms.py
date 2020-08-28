import dash_core_components as dcc
import dash_html_components as html
import utils

range_options = [{"label": f"Value {i}", "value": f"v{i}"} for i in range(20)]
range_options[-1]["disabled"] = True

layout = html.Div(
    [
        html.H1("Les formulaires"),
        html.H3("Toolbar"),
        utils.toolbar(
            [
                html.Div(
                    [
                        dcc.Dropdown(
                            options=range_options,
                            multi=True,
                            value=["v0" "v1", "v2", "v3" "v4", "v5", "v6" "v7", "v8"],
                        )
                    ],
                    className="col-12",
                ),
                html.Div(
                    [
                        html.Label("Text label", className="form-label"),
                        dcc.Input(placeholder="Placeholder", className="form-input"),
                    ],
                    className="form-group",
                ),

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
            options=range_options,
            multi=False,
            value="v0",
        ),
        html.H3("Multi select"),
        dcc.Dropdown(
            options=range_options,
            multi=True,
            value=["v0" "v1", "v2", "v3" "v4", "v5", "v6" "v7", "v8"],
        ),
        html.H3("Radio"),
        dcc.RadioItems(
            options=[
                {"label": "New York City", "value": "NYC"},
                {"label": "Montréal", "value": "MTL"},
                {"label": "San Francisco", "value": "SF"},
            ],
            value="MTL",
            className="group-radio-check",
        ),
        html.H3("Checkbox"),
        dcc.Checklist(
            options=[
                {"label": "New York City", "value": "NYC"},
                {"label": "Montréal", "value": "MTL"},
                {"label": "San Francisco", "value": "SF"},
            ],
            value=["NYC", "MTL"],
            className="group-radio-check",
        ),
        html.Br(),
        html.H3("Slider"),
        dcc.Slider(
            min=-5,
            max=10,
            step=0.5,
            value=-3,
            tooltip=dict(always_visible=True, placement="top"),
        ),
        html.H3("Steps"),
        dcc.Slider(
            min=0,
            max=9,
            marks={i: f"Label {i}" for i in range(10)},
            value=5,
            tooltip=dict(always_visible=False, placement="top"),
        ),
    ]
)
