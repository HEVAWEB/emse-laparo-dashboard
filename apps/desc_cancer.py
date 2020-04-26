import dash_html_components as html
import pandas as pd
import plotly.graph_objects as go
from dash.dependencies import Input, Output
from plotly.subplots import make_subplots

import utils
from app import app, plotly_theme
from .commons import toolbar

age_df = pd.read_csv("builds/desc_k_age.csv", encoding="cp1252", sep=";", thousands=" ")
age_dist_df = pd.read_csv(
    "builds/desc_k_age_dist.csv", encoding="cp1252", sep=";", thousands=" "
)
gender_df = pd.read_csv(
    "builds/desc_k_gender.csv", encoding="cp1252", sep=";", thousands=" "
)
meta_df = pd.read_csv(
    "builds/desc_k_meta.csv", encoding="cp1252", sep=";", thousands=" "
)
comor_df = pd.read_csv(
    "builds/desc_k_comor.csv", encoding="cp1252", sep=";", thousands=" "
)

base_color = plotly_theme["layout"]["colorway"][0]
counting_template = "%{y:.2%}<br>%{text} patient(s)"

layout = html.Div(
    [
        html.H3("Description des patients avec MTEV par cancer d'intérêt"),
        toolbar,
        html.Div([], id="fig-desc-age"),
        html.Div([], id="fig-desc-age-dist"),
        html.Div([], id="fig-desc-gender"),
        html.Div([], id="fig-desc-meta"),
        html.Div([], id="fig-desc-comor"),
        html.Div([], id="fig-desc-comor-focus"),
    ]
)


@app.callback(
    Output("fig-desc-age", "children"), [Input("tx-cancer-dropdown", "value")]
)
def update_age_figure(cancers):
    df = age_df.loc[age_df["Cancer"].isin(cancers)].sort_values(
        by="Médiane", ascending=False
    )
    fig = go.Figure(
        data=[go.Box(x=df["Cancer"], y=[])],
        layout={
            "title": "Distribution des âges par cancer",
            "yaxis": {"title": "Âge", "ticksuffix": " ans",},
            "margin": {"pad": 5, "t": 60, "l": 60},
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
    return utils.graph(fig)


@app.callback(
    Output("fig-desc-age-dist", "children"), [Input("tx-cancer-dropdown", "value")]
)
def update_age_dist_figure(cancers):
    df = age_dist_df.loc[age_dist_df["Cancer"].isin(cancers)]  # type: pd.DataFrame
    n_cancers = len(cancers)
    fig = make_subplots(
        rows=n_cancers,
        cols=1,
        shared_xaxes=True,
        vertical_spacing=0.12 - 0.007 * n_cancers,
        subplot_titles=df["Cancer"].to_list(),
        y_title="Proportion des patients",
    )

    x_values = list(df.columns[1:-1])

    y_values = df.drop(columns=["Cancer", "Total"]).div(df["Total"], axis=0).values

    for i, row in enumerate(df.itertuples(index=False), start=1):
        fig.add_trace(
            {
                "type": "bar",
                "x": x_values,
                "y": y_values[i - 1],
                "text": row[1:-1],
                "name": row.Cancer,
                "marker": {"color": base_color},
                "hovertemplate": "%{y:.2%}<br>%{text} patient(s)",
            },
            row=i,
            col=1,
        )
        fig["layout"]["annotations"][i - 1].update(x=0, xanchor="left")

    fig.update_layout(
        {
            "title": "Distribution des patients par âge et cancer",
            "showlegend": False,
            "height": 80 * n_cancers + 200,
            "margin": {"pad": 5, "t": 60, "l": 80},
        }
    )

    fig.update_yaxes(tickformat=".0%")
    fig.update_xaxes(title_text="Âge", row=n_cancers, col=1)

    return utils.graph(fig)


@app.callback(
    Output("fig-desc-gender", "children"), [Input("tx-cancer-dropdown", "value")]
)
def update_gender_figure(cancers):
    df = (
        gender_df.loc[gender_df["Cancer"].isin(cancers)]
        .assign(sorter=lambda x: x["Homme"] / x["Total"],)
        .sort_values(by="sorter", ascending=False)
    )

    fig = go.Figure(
        data=[
            go.Bar(
                x=df["Cancer"],
                y=df["Homme"] / df["Total"],
                text=df["Homme"],
                texttemplate="%{y:.1%}",
                hovertemplate=counting_template,
                textposition="outside",
                textfont_size=10,
                name="Homme",
            ),
            go.Bar(
                x=df["Cancer"],
                y=df["Femme"] / df["Total"],
                text=df["Femme"],
                texttemplate="%{y:.1%}",
                hovertemplate=counting_template,
                textposition="outside",
                textfont_size=10,
                name="Femme",
            ),
        ],
        layout={
            "title": "Dénombrement des patients par genre",
            "yaxis": {
                "title": "Proportion des patients",
                "autorange": True,
                "tickformat": ".1%",
            },
            "legend_title": "Genre",
            "margin": {"pad": 5, "t": 60, "l": 60, "r": 0},
            "bargroupgap": 0.05,
            "barmode": "stack",
        },
    )
    if len(cancers) > 6:
        fig.update_traces(textposition=None)
    return utils.graph(fig)


@app.callback(
    Output("fig-desc-meta", "children"), [Input("tx-cancer-dropdown", "value")]
)
def update_meta_figure(cancers):
    df = (
        meta_df.loc[meta_df["Cancer"].isin(cancers)]
        .assign(sorter=lambda x: x["Métastatique"] / x["Total"],)
        .sort_values(by="sorter", ascending=False)
    )

    fig = go.Figure(
        data=[
            go.Bar(
                x=df["Cancer"],
                y=df["Métastatique"] / df["Total"],
                text=df["Métastatique"],
                texttemplate="%{y:.1%}",
                hovertemplate=counting_template,
                textposition="outside",
                textfont_size=10,
                name="Oui",
            ),
            go.Bar(
                x=df["Cancer"],
                y=df["Non métastatique"] / df["Total"],
                text=df["Non métastatique"],
                texttemplate="%{y:.1%}",
                hovertemplate=counting_template,
                textposition="outside",
                textfont_size=10,
                name="Non",
            ),
        ],
        layout={
            "title": "Dénombrement des patients par présence de métastases",
            "yaxis": {
                "title": "Proportion des patients",
                "autorange": True,
                "tickformat": ".1%",
            },
            "legend_title": "Présence de<br>métastases",
            "margin": {"pad": 5, "t": 60, "l": 60, "r": 0},
            "bargroupgap": 0.05,
            "barmode": "stack",
        },
    )
    if len(cancers) > 6:
        fig.update_traces(textposition=None)
    return utils.graph(fig)


@app.callback(
    Output("fig-desc-comor", "children"), [Input("tx-cancer-dropdown", "value")]
)
def update_comor_figure(cancers):
    df = (
        comor_df.loc[comor_df["Cancer"].isin(cancers)]
        .assign(sorter=lambda x: x["Chimio. Total"] / x["Total"],)
        .sort_values(by="sorter", ascending=False)
    )

    fig = go.Figure(
        data=[
            go.Bar(
                x=df["Cancer"],
                y=df["Chirurgie"] / df["Total"],
                text=df["Chirurgie"],
                texttemplate="%{y:.1%}",
                hovertemplate=counting_template,
                textposition="outside",
                textfont_size=10,
                name="Chirurgie",
            ),
            go.Bar(
                x=df["Cancer"],
                y=df["Trauma"] / df["Total"],
                text=df["Trauma"],
                texttemplate="%{y:.1%}",
                hovertemplate=counting_template,
                textposition="outside",
                textfont_size=10,
                name="Trauma",
            ),
            go.Bar(
                x=df["Cancer"],
                y=df["AVC"] / df["Total"],
                text=df["AVC"],
                texttemplate="%{y:.1%}",
                hovertemplate=counting_template,
                textposition="outside",
                textfont_size=10,
                name="AVC",
            ),
            go.Bar(
                x=df["Cancer"],
                y=df["Insuffisance cardiaque"] / df["Total"],
                text=df["Insuffisance cardiaque"],
                texttemplate="%{y:.1%}",
                hovertemplate=counting_template,
                textposition="outside",
                textfont_size=10,
                name="Insuf. cardiaque",
            ),
            go.Bar(
                x=df["Cancer"],
                y=df["Grossesse"] / df["Total"],
                text=df["Grossesse"],
                texttemplate="%{y:.1%}",
                hovertemplate=counting_template,
                textposition="outside",
                textfont_size=10,
                name="Grossesse",
            ),
            go.Bar(
                x=df["Cancer"],
                y=df["Chimio. Total"] / df["Total"],
                text=df["Chimio. Total"],
                texttemplate="%{y:.1%}",
                hovertemplate=counting_template,
                textposition="outside",
                textfont_size=10,
                name="Chimio.",
            ),
        ],
        layout={
            "title": "Dénombrement des patients par comorbidité",
            "yaxis": {
                "title": "Proportion des patients",
                "autorange": True,
                "tickformat": ".1%",
            },
            "legend_title": "Comorbidités",
            "margin": {"pad": 5, "t": 60, "l": 60, "r": 0},
            "bargroupgap": 0.05,
        },
    )
    if len(cancers) > 6:
        fig.update_traces(textposition=None)
    return utils.graph(fig)


@app.callback(
    Output("fig-desc-comor-focus", "children"), [Input("tx-cancer-dropdown", "value")]
)
def update_comor_focus_figure(cancers):
    df = (
        comor_df.loc[comor_df["Cancer"].isin(cancers)]
        .assign(sorter=lambda x: x["Chimio. Total"] / x["Total"],)
        .sort_values(by="sorter", ascending=False)
    )

    fig = go.Figure(
        data=[
            go.Bar(
                x=df["Cancer"],
                y=df["Chimio. GHS"] / df["Total"],
                text=df["Chimio. GHS"],
                texttemplate="%{y:.1%}",
                hovertemplate=counting_template,
                textposition="outside",
                textfont_size=10,
                name="GHS",
            ),
            go.Bar(
                x=df["Cancer"],
                y=df["Chimio. SUS"] / df["Total"],
                text=df["Chimio. SUS"],
                texttemplate="%{y:.1%}",
                hovertemplate=counting_template,
                textposition="outside",
                textfont_size=10,
                name="SUS",
            ),
            go.Bar(
                x=df["Cancer"],
                y=df["Chimio. Acmonoclonaux"] / df["Total"],
                text=df["Chimio. Acmonoclonaux"],
                texttemplate="%{y:.1%}",
                hovertemplate=counting_template,
                textposition="outside",
                textfont_size=10,
                name="Acmonoclonaux",
            ),
        ],
        layout={
            "title": "Dénombrement des patients par comorbidité<br>"
            "<span style='font-size:12px'>Focus sur les chimiothérapies</span>",
            "yaxis": {
                "title": "Proportion des patients",
                "autorange": True,
                "tickformat": ".1%",
            },
            "legend_title": "Chimiothérapie",
            "margin": {"pad": 5, "t": 60, "l": 60, "r": 0},
            "bargroupgap": 0.05,
        },
    )
    if len(cancers) > 6:
        fig.update_traces(textposition=None)
    return utils.graph(fig)
