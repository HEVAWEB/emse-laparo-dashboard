import dash_html_components as html

import utils

# Load markdown text content
with open("assets/contents/md_context.md", "r", encoding="utf-8") as f:
    content = utils.MarkdownReader(f.read())

# Define the page's content
layout = html.Div(
    [
        content[0],
        html.Ul(
            [
                html.Li(
                    html.A(
                        html.Em("IEEE Xplore"),
                        href="https://ieeexplore.ieee.org/document/9186773",
                        target="_blank",
                    )
                ),
                html.Li(
                    html.A(
                        html.Em("ResearchGate"),
                        href="https://www.researchgate.net/publication/344127383_Automatic_and_Explainable_Labeling_of_Medical_Event_Logs_with_Autoencoding",
                        target="_blank",
                    )
                ),
            ]
        ),
        content[1],
    ]
)
