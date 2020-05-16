import pathlib

import dash_core_components as dcc
import dash_html_components as html
import rgpd_dash
from dash.dependencies import Input, Output

from app import app, config
from apps import case_study, context, doe, eula
from utils import __version__, translations

# Client - study configuration
CLIENT = "Mines Saint Etienne"
STUDY = "Automatic and Explainable Labeling of Medical Event Logs with Autoencoding"
LOGO_HEVA = "assets/logoHEVA_RVB.svg"
LOGO_CLIENT = "assets/logoEMSE_RVB.png"

# Change the webpage tab title here if needed
app.title = f"{CLIENT} {STUDY}"

# Global title: Client - Study
title = [html.H2(CLIENT), html.H1(STUDY)]

# Sidebar links: add/remove entries if needed

pages = {
    # Default page
    "/": title + [context.layout],
    "/context": title + [context.layout],
    "/doe": doe.layout,
    "/case_study": case_study.layout,
    "/eula": eula.layout,
}

# Navbar titles: which links & title to display on the navbar, add/remove entries if needed
navbar_titles = {
    "/context": "Context",
    "/doe": "Experiments",
    "/case_study": " Case Study",
}


# You should not feel the need to modify the code bellow

app.layout = html.Div(
    [
        dcc.Location(id="url", refresh=False),
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            children=[
                                html.Div(
                                    [
                                        html.Section(
                                            [
                                                html.Img(
                                                    src=LOGO_HEVA,
                                                    className="img-responsive sidebar-logo hide-xs",
                                                )
                                            ],
                                            className="navbar-section",
                                        ),
                                        html.Section(
                                            id="navbar-menu",
                                            className="navbar-section nav-links",
                                        ),
                                        html.Section(
                                            [
                                                html.Img(
                                                    src=LOGO_CLIENT,
                                                    className="img-responsive sidebar-logo hide-xs",
                                                )
                                            ],
                                            className="navbar-section  logo-client",
                                        ),
                                    ],
                                    className="navbar",
                                ),
                            ],
                            className="column col-2 sidebar col-lg-12",
                        ),
                        html.Div(
                            id="page-content",
                            className="column col-10 col-ml-auto col-lg-12",
                        ),
                    ],
                    className="columns col-gapless",
                ),
            ],
            className="container",
        ),
        html.Div(
            [
                html.Span(f"v{__version__}"),
                dcc.Link(translations["eula"][config["lang"]], href="/eula"),
                html.Span("© 2019"),
            ],
            className="footer",
        ),
        rgpd_dash.RgpdDash(
            trackingCode=config["tracking"]["code"],
            isDebug=config["tracking"]["debug"],
            locale=config["lang"],
        ),
    ]
)


@app.callback(
    [Output("page-content", "children"), Output("navbar-menu", "children")],
    [Input("url", "pathname")],
)
def display_page(pathname):
    """ Update page content with navbar menu and page content corresponding to the tab.

    :param pathname: Path of the page
    :return: Tuple containing content of the page and updated navbar """

    pathname = pathname if pathname != "/" else "/context"
    # Children of the navbar menu, with selected navlink highlighted
    children_menu = [
        html.Li(dcc.Link(title, href=href), className="nav-item")
        if href != pathname
        else html.Li(dcc.Link(title, href=href), className="nav-item nav-item-focus")
        for href, title in navbar_titles.items()
    ]

    # Creating menu
    menu = html.Ul(children_menu, className="nav",)

    return (pages.get(pathname, html.H1(["Page not found"])), menu)


if __name__ == "__main__":

    # Watch md & built files for full reload
    content_path = pathlib.Path(__file__).parent / "assets"
    builds_path = pathlib.Path(__file__).parent / "builds"
    extra_files = [*content_path.rglob("*.md"), *builds_path.rglob("*")]
    app.run_server(debug=True, extra_files=extra_files)
