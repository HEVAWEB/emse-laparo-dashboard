import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
import plotly.graph_objs as go

import utils

with open("assets/contents/demo.md", "r", encoding="utf-8") as f:
    content = f.read()

df_volcano = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/volcano.csv"
)

traces_vol = [go.Heatmap(z=df_volcano.to_numpy())]
layout_vol = dict(title="Volcano heatmap - Sequential colorscale")
fig_vol = go.Figure(data=traces_vol, layout=layout_vol)

df_gap = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv"
)

traces_gap = [
    go.Scatter(
        x=df_continent["lifeExp"],
        y=df_continent["gdpPercap"],
        name=name,
        mode="markers",
        marker=dict(
            size=df_continent["pop"], sizeref=200000, sizemode="area", sizemin=4
        ),
        text=df_continent["country"],
    )
    for name, df_continent in df_gap.loc[df_gap["year"] == 2007].groupby("continent")
]
layout_gap = dict(title="Gapminder 2007 - Categorical colorway")
fig_gap = go.Figure(data=traces_gap, layout=layout_gap)

traces_vol2 = [
    go.Heatmap(z=df_volcano.to_numpy() - np.median(df_volcano.values), zmid=0)
]
layout_vol2 = dict(title="Volcano heatmap - Divergent colorscale")
fig_vol2 = go.Figure(data=traces_vol2, layout=layout_vol2)

del df_volcano
del df_gap

layout = html.Div(
    [
        utils.markdown_content(content),
        utils.graph(fig_vol),
        utils.graph(fig_gap),
        utils.graph(fig_vol2),
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
    ]
)
