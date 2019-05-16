import dash_core_components as dcc
import dash_html_components as html

with open("assets/demo.md", "r", encoding="utf-8") as f:
    content = f.read()

layout = html.Div([dcc.Markdown([content])])
