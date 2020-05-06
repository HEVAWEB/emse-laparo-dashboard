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
filename = f"builds/accuracy.json"
with open(filename, "r", encoding="utf-8") as f:
    fig_accuracy = json.load(f)
fig_accuracy = go.Figure(fig_accuracy)
fig_accuracy.update_layout(height = 500, width = None)

# Gap
filename = f"builds/gap.json"
with open(filename, "r", encoding="utf-8") as f:
    fig_gap = json.load(f)
fig_gap = go.Figure(fig_gap)
fig_gap.update_layout(height = 500, width = None)

# R
filename = f"builds/R.json"
with open(filename, "r", encoding="utf-8") as f:
    fig_R = json.load(f)
fig_R = go.Figure(fig_R)
fig_R.update_layout(height = 500, width = None)

# P
filename = f"builds/P.json"
with open(filename, "r", encoding="utf-8") as f:
    fig_P = json.load(f)
fig_P = go.Figure(fig_P)
fig_P.update_layout(height = 500, width = None)

# F
filename = f"builds/F.json"
with open(filename, "r", encoding="utf-8") as f:
    fig_F = json.load(f)
fig_F = go.Figure(fig_F)
fig_F.update_layout(height = 500, width = None)

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
        utils.graph(fig_accuracy, loading=True),
        utils.graph(fig_gap, loading=True),
        content[next(i)],
        utils.graph(fig_R, loading=True),
        utils.graph(fig_P, loading=True),
        utils.graph(fig_F, loading=True),
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
