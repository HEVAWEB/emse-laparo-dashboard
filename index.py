import pathlib

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app, config
from apps import context, gallery, method, results, vars
from utils import __version__

# Dashboard language
config["locale"] = "fr"

# Client - study configuration
CLIENT = "HEVA"
STUDY = "Study"
LOGO_HEVA = "assets/logoHEVA_RVB.svg"
LOGO_CLIENT = "assets/logoHEVA_RVB.svg"

# Change the webpage tab title here if needed
app.title = f"{CLIENT} {STUDY}"

# Global title: Client - Study
title = [html.H2(CLIENT), html.H1(STUDY)]

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
    "/": title + [context.layout],
    "/context": title + [context.layout],
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
    return pages.get(pathname, html.H1(["Page not found"]))


if __name__ == "__main__":

    # Watch md & built files for full reload
    content_path = pathlib.Path(__file__).parent / "assets" / "contents"
    builds_path = pathlib.Path(__file__).parent / "builds"
    extra_files = [*content_path.rglob("*.md"), *builds_path.rglob("*")]
    app.run_server(debug=True, extra_files=extra_files)
