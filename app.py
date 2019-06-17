import dash
import plotly.graph_objs as go
import plotly.io as pio
from flask import Flask

__all__ = ("app", "config")

external_stylesheets = [
    "https://unpkg.com/spectre.css@0.5.8/dist/spectre.min.css",
    # Not needed for now
    # "https://unpkg.com/spectre.css@0.5.8/dist/spectre-exp.min.css",
    "https://fonts.googleapis.com/css?family=Montserrat:700",
]

server = Flask(__name__)
app = dash.Dash(server=server, name=__name__, external_stylesheets=external_stylesheets)

# Set the two following parameters to True if you encounter
# issues with CDNs
app.css.config.serve_locally = False
app.scripts.config.serve_locally = False

app.config.suppress_callback_exceptions = True

# Common plot theming should go there
_base_template = pio.to_templated(
    go.Figure(
        layout=go.Layout(
            title=dict(
                x=0,
                font=dict(family="Montserrat, sans-serif", color="#5E5A85", size=20),
            ),
            xaxis=dict(
                tickfont=dict(family="SF, sans-serif", color="#9491AD", size=12),
                gridcolor="rgba(244,244,247)",
                gridwidth=1,
                color="#2B1D46",
                title=dict(
                    font=dict(family="SF, sans-serif", color="#2B1D46", size=14)
                ),
            ),
            yaxis=dict(
                tickfont=dict(family="SF, sans-serif", color="#9491AD", size=12),
                gridcolor="rgba(244,244,247)",
                color="#2B1D46",
                title=dict(
                    font=dict(family="SF, sans-serif", color="#2B1D46", size=14)
                ),
            ),
            hoverlabel=dict(font=dict(family="SF, sans-serif", size=12)),
            bargap=0.2,
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            colorway=[
                "#4A2572",
                "#DD255F",
                "#FF3C48",
                "#FF7240",
                "#FABB00",
                "#FFEF00",
                "#ACCB44",
                "#4CA094",
                "#188C9C",
                "#326AB1",
            ],
            images=[dict(name="base_template")],
        )
    )
)

# Graph configuration goes here
config = {
    "toImageButtonOptions": {
        "format": "svg",
        "filename": "plot",
        "height": 720,
        "width": 1280,
    },
    "displaylogo": False,
    "modeBarButtonsToRemove": ["select2d", "lasso2d"],
    "doubleClick": "reset",
}

pio.templates["heva_theme"] = _base_template.layout.template
pio.templates.default = "heva_theme"
