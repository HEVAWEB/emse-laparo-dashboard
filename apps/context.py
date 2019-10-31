import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objects as go

import utils

# Load markdown text content
with open("assets/contents/demo.md", "r", encoding="utf-8") as f:
    content = utils.MarkdownReader(f.read())

# Make the simple plot
simple_fig = go.Figure(
    data=[go.Scatter(x=[0, 1, 2, 3, 4], y=[2, 3, 4, 6, 1])],
    layout=dict(
        title="Un graphe simple",
        margin=dict(r=10, l=20),
        xaxis=dict(automargin=True),
        yaxis=dict(automargin=True),
    ),
)

# Description dataframe for datatables
df = pd.read_csv("builds/description.csv")

# Define the page's content
layout = html.Div(
    [
        content[0],
        utils.table_from_df(
            df, title="Orientez les tables en largeur...", orient_vertically=False
        ),
        utils.two_graphs(
            utils.table_from_df(
                df, title="... ou en hauteur !", orient_vertically=True
            ),
            utils.table_from_csv("builds/iris.csv", "Table CSV directe"),
        ),
        content[1],
        utils.takeaways("Le Markdown c'est cool."),
        content[2],
        utils.two_graphs(content[3], utils.graph(simple_fig)),
        utils.two_graphs(utils.graph(simple_fig), utils.graph(simple_fig)),
        content[4],
        html.H3(["Zone expérimentale - Réservée au design !"]),
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
