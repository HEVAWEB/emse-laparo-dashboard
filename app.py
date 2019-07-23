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

# Common plot theming should go there
#_sequence_colors = [
#    "#0d0887",
#    "#46039f",
#    "#7201a8",
#    "#9c179e",
#    "#bd3786",
#    "#d8576b",
#    "#ed7953",
#    "#fb9f3a",
#    "#fdca26",
#    "#f0f921",
#]

_sequence_colors = [
    "#4a2572",
    "#8b256a",
    "#cd2561",
    "#e83f55",
    "#f76147",
    "#ff8e32",
    "#ffc515",
    "#fff11c",
    "#fff88e",
    "#ffffff",
]
"""
_divergent_colors = [
    "#4a2572",
    "#6e4d8d",
    "#9277a9",
    "#b6a3c5",
    "#dad0e2",
    "#ffffff",
    "#ffd81f",
    "#ffc12c",
    "#ffa935",
    "#ff8f3b",
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
