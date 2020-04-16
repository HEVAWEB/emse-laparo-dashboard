import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Output, Input
from dash_table import DataTable

import utils
from app import app
from .commons import toolbar

pass_df = pd.read_csv(
    "builds/pec_k_pass.csv", encoding="cp1252", sep=";", thousands=" "
).sort_values(by="Soins intensifs", ascending=False)

proc_df = pd.read_csv(
    "builds/pec_k_proc.csv", encoding="cp1252", sep=";", thousands=" "
).sort_values(by="Thromboaspiration", ascending=False)

urg_df = pd.read_csv(
    "builds/pec_k_urg.csv", encoding="cp1252", sep=";", thousands=" "
).sort_values(by="Oui", ascending=False)

out_df = pd.read_csv(
    "builds/pec_k_out.csv", encoding="cp1252", sep=";", thousands=" "
).sort_values(by="Retour au domicile", ascending=False)

costs_df = pd.read_csv(
    "builds/pec_k_costs.csv", encoding="cp1252", sep=";", thousands=" "
).sort_values(by="Moyenne", ascending=False)

sej_dur_df = pd.read_csv(
    "builds/pec_k_sej_dur.csv", encoding="cp1252", sep=";", thousands=" "
).sort_values(by="Moyenne", ascending=False)

sej_df = pd.read_csv(
    "builds/pec_k_sej.csv", encoding="cp1252", sep=";", thousands=" "
).sort_values(by="Moyenne", ascending=False)

layout = html.Div(
    [
        html.H3("Prise en charge des patients avec MTEV par cancer d'intérêt"),
        toolbar,
        html.Div([], id="table-pec-sej"),
        html.Div([], id="fig-pec-sej_dur"),
        html.Div([], id="fig-pec-pass"),
        html.Div([], id="fig-pec-proc"),
        html.Div([], id="fig-pec-urg"),
        html.Div([], id="fig-pec-out"),
        html.Div([], id="fig-pec-costs"),
    ]
)


@app.callback(
    Output("fig-pec-pass", "children"), [Input("tx-cancer-dropdown", "value")]
)
def update_pass_figure(cancers):
    df = pass_df.loc[pass_df["Cancer"].isin(cancers)]
    fig = go.Figure(
        data=[
            go.Bar(
                x=df["Cancer"],
                y=df["Réanimation"],
                text=df["Réanimation"],
                hoverinfo="text+name",
                textposition="outside",
                textfont_size=10,
                name="Réanimation",
            ),
            go.Bar(
                x=df["Cancer"],
                y=df["Soins intensifs"],
                text=df["Soins intensifs"],
                hoverinfo="text+name",
                textposition="outside",
                textfont_size=10,
                name="Soins intensifs",
            ),
            go.Bar(
                x=df["Cancer"],
                y=df["Surveillance continue"],
                text=df["Surveillance continue"],
                hoverinfo="text+name",
                textposition="outside",
                textfont_size=10,
                name="Surveillance continue",
            ),
        ],
        layout={
            "title": "Dénombrement des patients par type de passage",
            "yaxis": {"title": "Nombre de patients"},
            "legend_title": "Type de passage",
            "margin": {"pad": 5, "t": 60, "l": 50, "r": 0},
        },
    )
    if len(cancers) > 6:
        fig.update_traces(textposition=None)
    return utils.graph(fig)


@app.callback(
    Output("fig-pec-proc", "children"), [Input("tx-cancer-dropdown", "value")]
)
def update_proc_figure(cancers):
    df = proc_df.loc[proc_df["Cancer"].isin(cancers)]
    fig = go.Figure(
        data=[
            go.Bar(
                x=df["Cancer"],
                y=df["Thromvectomie"],
                text=df["Thromvectomie"],
                hoverinfo="text+name",
                textposition="outside",
                textfont_size=10,
                name="Thromvectomie",
            ),
            go.Bar(
                x=df["Cancer"],
                y=df["Thromboaspiration"],
                text=df["Thromboaspiration"],
                hoverinfo="text+name",
                textposition="outside",
                textfont_size=10,
                name="Thromboaspiration",
            ),
            go.Bar(
                x=df["Cancer"],
                y=df["Fibrinolyse"],
                text=df["Fibrinolyse"],
                hoverinfo="text+name",
                textposition="outside",
                textfont_size=10,
                name="Fibrinolyse",
            ),
        ],
        layout={
            "title": "Dénombrement des patients par procédure réalisée",
            "yaxis": {"title": "Nombre de patients"},
            "legend_title": "Procédure",
            "margin": {"pad": 5, "t": 60, "l": 50, "r": 0},
        },
    )
    if len(cancers) > 6:
        fig.update_traces(textposition=None)
    return utils.graph(fig)


@app.callback(Output("fig-pec-urg", "children"), [Input("tx-cancer-dropdown", "value")])
def update_urg_figure(cancers):
    df = urg_df.loc[urg_df["Cancer"].isin(cancers)]
    fig = go.Figure(
        data=[
            go.Bar(
                x=df["Cancer"],
                y=df["Oui"],
                text=df["Oui"],
                hoverinfo="text+name",
                textposition="outside",
                textfont_size=10,
                name="Oui",
            ),
            go.Bar(
                x=df["Cancer"],
                y=df["Non"],
                text=df["Non"],
                hoverinfo="text+name",
                textposition="outside",
                textfont_size=10,
                name="Non",
            ),
        ],
        layout={
            "title": "Dénombrement des patients par mode d'arrivée",
            "yaxis": {"title": "Nombre de patients", "autorange": True},
            "legend_title": "Arrivée par les urgences",
            "margin": {"pad": 5, "t": 60, "l": 50, "r": 0},
        },
    )
    if len(cancers) > 6:
        fig.update_traces(textposition=None)
    return utils.graph(fig)


@app.callback(Output("fig-pec-out", "children"), [Input("tx-cancer-dropdown", "value")])
def update_out_figure(cancers):
    df = out_df.loc[out_df["Cancer"].isin(cancers)]
    fig = go.Figure(
        data=[
            go.Bar(
                x=df["Cancer"],
                y=df["Retour au domicile"],
                text=df["Retour au domicile"],
                hoverinfo="text+name",
                textposition="outside",
                textfont_size=10,
                name="Retour au domicile",
            ),
            go.Bar(
                x=df["Cancer"],
                y=df["Transfert définitif"],
                text=df["Transfert définitif"],
                hoverinfo="text+name",
                textposition="outside",
                textfont_size=10,
                name="Transfert définitif",
            ),
            go.Bar(
                x=df["Cancer"],
                y=df["Transfert provisoire "],
                text=df["Transfert provisoire "],
                hoverinfo="text+name",
                textposition="outside",
                textfont_size=10,
                name="Transfert provisoire ",
            ),
            go.Bar(
                x=df["Cancer"],
                y=df["Mutation vers une autre unité médicale"],
                text=df["Mutation vers une autre unité médicale"],
                hoverinfo="text+name",
                textposition="outside",
                textfont_size=10,
                name="Mutation vers<br>une autre unité médicale",
            ),
            go.Bar(
                x=df["Cancer"],
                y=df["Décès"],
                text=df["Décès"],
                hoverinfo="text+name",
                textposition="outside",
                textfont_size=10,
                name="Décès",
            ),
        ],
        layout={
            "title": "Dénombrement des patients par mode de sortie",
            "yaxis": {"title": "Nombre de patients", "autorange": True},
            "legend_title": "Mode de sortie",
            "margin": {"pad": 5, "t": 60, "l": 50, "r": 0},
        },
    )
    if len(cancers) > 6:
        fig.update_traces(textposition=None)
    return utils.graph(fig)


@app.callback(
    Output("fig-pec-costs", "children"), [Input("tx-cancer-dropdown", "value")]
)
def update_costs_figure(cancers):
    df = costs_df.loc[costs_df["Cancer"].isin(cancers)]
    fig = go.Figure(
        data=[go.Box(x=df["Cancer"], y=[])],
        layout={
            "title": "Distribution des coûts de séjour",
            "yaxis": {
                "title": "Coût de séjour",
                "range": [0, 15000],
                "ticksuffix": " €",
            },
            "margin": {"pad": 5, "t": 60, "l": 50},
        },
    )
    fig.update_traces(
        q1=df["Q1"],
        median=df["Médiane"],
        q3=df["Q3"],
        lowerfence=df["Minimum"],
        upperfence=df["Maximum"],
        mean=df["Moyenne"],
    )
    table = DataTable(
        id="table-costs",
        columns=[{"name": i, "id": i, "type": "numeric"} for i in df.columns],
        data=df.to_dict("records"),
        sort_action="native",
        style_table={"maxHeight": "440px"},
        fixed_rows={"headers": True},
        style_cell={"width": "100px"},
    )
    # utils.table_from_df(df, title="Table des coûts de séjour (€)")
    return html.Div(
        [
            utils.graph(fig),
            html.Div(
                [html.H4("Table des coûts de séjours (€)"), table], className="graph"
            ),
        ]
    )


@app.callback(
    Output("fig-pec-sej_dur", "children"), [Input("tx-cancer-dropdown", "value")]
)
def update_sej_dur_figure(cancers):
    df = sej_dur_df.loc[sej_dur_df["Cancer"].isin(cancers)]
    fig = go.Figure(
        data=[go.Box(x=df["Cancer"], y=[])],
        layout={
            "title": "Distribution des durées de séjour",
            "yaxis": {"title": "Durée de séjour", "range": [0, 25], "ticksuffix": " j"},
            "margin": {"pad": 5, "t": 60, "l": 50},
        },
    )
    fig.update_traces(
        q1=df["Q1"],
        median=df["Médiane"],
        q3=df["Q3"],
        lowerfence=df["Minimum"],
        upperfence=df["Maximum"],
        mean=df["Moyenne"],
    )
    table = DataTable(
        id="table-costs",
        columns=[{"name": i, "id": i, "type": "numeric"} for i in df.columns],
        data=df.to_dict("records"),
        sort_action="native",
        style_table={"maxHeight": "440px"},
        fixed_rows={"headers": True},
        style_cell={"width": "100px"},
    )
    # utils.table_from_df(df, title="Table des coûts de séjour (€)")
    return html.Div(
        [
            utils.graph(fig),
            html.Div(
                [html.H4("Table des durées de séjours (jour)"), table],
                className="graph",
            ),
        ]
    )


@app.callback(
    Output("table-pec-sej", "children"), [Input("tx-cancer-dropdown", "value")]
)
def update_sej_table(cancers):
    df = sej_df.loc[sej_df["Cancer"].isin(cancers)]

    table = DataTable(
        id="table-costs",
        columns=[{"name": i, "id": i, "type": "numeric"} for i in df.columns],
        data=df.to_dict("records"),
        sort_action="native",
        style_table={"maxHeight": "440px"},
        fixed_rows={"headers": True},
        style_cell={"width": "100px"},
    )
    # utils.table_from_df(df, title="Table des coûts de séjour (€)")
    return html.Div(
        [html.Div([html.H4("Dénombrement des séjours MTEV"), table], className="graph")]
    )
