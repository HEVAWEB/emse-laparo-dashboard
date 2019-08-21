import pathlib

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app, config
from apps import context, gallery, method, results, vars
from utils import __version__

# Import your pages above

# Change the webpage tab title here if needed
app.title = "HEVA Study"
config["locale"] = "fr"


# Global title: Client - Study
title = [html.H2("Client"), html.H1("Study")]

# Change client logo
LOGO_HEVA = "assets/logoHEVA_RVB.svg"
LOGO_CLIENT = "assets/logoHEVA_RVB.svg"

# Sidebar links: add/remove entries if needed
menu = html.Ul(
    children=[
        dcc.Link("Context", href="/context", className="nav-item"),
        dcc.Link("Gallery", href="/gallery", className="nav-item"),
        dcc.Link("Variables", href="/vars", className="nav-item"),
        dcc.Link("Results", href="/results", className="nav-item"),
        dcc.Link("Methodology", href="/methods", className="nav-item"),
    ],
    className="nav",
)
pages = {
    # Default page
    "/": context.layout,
    "/context": context.layout,
    "/methods": method.layout,
    "/vars": vars.layout,
    "/results": results.layout,
    "/gallery": gallery.layout,
}


# You should not feel the need to modify the code bellow

app.layout = html.Div(
    [
        dcc.Location(id="url", refresh=False),
        html.Div(
            [
                html.Div(
                    children=[
                        html.Div(
                            [
                                html.Img(
                                    src=LOGO_HEVA, className="img-responsive logo_heva"
                                )
                            ],
                            className="logo-HEVA-container",
                        ),
                        menu,
                        html.Div(
                            [
                                html.Img(
                                    src=LOGO_CLIENT,
                                    className="img-responsive logo-client",
                                )
                            ],
                            className="logo-client-container",
                        ),
                    ],
                    className="column col-3 sidebar",
                ),
                html.Div(id="page-content", className="column col-9 col-ml-auto"),
            ],
            className="columns col-gapless",
        ),
        html.Footer([f"{__version__}"], className="footer"),
    ]
)


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    """ Update page content with sidebar links"""
    return title + [pages.get(pathname, html.H1(["Page not found"]))]


if __name__ == "__main__":

    # Watch md files for full reload
    content_path = (
        pathlib.Path(__file__).parent.joinpath("assets", "contents").resolve()
    )
    extra_files = list(content_path.rglob("*.md"))
    app.run_server(debug=True, extra_files=extra_files)
