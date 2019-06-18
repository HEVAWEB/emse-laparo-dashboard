import dash_html_components as html
import plotly.graph_objs as go

import utils

with open("assets/contents/demo.md", "r", encoding="utf-8") as f:
    content = f.read()

fig = go.Figure(
    data=[go.Scatter(x=(1, 2, 3), y=(4, 2, 6))], layout=dict(title="Some simple graph")
)

layout = html.Div(
    [
        utils.markdown_content(content),
        utils.graph(fig),
        utils.takeaways(
            "This is a conclusion section written again with **Markdown**. It has its own utils component."
        ),
        utils.markdown_content("You can integrate tables like graphs"),
        utils.simple_table(
            """| Tables |  Are | Cool |
            |----------|:-------------:|------:|
            | col 1 is | left-aligned | $1600 |
            | col 2 is | centered | $12 |
            | col 3 is | *right-aligned* |**$1** |"""
        ),
    ]
)
