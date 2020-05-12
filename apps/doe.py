import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pandas as pd
import plotly.graph_objects as go
import json

import utils

# Load markdown text content
with open("assets/contents/md_doe.md", "r", encoding="utf-8") as f:
    content = utils.MarkdownReader(f.read())

# Accuracy
filename = f"builds/dico_plotly_doe.json"
with open(filename, "r", encoding="utf-8") as f:
    dico_plotly_doe = json.load(f)

# Results clust
filename = f"builds/results_clust.csv"
df_results_clust = pd.read_csv(filename, index_col = 0)

# Results expl
filename = f"builds/results_explaination.csv"
df_results_explain = pd.read_csv(filename, index_col = 0)

# Define the page's content
i = iter(range(len(list(content))))

layout = html.Div(
    [
        content[next(i)],
        content[next(i)],
        utils.graph(dico_plotly_doe['accuracy'], loading=True),
        utils.graph(dico_plotly_doe['gap'], loading=True),
        content[next(i)],
        utils.graph(dico_plotly_doe['R'], loading=True),
        utils.graph(dico_plotly_doe['P'], loading=True),
        utils.graph(dico_plotly_doe['F'], loading=True),
        content[next(i)],
        content[next(i)],
        dash_table.DataTable(
            columns=[{"name" : tuple(x.split('_')), "id" : x} for x in df_results_clust.columns],
            data=df_results_clust.to_dict("rows"),
            merge_duplicate_headers=True,
            style_cell={'textAlign': 'left'}
            ),
        content[next(i)],
        dash_table.DataTable(
            columns=[{"name" : tuple(x.split('_')), "id" : x} for x in df_results_explain.columns],
            data=df_results_explain.to_dict("rows"),
            merge_duplicate_headers=True,
            style_cell={'textAlign': 'left'}
            )
    ]
)
