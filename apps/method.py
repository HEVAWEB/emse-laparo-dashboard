import dash_html_components as html

import utils


with open("assets/contents/methods.md", "r", encoding="utf-8") as f:
    content = utils.markdown_content(f.read())

layout = html.Div([content])
