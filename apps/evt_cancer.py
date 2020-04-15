import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
import plotly.graph_objs as go
import xarray as xr
from dash.dependencies import Input, Output

import utils
from app import app
from .common_cancer import OPTIONS_CANCER

TYPE_NAMES = {
    "total": "MTEV total",
    "m": "Embolie pulmonaire",
    "t": "Thrombose veineuse",
}

# Dataset construction from .csv results
tx_tot_df = pd.read_csv(
    "builds/tx_k_tot.csv", encoding="cp1252", sep=";", thousands=" "
)
tx_t_df = pd.read_csv("builds/tx_k_t.csv", encoding="cp1252", sep=";", thousands=" ")
tx_m_df = pd.read_csv("builds/tx_k_m.csv", encoding="cp1252", sep=";", thousands=" ")

ds = xr.Dataset(
    data_vars={
        "n": (["cancer"], tx_tot_df["n"]),
        "n_mtev": (
            ["cancer", "type"],
            np.array(
                [
                    tx_tot_df["n_mtev"].values,
                    tx_t_df["n_mtev"].values,
                    tx_m_df["n_mtev"].values,
                ]
            ).T,
        ),
        "tx": (
            ["cancer", "type"],
            np.array(
                [tx_tot_df["tx"].values, tx_t_df["tx"].values, tx_m_df["tx"].values,]
            ).T,
        ),
    },
    coords={"cancer": tx_tot_df["cancer"].to_list(), "type": ["total", "t", "m"]},
)

del tx_t_df, tx_m_df, tx_tot_df

layout = html.Div(
    [
        html.H3("Taux d'évènements de MTEV par cancer d'intérêt"),
        utils.toolbar(
            [
                html.Div(
                    [html.Label(["Cancer(s)"], className="form-label")],
                    className="col-2 col-sm-12",
                ),
                html.Div(
                    [
                        dcc.Dropdown(
                            id="tx-cancer-dropdown",
                            options=OPTIONS_CANCER,
                            multi=True,
                            value=["Digestif bas", "Digestif haut", "Glioblastome"],
                            clearable=False,
                        ),
                    ],
                    className="col-10 col-sm-12",
                ),
            ]
        ),
        html.Div([], id="fig-tx-tot"),
        utils.markdown_content("Commentaire des données à rajouter."),
        utils.takeaways("Conclusion à rajouter."),
    ]
)


@app.callback(Output("fig-tx-tot", "children"), [Input("tx-cancer-dropdown", "value")])
def update_figures(cancers):
    sub_ds = ds.sel(cancer=cancers)
    size_ref = sub_ds["n_mtev"].max().item() / 30 ** 2

    if len(cancers) <= 5:
        fig = create_fig_few_points(sub_ds, size_ref)
    else:
        fig = create_fig_many_points(sub_ds, size_ref)

    return utils.graph(fig)


def create_fig_few_points(ds: xr.Dataset, size_ref):
    data = []

    ds = ds.sortby(ds.sel(type="total")["tx"], ascending=False)
    for name, da in ds.groupby("type"):
        da = da.squeeze("type", drop=True)

        full_name = TYPE_NAMES.get(name)

        data.append(
            go.Scatter(
                x=da["cancer"],
                y=da["tx"],
                marker={
                    "size": da["n_mtev"],
                    "sizemin": 3,
                    "sizeref": size_ref,
                    "sizemode": "area",
                },
                mode="markers",
                name=full_name,
                text=da["n_mtev"],
                customdata=da["n"],
                hovertemplate="<b>%{x}</b><br>"
                "N total : <b>%{customdata}</b><br>"
                f"N {full_name} : <b>"
                "%{text}</b><br>"
                "Taux : <b>%{y:.1%}</b><extra></extra>",
            )
        )

    fig = go.Figure(
        data=data,
        layout={
            "title": "Taux d'événements de MTEV par cancer",
            "yaxis": {
                "tickformat": ".1%",
                "title": "Taux d'événements",
                "rangemode": "tozero",
                "zerolinecolor": "#9491AD",
            },
            "hovermode": "x",
            "legend": {"title": "Dénombrement"},
            "margin": {"pad": 5},
        },
    )
    return fig


def create_fig_many_points(ds: xr.Dataset, size_ref):
    data = []

    ds = ds.sortby(ds.sel(type="total")["tx"], ascending=True)
    for name, da in ds.groupby("type"):
        da = da.squeeze("type", drop=True)

        full_name = TYPE_NAMES.get(name)

        data.append(
            go.Scatter(
                y=da["cancer"],
                x=da["tx"],
                marker={
                    "size": da["n_mtev"],
                    "sizemin": 3,
                    "sizeref": size_ref,
                    "sizemode": "area",
                },
                mode="markers",
                name=full_name,
                text=da["n_mtev"],
                customdata=da["n"],
                hovertemplate="<b>%{y}</b><br>"
                "N total : <b>%{customdata}</b><br>"
                f"N {full_name} : <b>"
                "%{text}</b><br>"
                "Taux : <b>%{x:.1%}</b><extra></extra>",
            )
        )

    fig = go.Figure(
        data=data,
        layout={
            "title": "Taux d'événements de MTEV par cancer",
            "xaxis": {
                "tickformat": ".1%",
                "title": "Taux d'événements",
                "rangemode": "tozero",
                "zerolinecolor": "#9491AD",
            },
            "yaxis": {"automargin": True},
            "hovermode": "closest",
            "legend": {"title": "Dénombrement"},
            "margin": {"pad": 5},
        },
    )
    return fig
