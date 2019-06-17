import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps import context, method, results, vars
from utils import __version__

# Import your pages above

# Change the webpage tab title here if needed
app.title = "HEVA Study"
# Global title: Client - Study
title = [html.H2("Client"), html.H1("Study")]

# Sidebar links: add/remove entries if needed
menu = html.Ul(
    children=[
        dcc.Link("Context", href="/context", className="nav-item"),
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
}

# Main layout: add client/study logo
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
                                    src="assets/logoHEVA_RVB.svg",
                                    className="img-responsive logo_heva",
                                )
                            ],
                            className="logo-HEVA-container",
                        ),
                        menu,
                        # Change logo client here if needed
                        html.Div(
                            [
                                html.Img(
                                    src="assets/logoHEVA_RVB.svg",
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
        html.Footer([f"{__version__}"]),
    ]
)


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    """ Update page content with sidebar links"""
    return title + [pages.get(pathname, html.H1(["Page not found"]))]


if __name__ == "__main__":
    app.run_server(debug=True)
