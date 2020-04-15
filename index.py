import pathlib

import dash_core_components as dcc
import dash_html_components as html
import rgpd_dash
from dash.dependencies import Input, Output

from app import app, config
from apps import context, eula, method, desc_cancer, evt_cancer, pec_cancer
from utils import __version__, translations

# Client - study configuration
CLIENT = "Pfizer"
STUDY = "MTEV"
LOGO_HEVA = "assets/logoHEVA_RVB.svg"
LOGO_CLIENT = "assets/pfizer.png"

# Change the webpage tab title here if needed
app.title = f"{CLIENT} {STUDY}"

# Global title: Client - Study
title = [html.H2(CLIENT), html.H1(STUDY)]

# Sidebar links: add/remove entries if needed
menu = html.Ul(
    children=[
        html.Li(dcc.Link("Contexte", href="/context"), className="nav-item"),
        html.Li(dcc.Link("Méthodologie", href="/methods"), className="nav-item"),
        html.Li(
            dcc.Link(
                "Description des patients avec MTEV par cancer d'intérêt",
                href="/desc_cancer",
            ),
            className="nav-item",
        ),
        html.Li(
            dcc.Link(
                "Taux d'évènements de MTEV par cancer d'intérêt", href="/evt_cancer"
            ),
            className="nav-item",
        ),
        html.Li(
            dcc.Link(
                "Prise en charge des patients avec MTEV par cancer d'intérêt",
                href="/pec_cancer",
            ),
            className="nav-item",
        ),
    ],
    className="nav",
)
pages = {
    # Default page
    "/": title + [context.layout],
    "/context": title + [context.layout],
    "/methods": method.layout,
    "/desc_cancer": desc_cancer.layout,
    "/evt_cancer": evt_cancer.layout,
    "/pec_cancer": pec_cancer.layout,
    "/eula": eula.layout,
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
                                            menu, className="navbar-section nav-links"
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


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    """ Update page content with sidebar links"""
    return pages.get(pathname, html.H1(["Page not found"]))


if __name__ == "__main__":
    # Watch md & built files for full reload
    content_path = pathlib.Path(__file__).parent / "assets"
    builds_path = pathlib.Path(__file__).parent / "builds"
    extra_files = [*content_path.rglob("*.md"), *builds_path.rglob("*")]
    app.run_server(debug=True, extra_files=extra_files)
