import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input

from app import app
from apps import context, outcome, vars, results, method

app.layout = html.Div(
    [
        dcc.Location(id="url", refresh=False),
        html.Div(
            children=[
                html.H1("Dashboard"),
                html.Ul(
                    children=[
                        html.Li(dcc.Link("Context", href="/context")),
                        html.Li(dcc.Link("Outcome", href="/outcome")),
                        html.Li(dcc.Link("Variables", href="/vars")),
                        html.Li(dcc.Link("Results", href="/results")),
                        html.Li(dcc.Link("Methodology", href="/methods")),
                    ]
                ),
            ],
            className="two columns",
        ),
        html.Div(id="page-content", className="ten columns"),
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
