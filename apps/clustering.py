import json
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.io as pio
import plotly.graph_objects as go

import utils
from app import app

# MD
with open("assets/contents/md_clustering.md", "r", encoding="utf-8") as f:
    content = utils.MarkdownReader(f.read())

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
                    id="type_selector_in",
                    options=[
                        {"label": k, "value": k}
                        for k in dico_plotly
                    ],
                    value=list(dico_plotly.keys())[0],
                    clearable=False
                    ),

            ]
        ),
        html.Div(id="type_selector_out"),
        html.Div(
            [
                content[2],
                dcc.Dropdown(
                    id="patient_selector_in",
                    clearable=False)
            ]
        ),
        html.Div(id="patient_selector_out"),
    ]
)

@app.callback(
    dash.dependencies.Output("patient_selector_in", component_property="options"),
    [
        dash.dependencies.Input("type_selector_in", component_property="value"),
    ],
)
def update_list_patients(key):
    return [{"label": i, "value": i} for i in dico_plotly[key] if i not in ['boxplot', 'tsne']]


@app.callback(
    dash.dependencies.Output("type_selector_out", component_property="children"),
    [
        dash.dependencies.Input("type_selector_in", component_property="value"),
    ],
)

def update_output(key):

    fig_tsne = go.Figure(dico_plotly[key]['tsne'])
    fig_boxplot = go.Figure(dico_plotly[key]['boxplot'])


    # if int(key) <= 15:
    #     fig_tsne.update_layout(height = 500, width = None)
    #     fig_boxplot.update_layout(height = 500, width = None)

    #     return utils.two_graphs(
    #         utils.graph(fig_tsne, loading=True),
    #         utils.graph(fig_boxplot, loading=True)
    #     )

    # else:

    fig_tsne.update_layout(height = 750, width = None)
    fig_boxplot.update_layout(height = 750, width = None)

    return [
        utils.graph(fig_tsne, loading=True),
        utils.graph(fig_boxplot, loading=True)
    ]


@app.callback(
    dash.dependencies.Output("patient_selector_in", component_property="value"),
    [
        dash.dependencies.Input("patient_selector_in", component_property="options")
    ],
)
def get_options(available_options):
    return available_options[0]["value"]

@app.callback(
    dash.dependencies.Output("patient_selector_out", component_property="children"),
    [
        dash.dependencies.Input("type_selector_in", component_property="value"),
        dash.dependencies.Input("patient_selector_in", component_property="value"),
    ],
)
def update_output(key, i):

    fig_list = dico_plotly[key][i]

    fig_enc_dec = go.Figure(fig_list[0])
    fig_enc_dec.update_layout(height = 500, width = None)
    fig_features = go.Figure(fig_list[1])
    fig_features.update_layout(height = 500, width = None)
    df_features = pd.DataFrame(fig_list[2])

    output = [
        utils.two_graphs(
            utils.graph(fig_enc_dec, loading=True),
            utils.graph(fig_features, loading=True)
        ),
        utils.table_from_df(df_features, title='Features'),
    ]
    return output
