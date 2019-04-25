import dash

external_stylesheets = [
    "https://unpkg.com/spectre.css/dist/spectre.min.css",
    "https://unpkg.com/spectre.css/dist/spectre-exp.min.css",
    "https://unpkg.com/spectre.css/dist/spectre-icons.min.css",
    "https://fonts.googleapis.com/css?family=Montserrat"
]
app = dash.Dash(
    __name__, external_stylesheets=external_stylesheets
)

app.css.config.serve_locally = True
app.scripts.config.serve_locally = True
app.config.suppress_callback_exceptions = True
