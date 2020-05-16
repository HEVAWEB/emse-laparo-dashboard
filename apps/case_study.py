import json

import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output

import utils
from app import app, plotly_theme

# MD
with open("assets/contents/md_case_study.md", "r", encoding="utf-8") as f:
    content = utils.MarkdownReader(f.read())

# data plotly
filename = f"builds/dico_plotly.json"

with open(filename, "r", encoding="utf-8") as f:
    dico_plotly = json.load(f)

layout = html.Div(
    [
        content[0],
        html.Div(
            [
                content[1],
                dcc.Dropdown(
                    id="nbclust_selector_in",
                    options=[{"label": k, "value": k} for k in dico_plotly],
                    value=list(dico_plotly.keys())[1],
                    clearable=False,
                    placeholder="Select the number of clusters",
                ),
            ]
        ),
        html.Div(id="nbclust_selector_out"),
        html.Div(
            [
                content[3],
                dcc.Dropdown(
                    id="cluster_selector_in",
                    clearable=False,
                    placeholder="Select the cluster",
                ),
            ]
        ),
        html.Div(id="cluster_selector_out"),
    ]
)


@app.callback(
    Output("cluster_selector_in", "options"), [Input("nbclust_selector_in", "value"),],
)
def update_list_clusters(key):
    return [
        {"label": i, "value": i}
        for i in dico_plotly[key]
        if i not in ["boxplot", "tsne"]
    ]


@app.callback(
    Output("nbclust_selector_out", "children"),
    [Input("nbclust_selector_in", "value"),],
)
def update_output(key):
    fig_tsne = dico_plotly[key]["tsne"]
    fig_tsne["layout"]["template"] = plotly_theme
    fig_boxplot = dico_plotly[key]["boxplot"]
    fig_boxplot["layout"]["template"] = plotly_theme

    img_apollo = html.Div([
            content[2],
            html.Img(
            src= f'assets/apollo/apollo_{key}.png',
            width='50%',
            style={
                "align": "middle"
                }
            )
    ]
    )

    return [img_apollo, utils.graph(fig_tsne, loading=True), utils.graph(fig_boxplot, loading=True)]


@app.callback(
    Output("cluster_selector_in", "value"), [Input("cluster_selector_in", "options")],
)
def get_options(available_options):
    return available_options[0]["value"]


@app.callback(
    Output("cluster_selector_out", "children"),
    [Input("nbclust_selector_in", "value"), Input("cluster_selector_in", "value"),],
)
def update_output(key, i):
    fig_list = dico_plotly[key][i]

    fig_enc_dec = fig_list[0]
    fig_enc_dec["layout"]["template"] = plotly_theme
    fig_features = fig_list[1]
    fig_features["layout"]["template"] = plotly_theme
    df_features = pd.DataFrame(fig_list[2])

    output = [
        utils.two_graphs(
            utils.graph(fig_enc_dec, loading=True),
            utils.graph(fig_features, loading=True),
        ),
        utils.table_from_df(df_features, title="Features"),
    ]
    return output
