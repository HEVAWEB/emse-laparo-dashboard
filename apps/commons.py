import dash_core_components as dcc
import dash_html_components as html

import utils

OPTIONS_CANCER = [
    {"label": "Digestif bas", "value": "Digestif bas"},
    {"label": "Digestif haut", "value": "Digestif haut"},
    {"label": "Glioblastome", "value": "Glioblastome"},
    {"label": "Gynécologique", "value": "Gynécologique"},
    {"label": "Lymphome", "value": "Lymphome"},
    {"label": "Mélanome", "value": "Mélanome"},
    {"label": "Myélome", "value": "Myélome"},
    {"label": "ORL", "value": "ORL"},
    {"label": "Pancréas", "value": "Pancréas"},
    {"label": "Poumon", "value": "Poumon"},
    {"label": "Prostate", "value": "Prostate"},
    {"label": "Sein", "value": "Sein"},
    {"label": "Testicule", "value": "Testicule"},
    {"label": "Urothélial", "value": "Urothélial"},
]
toolbar = utils.toolbar(
    [
        html.Div(
            [html.Label(["Cancer(s)"], className="form-label")],
            className="col-2 col-sm-12",
        ),
        html.Div(
            [
                dcc.Dropdown(
                    id="tx-cancer-dropdown",
                    options=OPTIONS_CANCER,
                    multi=True,
                    value=["Digestif bas", "Digestif haut", "Glioblastome"],
                    clearable=False,
                    persistence=True,
                    persistence_type="local"
                ),
            ],
            className="col-10 col-sm-12",
        ),
    ]
)
