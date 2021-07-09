import dash
from flask import Flask
from heva_theme import _base_template, config as plotconfig, set_style

from config import RoleEnum, Settings

set_style()
__all__ = ("app", "config", "plotconfig", "plotly_theme", "RoleEnum")

config = Settings()

plotconfig["locale"] = config.language
plotly_theme = _base_template.layout.template

external_stylesheets = [
    "https://unpkg.com/spectre.css@0.5.8/dist/spectre.min.css",
    "https://unpkg.com/spectre.css@0.5.8/dist/spectre-icons.min.css",
    # Not needed for now
    # "https://unpkg.com/spectre.css@0.5.8/dist/spectre-exp.min.css",
    "https://fonts.googleapis.com/css?family=Montserrat:700",
]

external_scripts = (
    ["https://cdn.plot.ly/plotly-locale-fr-latest.js"]
    if config.language == "fr"
    else []
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

auth = config.authenticator(app, config.users)
