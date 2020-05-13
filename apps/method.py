import dash_html_components as html

import utils

METHODO_TAK = "assets/Schema_methodo_TAK.svg"
LECTURE_SUNBURST = "assets/Schema_lecture_sunburst.svg"
LECTURE_TAK = "assets/Schema_lecture_TAK.svg"

with open("assets/contents/methods.md", "r", encoding="utf-8") as f:
    content = utils.MarkdownReader(f.read())

layout = html.Div(
    [
        content[0],
        utils.two_graphs(
            content[1],
            html.Figure(
                [
                    html.Img(
                        src=LECTURE_SUNBURST,
                        id="methodo_tak",
                        className="img-responsive p-centered",
                        style={"maxHeight": 500},
                    ),
                    html.Figcaption(
                        "Exemple de sunburst à 5 traitements.",
                        className="figure-caption text-center",
                    ),
                ],
                className="figure",
            ),
        ),
        content[2],
        utils.two_graphs(
            html.Figure(
                [
                    html.Img(
                        src=LECTURE_TAK,
                        id="methodo_tak",
                        className="img-responsive p-centered",
                        style={"maxHeight": 370},
                    ),
                    html.Figcaption(
                        "Exemple de TAK à 5 traitements.",
                        className="figure-caption text-center",
                    ),
                ],
                className="figure",
            ),
            content[3],
        ),
        content[4],
        html.Figure(
            [
                html.Img(
                    src=METHODO_TAK,
                    id="methodo_tak",
                    className="img-responsive p-centered",
                    style={"maxHeight": 600},
                ),
                html.Figcaption(
                    "Ci-dessus, le procédé simplifié pour obtenir un TAK : tous les patients "
                    "sont modélisés sous forme de vecteur temporel incluant leurs événements. "
                    "L'algorithme TAK trouve le meilleur ordonnancement pour faire émerger des "
                    "motifs temporels dans la prise en charge au niveau de la cohorte complète.",
                    className="figure-caption text-center",
                ),
            ],
            className="figure",
        ),
    ]
)
