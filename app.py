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
app = dash.Dash(
    server=server,
    name=__name__,
    external_stylesheets=external_stylesheets,
    serve_locally=False,
)

app.config.suppress_callback_exceptions = True

_sequence_colors = [
    "#4a2572",
    "#cd2561",
    "#e83f55",
    "#f76147",
    "#ff8e32",
    "#ffc515",
    "#fff11c",
    "#fff88e",
    "#ffffff",
]

_divergent_colors = [
    "#4a2572",
    "#674588",
    "#84669e",
    "#a088b4",
    "#bdaccb",
    "#dad0e2",
    "#ffe9ae",
    "#ffd075",
    "#ffb452",
    "#ff9541",
    "#ff7240",
]
"""
_divergent_colors = [
    "#9e0142",
    "#d53e4f",
    "#f46d43",
    "#fdae61",
    "#fee08b",
    "#ffffbf",
    "#e6f598",
    "#abdda4",
    "#66c2a5",
    "#3288bd",
    "#5e4fa2",
]
"""

sequence_colorscale = [
    (i / (len(_sequence_colors) - 1), c) for i, c in enumerate(_sequence_colors)
]

divergent_colorscale = [
    (i / (len(_divergent_colors) - 1), c) for i, c in enumerate(_divergent_colors)
]

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
                "#188C9C",
                "#FF7240",
                "#DD255F",
                "#326AB1",
                "#ACCB44",
                "#FABB00",
                "#FF3C48",
                "#4CA094",
                "#FFEF00",
            ],
            colorscale=dict(
                sequential=sequence_colorscale, diverging=divergent_colorscale
            ),
            images=[dict(name="base_template")],
            template=dict(data=dict(heatmap=[dict(autocolorscale=True)])),
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
