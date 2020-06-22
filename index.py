import pathlib

import dash_core_components as dcc
import dash_html_components as html
import rgpd_dash
from dash.dependencies import Input, Output

from app import app, config
from apps import (
    context,
    eula,
    forms,
    method,
    desc_cancer,
    evt_cancer,
    pec_cancer,
    gallery,
    design,
    typography,
    buttons,
    composant,
)
from utils import __version__, translations

# Client - study configuration
CLIENT = "HEVA"
STUDY = "Dashboard Design"
LOGO_HEVA = "assets/logoHEVA_RVB.svg"
LOGO_CLIENT = "assets/pfizer.png"

# Change the webpage tab title here if needed
app.title = f"Artémis Design"

# Global title: Client - Study
title = [html.H2(CLIENT), html.H1(STUDY)]

# Pages links: add/remove entries if needed
pages = {
    # Default page
    "/": title + [context.layout],
    "/context": title + [context.layout],
    "/methods": method.layout,
    "/gallery": gallery.layout,
    "/design": design.layout,
    "/desc_cancer": desc_cancer.layout,
    "/evt_cancer": evt_cancer.layout,
    "/pec_cancer": pec_cancer.layout,
    "/eula": eula.layout,
    "/typo": typography.layout,
    "/button": buttons.layout,
    "/composants": composant.layout,
    "/form": forms.layout
}

# Navbar titles: which links & title to display on the navbar, add/remove entries if needed
navbar_titles = {
    "/typo": "S1 - Typographie",
    "/button": "S2 - Boutons",
    "/form": "S3 - Formulaires",
    "/composants": "Composants",
    "/context": "Contexte",
    "/methods": " Méthodologie",
    "/gallery": "Galerie des graphes",
    "/design": "Zone 51",
    "/desc_cancer": "Description des patients avec MTEV par cancer d'intérêt",
    "/evt_cancer": "Taux d'évènements de MTEV par cancer d'intérêt",
    "/pec_cancer": "Prise en charge des patients avec MTEV par cancer d'intérêt",
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
