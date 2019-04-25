import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input

from app import app
from apps import context, outcome, vars, results, method


app.layout = html.Div(
    [
        html.Link(href="/assets/style.css", rel="stylesheet"),
        dcc.Location(id="url", refresh=False),
        html.Div(
            [
                html.Div(
                    children=[
                        html.Img(
                            src="assets/logoHEVA_RVB.svg", className="img-responsive"
                        ),
                        html.H1("Dashboard"),
                        html.Ul(
                            children=[
                                html.Li(
                                    dcc.Link("Context", href="/context"),
                                    className="nav-item",
                                ),
                                html.Li(
                                    dcc.Link("Outcome", href="/outcome"),
                                    className="nav-item",
                                ),
                                html.Li(
                                    dcc.Link("Variables", href="/vars"),
                                    className="nav-item",
                                ),
                                html.Li(
                                    dcc.Link("Results", href="/results"),
                                    className="nav-item",
                                ),
                                html.Li(
                                    dcc.Link("Methodology", href="/methods"),
                                    className="nav-item",
                                ),
                            ],
                            className="nav",
                        ),
                    ],
                    className="column col-2",
                ),
                html.Div(id="page-content", className="column col-10"),
            ],
            className="columns",
        ),
    ]
)


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/context" or pathname == "/":
        return context.layout
    elif pathname == "/outcome":
        return outcome.layout
    elif pathname == "/methods":
        return method.layout
    elif pathname == "/vars":
        return vars.layout
    elif pathname == "/results":
        return results.layout
    else:
        return "404 Not Found"


if __name__ == "__main__":
    app.run_server(debug=True, port=8051)
