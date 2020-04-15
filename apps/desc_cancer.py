import dash_html_components as html

import utils

layout = html.Div(
    [
        html.H3("Description des patients avec MTEV par cancer d'intérêt"),
        utils.markdown_content("Pas de contenu."),
    ]
)
