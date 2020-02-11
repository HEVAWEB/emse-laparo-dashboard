import dash
import toml
from flask import Flask
from heva_theme import _base_template, config as plotconfig, set_style

set_style()
__all__ = ("app", "config", "plotconfig", "plotly_theme")

config = toml.load("config.toml")
config["lang"] = config.get("lang", "fr")

plotconfig["locale"] = config["lang"]
plotly_theme = _base_template.layout.template

external_stylesheets = [
    "https://unpkg.com/spectre.css@0.5.8/dist/spectre.min.css",
    # Not needed for now
    # "https://unpkg.com/spectre.css@0.5.8/dist/spectre-exp.min.css",
    "https://fonts.googleapis.com/css?family=Montserrat:700",
]


external_scripts = (
    ["https://cdn.plot.ly/plotly-locale-fr-latest.js"] if config["lang"] == "fr" else []
)

server = Flask(__name__)
app = dash.Dash(
    server=server,
    name=__name__,
    external_stylesheets=external_stylesheets,
    external_scripts=external_scripts,
    serve_locally=False,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)

app.config.suppress_callback_exceptions = True
