import dash_html_components as html
import utils

layout = html.Div(
    [
        html.H1("Les composants"),
        utils.toolbar([]),
        html.H3("Popin"),
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.Button("×", className="notifier-close"),
                                        html.P(
                                            html.Span(
                                                "Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
                                                "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
                                            )
                                        ),
                                    ],
                                    className="notifier-note",
                                )
                            ],
                            className="plotly-notifier",
                        ),
                    ],
                    className="col col-4",
                )
            ],
            className="columns",
        ),
        html.H3("Code"),
        utils.markdown_content(
            """
    ```
    import foo
    foo.bar()
    ```"""
        ),
    ]
)
