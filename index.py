import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps import context, method, results, vars
from utils import __version__

# Import your pages above

# Global title: Client - Study
title = [html.H2("Client"), html.H1("Study")]

# Sidebar links: add/remove entries if needed
menu = html.Ul(
    children=[
        html.Li(dcc.Link("Context", href="/context"), className="nav-item"),
        html.Li(dcc.Link("Variables", href="/vars"), className="nav-item"),
        html.Li(dcc.Link("Results", href="/results"), className="nav-item"),
        html.Li(dcc.Link("Methodology", href="/methods"), className="nav-item"),
    ],
    className="nav",
)


# Main layout: add client/study logo
app.layout = html.Div(
    [
        html.Link(href="/assets/font/font.css", rel="stylesheet"),
        html.Link(href="/assets/style.css", rel="stylesheet"),
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
    """
    Side bar menu callback.

    Update the page's content.
    You may add/remove entries here.
    """
    if pathname == "/context" or pathname == "/":
        new_layout = context.layout
    elif pathname == "/methods":
        new_layout = method.layout
    elif pathname == "/vars":
        new_layout = vars.layout
    elif pathname == "/results":
        new_layout = results.layout
    else:
        new_layout = html.H1(["Page not found"])

    return title + [new_layout]


if __name__ == "__main__":
    app.run_server(debug=True, port=8051)
