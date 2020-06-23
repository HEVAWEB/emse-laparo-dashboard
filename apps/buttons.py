import dash_core_components as dcc
import dash_html_components as html
from dash_table import DataTable

from utils.html import button

datatable = DataTable(
    columns=[
        {"name": ["", "Year"], "id": "year"},
        {"name": ["City", "Montreal"], "id": "montreal"},
        {"name": ["City", "Vancouver"], "id": "vancouver"},
        {"name": ["Climate", "Temperature"], "id": "temp"},
        {"name": ["Climate", "Humidity"], "id": "humidity"},
    ],
    data=[
        {
            "year": i,
            "montreal": i * 10,
            "vancouver": i * 5,
            "temp": "text",
            "humidity": i * -100,
        }
        for i in range(30)
    ],
    merge_duplicate_headers=True,
    export_format="csv",
    sort_action="native",
    style_cell_conditional=[{"if": {"column_id": "temp"}, "text-align": "left"}],
    page_action="native",
    page_size=10,
)

layout = html.Div(
    [
        html.H1("Les boutons"),
        html.H3("Default"),
        html.H4("Large"),
        button("Default", size="large"),
        button("Disabled", size="large", disabled=True),
        html.Br(),
        button(
            "Default", size="large", right_icon="icon-arrow-down", left_icon="icon-time"
        ),
        button(
            "Disabled",
            size="large",
            disabled=True,
            right_icon="icon-arrow-down",
            left_icon="icon-time",
        ),
        html.H4("Medium"),
        button("Default"),
        button("Disabled", disabled=True),
        html.Br(),
        button("Default", right_icon="icon-arrow-down", left_icon="icon-time"),
        button(
            "Disabled",
            disabled=True,
            right_icon="icon-arrow-down",
            left_icon="icon-time",
        ),
        html.H4("Small"),
        button("Default", size="small"),
        button("Disabled", size="small", disabled=True),
        html.Br(),
        button(
            "Default", size="small", right_icon="icon-arrow-down", left_icon="icon-time"
        ),
        button(
            "Disabled",
            size="small",
            disabled=True,
            right_icon="icon-arrow-down",
            left_icon="icon-time",
        ),
        html.Hr(),
        html.H3("Secondary"),
        html.H4("Large"),
        button("Default", kind="secondary", size="large"),
        button("Disabled", kind="secondary", size="large", disabled=True),
        html.Br(),
        button(
            "Default",
            kind="secondary",
            size="large",
            right_icon="icon-arrow-down",
            left_icon="icon-time",
        ),
        button(
            "Disabled",
            kind="secondary",
            size="large",
            disabled=True,
            right_icon="icon-arrow-down",
            left_icon="icon-time",
        ),
        html.H4("Medium"),
        button("Default", kind="secondary"),
        button("Disabled", kind="secondary", disabled=True),
        html.Br(),
        button(
            "Default",
            kind="secondary",
            right_icon="icon-arrow-down",
            left_icon="icon-time",
        ),
        button(
            "Disabled",
            kind="secondary",
            disabled=True,
            right_icon="icon-arrow-down",
            left_icon="icon-time",
        ),
        html.H4("Small"),
        button("Default", kind="secondary", size="small"),
        button("Disabled", kind="secondary", size="small", disabled=True),
        html.Br(),
        button(
            "Default",
            kind="secondary",
            size="small",
            right_icon="icon-arrow-down",
            left_icon="icon-time",
        ),
        button(
            "Disabled",
            kind="secondary",
            size="small",
            disabled=True,
            right_icon="icon-arrow-down",
            left_icon="icon-time",
        ),
        html.Hr(),
        html.H3("Links"),
        button("Default", kind="link", size="medium"),
        button("Disabled", kind="link", size="medium", disabled=True),
        html.Br(),
        button(
            "Default",
            kind="link",
            size="medium",
            right_icon="icon-arrow-down",
            left_icon="icon-time",
        ),
        button(
            "Disabled",
            kind="link",
            size="medium",
            disabled=True,
            right_icon="icon-arrow-down",
            left_icon="icon-time",
        ),
        html.Hr(),
        html.H3("Button group"),
        html.H4("Large"),
        html.Div(
            [
                button("Default", size="large"),
                button("Default", size="large"),
                button("Default", size="large"),
            ],
            className="btn-group btn-group-block",
        ),
        html.H4("Medium"),
        html.Div(
            [button("Default"), button("Default"), button("Default")],
            className="btn-group btn-group-block",
        ),
        html.H4("Small"),
        html.Div(
            [
                button("Default", size="small"),
                button("Default", size="small"),
                button("Default", size="small"),
            ],
            className="btn-group btn-group-block",
        ),
        html.H4("Secondary"),
        html.Div(
            [
                button("Default", kind="secondary"),
                button("Default", kind="secondary"),
                button("Default", kind="secondary"),
            ],
            className="btn-group btn-group-block",
        ),
        html.Hr(),
        html.H4("Tabs"),
        dcc.Tabs(
            id="tabs",
            value="tab-1",
            children=[
                dcc.Tab(label="Default", value="tab-1",),
                dcc.Tab(label="Second option", value="tab-2",),
                dcc.Tab(label="Third option", value="tab-3",),
                dcc.Tab(label="Disabled tab", value="tab-4", disabled=True,),
            ],
            parent_className="custom-tabs",
            className="custom-tabs-container",
        ),
        html.Hr(),
        html.H4("Pagination"),
        datatable,
        html.H4("Accordion"),
        html.Details(
            [
                html.Summary(
                    [html.I(className="icon icon-arrow-right"), html.Span("Value"),],
                    className="accordion-header",
                ),
                html.Div(
                    [html.I(className="icon icon-arrow-right"), html.Span("Element")],
                    className="accordion-body",
                ),
            ],
            className="accordion",
        ),
        html.Details(
            [
                html.Summary([html.Span("Value")], className="accordion-header",),
                html.Div([html.Span("Element")], className="accordion-body",),
            ],
            className="accordion",
        ),
        html.Hr(),
    ]
)
