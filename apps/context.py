import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

import utils

# Load markdown text content
with open("assets/contents/demo.md", "r", encoding="utf-8") as f:
    content = f.read()

# Define the page's content
layout = html.Div(
    [
        utils.markdown_content(content),
        utils.takeaways(
            "This is a conclusion section written again with **Markdown**. It has its own utils component."
        ),
        utils.markdown_content("You can integrate tables like graphs"),
        utils.table_from_md(
            """| Tables |  Are | Cool |
            |----------|:-------------:|------:|
            | col 1 is | left-aligned | $1600 |
            | col 2 is | centered | $12 |
            | col 3 is | *right-aligned* |**$1** |"""
        ),
        utils.table_from_df(pd.read_csv("builds/iris.csv")),
        html.H3(["Components"]),
        html.H4(["Dropdown"]),
        dcc.Dropdown(
            options=[
                {"label": "New York City", "value": "NYC"},
                {"label": "Montréal", "value": "MTL"},
                {"label": "San Francisco", "value": "SF"},
            ],
            value="MTL",
        ),
        html.H4(["Slider"]),
        dcc.Slider(
            min=0, max=9, marks={i: "Label {}".format(i) for i in range(10)}, value=5
        ),
        html.H4(["Range Slider"]),
        dcc.RangeSlider(count=1, min=-5, max=10, step=0.5, value=[-3, 7]),
        html.H4(["Simple Input"]),
        dcc.Input(placeholder="Enter a value...", type="text", value=""),
        html.H4(["Textarea"]),
        dcc.Textarea(
            placeholder="Enter a value...",
            value="This is a TextArea component",
            style={"width": "100%"},
        ),
        html.H4(["Checklist"]),
        dcc.Checklist(
            options=[
                {"label": "New York City", "value": "NYC"},
                {"label": "Montréal", "value": "MTL"},
                {"label": "San Francisco", "value": "SF"},
            ],
            value=["MTL", "SF"],
        ),
        html.H4(["Radio items"]),
        dcc.RadioItems(
            options=[
                {"label": "New York City", "value": "NYC"},
                {"label": "Montréal", "value": "MTL"},
                {"label": "San Francisco", "value": "SF"},
            ],
            value="MTL",
        ),
        html.H4(["Button"]),
        html.Button("Submit", id="button"),
        utils.markdown_content(
            "We would like all components except those with a grey background to have a margin with end of page."
        ),
    ]
)
