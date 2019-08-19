import dash_html_components as html
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

import utils

df_volcano = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/volcano.csv"
)

df_gap = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv"
)


heatmap_volcano = go.Figure(
    data=[go.Heatmap(z=df_volcano.to_numpy())],
    layout=dict(title="Volcano heatmap - Sequential colorscale"),
)
scatter_gapminder = go.Figure(
    data=[
        go.Scatter(
            x=df_continent["lifeExp"],
            y=df_continent["gdpPercap"],
            name=name,
            mode="markers",
            marker=dict(
                size=df_continent["pop"], sizeref=200000, sizemode="area", sizemin=4
            ),
            text=df_continent["country"],
        )
        for name, df_continent in df_gap.loc[df_gap["year"] == 2007].groupby(
            "continent"
        )
    ],
    layout=dict(
        title="Gapminder 2007 - Categorical colorway",
        hovermode="closest",
        xaxis=dict(title="Life expectancy (years)"),
        yaxis=dict(title="GDP per capita ($)"),
    ),
)

scatter_gapminder2 = px.scatter(
    df_gap,
    x="lifeExp",
    y="gdpPercap",
    color="continent",
    hover_name="country",
    animation_frame="year",
    animation_group="country",
    size="pop",
    size_max=100,
).update_layout(
    title="Using Ploty Express & animated",
    xaxis=dict(title="Life expectancy (years)", range=[20, 100]),
    yaxis=dict(title="GDP per capita ($)", range=[0, 60000]),
    hovermode="closest",
)

line_gapminder = go.Figure(
    data=[
        go.Scatter(
            x=df_gap["year"].unique(),
            y=df_gap.loc[df_gap["country"] == country]["lifeExp"],
            name=country,
        )
        for country in ("France", "Germany", "Italy", "Belgium", "Spain")
    ],
    layout=dict(
        title="Life expectancy in Europe",
        xaxis=dict(title="Year"),
        yaxis=dict(title="Life expectancy (years)"),
    ),
)

europe_countries = list(df_gap[df_gap["continent"] == "Europe"]["country"].unique())

bar_gapminder = go.Figure(
    data=[
        go.Bar(
            x=europe_countries,
            y=df_gap[
                (df_gap["year"] == 2007) & (df_gap["country"].isin(europe_countries))
            ]["gdpPercap"],
        )
    ],
    layout=dict(
        title="Gapminder 2007 Europe GDPs", yaxis=dict(title="GDP per capita ($)")
    ),
)

histogram_gapminder = px.histogram(
    df_gap.loc[df_gap["year"] == 2007], x="continent", y="country"
).update_layout(
    title="Gapminder Countries per continent",
    yaxis_title="# coutries",
    xaxis_title="Continent",
)

boxplot_gapminder = px.box(
    df_gap.loc[df_gap["year"] == 2007], x="continent", y="lifeExp"
).update_layout(
    title="Life expectancy per continent",
    yaxis_title="Life expectancy (years)",
    xaxis_title="Continent",
)

scaled_volcano = (
    df_volcano.to_numpy()
    - (np.max(df_volcano.to_numpy()) + np.min(df_volcano.to_numpy())) / 2
)

heatmap_volcano_2 = go.Figure(
    data=[
        go.Heatmap(
            z=scaled_volcano,
            zmid=0,
            zmax=scaled_volcano.max(),
            zmin=scaled_volcano.min(),
        )
    ],
    layout=dict(title="Volcano heatmap - Divergent colorscale"),
)

del df_volcano
del scaled_volcano
del df_gap

layout = html.Div(
    [
        html.H3(["Plotly gallery"]),
        html.H4(["Points"]),
        utils.graph(scatter_gapminder),
        utils.graph(scatter_gapminder2),
        html.H4(["Line"]),
        utils.graph(line_gapminder),
        html.H4(["Bar"]),
        utils.graph(bar_gapminder),
        html.H4(["Histogram"]),
        utils.graph(histogram_gapminder),
        html.H4(["Boxplot"]),
        utils.graph(boxplot_gapminder),
        html.H4(["Heatmap"]),
        utils.two_graphs(utils.graph(heatmap_volcano), utils.graph(heatmap_volcano_2)),
        utils.markdown_content(
            "More plots can be found at [https://plot.ly/python/](https://plot.ly/python/)"
        ),
    ]
)
