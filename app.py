import dash
from flask import Flask
from heva_theme import config, set_style

set_style()
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
