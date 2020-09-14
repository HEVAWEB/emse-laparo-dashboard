import json

import dash_html_components as html
import dash_table
import pandas as pd

import utils

# Load markdown text content
with open("assets/contents/md_doe.md", "r", encoding="utf-8") as f:
    content = iter(utils.MarkdownReader(f.read()))

# Accuracy
filename = f"builds/dico_plotly_doe.json"
with open(filename, "r", encoding="utf-8") as f:
    dico_plotly_doe = json.load(f)

# Results clust
filename = f"builds/results_clust.csv"
df_results_clust = pd.read_csv(filename, index_col=0)

# Results expl
filename = f"builds/results_explaination.csv"
df_results_explain = pd.read_csv(filename, index_col=0)

# Define the page's content

def make_table(df):
    return dash_table.DataTable(
        columns=[
            {"name": tuple(x.split("_")), "id": x}
            for x in df.columns
        ],
        data=df.to_dict("records"),
        style_table=dict(overflowX="auto"),
        merge_duplicate_headers=True,
        style_cell={"textAlign": "center"},
        style_data_conditional=[
            {
                'if': {
                    'column_id': ['__kappa', '__alpha', '__beta', '__gamma'],
                },
                'fontWeight': 'bold'
            }
        ]
    )


layout = html.Div(
    [
        next(content),
        next(content),
        utils.graph(dico_plotly_doe["accuracy"], loading=True),
        utils.graph(dico_plotly_doe["gap"], loading=True),
        next(content),
        utils.graph(dico_plotly_doe["R"], loading=True),
        utils.graph(dico_plotly_doe["P"], loading=True),
        utils.graph(dico_plotly_doe["F"], loading=True),
        next(content),
        next(content),
        make_table(df_results_clust),
        next(content),
        make_table(df_results_explain),
    ]
)
