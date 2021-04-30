import pathlib
from typing import List

import dash_core_components as dcc
import dash_html_components as html
import rgpd_dash
from dash.dependencies import Input, Output

from app import RoleEnum, app, auth, config
from apps import context, design, eula, gallery, method, results
from utils import __version__, translations

server = app.server

# Client - study configuration
CLIENT = "HEVA"
STUDY = "Study"
LOGO_HEVA = "assets/logoHEVA_RVB.svg"
LOGO_CLIENT = "assets/logoHEVA_RVB.svg"

# Change the webpage tab title here if needed
app.title = f"{CLIENT} {STUDY}"

# Global title: Client - Study
title = [html.H2(CLIENT), html.H1(STUDY)]

# Pages links: add/remove entries if needed
pages = {
    # Default page
    "/": title + [context.layout],
    "/context": title + [context.layout],
    "/design": design.layout,
    "/methods": method.layout,
    "/results": results.layout,
    "/gallery": gallery.layout,
    "/eula": eula.layout,
}

# Navbar titles: which links & title to display on the navbar, add/remove entries if needed
navbar_titles = {
    "/context": "Contexte",
    "/design": "Zone 51",
    "/methods": " Méthodologie",
    "/gallery": "Galerie",
    "/results": "Résultats",
}

# Page access restriction is done there.
# By default all pages have a "guest" access.
pages_access = {"/context": [RoleEnum.guest]}

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
                                        html.Div(
                                            [
                                                html.Img(
                                                    src=LOGO_HEVA,
                                                    className="img-responsive sidebar-logo hide-xs",
                                                )
                                            ],
                                        ),
                                        html.Div(id="navbar-menu"),
                                        html.Div(
                                            [
                                                html.Img(
                                                    src=LOGO_CLIENT,
                                                    className="img-responsive sidebar-logo hide-xs",
                                                )
                                            ],
                                            className="logo-client",
                                        ),
                                    ],
                                    id="main-sidebar",
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
                dcc.Link(translations["eula"][config.language], href="/eula"),
                html.Span("© 2019"),
            ],
            className="footer",
        ),
        rgpd_dash.RgpdDash(
            trackingCode=config.tracking_code,
            isDebug=config.debug,
            locale=config.language,
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
    user_role = auth.get_role()

    children_menu = make_menu(pathname, user_role)
    menu = html.Ul(children_menu, className="nav")

    # We need to make sure that the user as access to the page
    # (direct url access)
    ac_list = pages_access.get(pathname, [RoleEnum.admin])
    if not any(user_role.has_access(ac) for ac in ac_list):
        return html.H1(["Page not found"]), menu

    return pages.get(pathname, html.H1(["Page not found"])), menu


def make_menu(pathname: str, user_role: RoleEnum) -> List[html.Li]:
    """Create the navbar menu, with selected navlink highlighted."""
    # You may filter the menu items there depending on user role
    menu_items = navbar_titles

    return [
        html.Li(dcc.Link(title, href=href), className="nav-item")
        if href != pathname
        else html.Li(dcc.Link(title, href=href), className="nav-item nav-item-focus")
        for href, title in menu_items.items()
    ]


if __name__ == "__main__":
    # Watch md & built files for full reload
    content_path = pathlib.Path(__file__).parent / "assets"
    builds_path = pathlib.Path(__file__).parent / "builds"
    extra_files = [*content_path.rglob("*.md"), *builds_path.rglob("*")]
    app.run_server(debug=True, extra_files=extra_files)
