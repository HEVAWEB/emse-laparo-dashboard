import dash_html_components as html
import dash_table
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

# Datatable
df_iris = pd.read_csv("builds/iris.csv")
table = dash_table.DataTable(
    columns=[{"name": i, "id": i} for i in df_iris.columns],
    data=df_iris.to_dict(orient="records"),
    export_format="csv",
    sort_action="native",
)

i_content = iter(content)
# Define the page's content
layout = html.Div(
    [
        next(i_content),
        utils.table_from_df(
            df, title="Orientez les tables en largeur...", orient_vertically=False
        ),
        utils.table_from_df(df, title="... ou en hauteur !", orient_vertically=True),
        utils.table_from_csv("builds/iris.csv", "Table CSV directe"),
        next(i_content),
        utils.takeaways("Le Markdown c'est cool."),
        next(i_content),
        utils.two_graphs(content[3], utils.graph(simple_fig)),
        utils.two_graphs(utils.graph(simple_fig), utils.graph(simple_fig)),
        next(i_content),
        next(i_content),
    ]
)
