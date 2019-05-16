import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from app import config

with open("assets/demo.md", "r", encoding="utf-8") as f:
    content = f.read()

fig = go.Figure(
    data=[go.Scatter(x=(1, 2, 3), y=(4, 2, 6))], layout=dict(title="Some simple graph")
)

layout = html.Div(
    [
        dcc.Markdown([content]),
        html.Div([dcc.Graph(figure=fig, config=config)], className="graph"),
    ]
)
