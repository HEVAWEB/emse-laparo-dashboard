import dash

import plotly.graph_objs as go
import plotly.io as pio

__all__ = ("app",)

external_stylesheets = [
    "https://unpkg.com/spectre.css/dist/spectre.min.css",
    "https://unpkg.com/spectre.css/dist/spectre-exp.min.css",
    "https://unpkg.com/spectre.css/dist/spectre-icons.min.css",
    "https://fonts.googleapis.com/css?family=Montserrat",
]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.css.config.serve_locally = True
app.scripts.config.serve_locally = True
app.config.suppress_callback_exceptions = True

# Common plot theming should go there
_base_template = pio.to_templated(
    go.Figure(
        layout=go.Layout(
            font={"family": "Montserrat"},
            images=[
                dict(
                    name="watermark_heva",
                    source="assets/logoHEVA_RVB.svg",
                    xref="paper",
                    yref="paper",
                    x=1,
                    y=1.05,
                    sizex=0.1,
                    sizey=0.1,
                    xanchor="right",
                    yanchor="bottom",
                )
            ],
        )
    )
)

pio.templates["heva_theme"] = _base_template.layout.template
pio.templates.default = "heva_theme"
