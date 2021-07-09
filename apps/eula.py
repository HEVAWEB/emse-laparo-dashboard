import dash_html_components as html
import rgpd_dash

import utils
from app import config

SITE = "https://https://artemis-emse-laparo.hevaweb.com/"

with open("assets/eula/eula-fr.md", "r", encoding="utf-8") as f:
    content = utils.MarkdownReader(f.read().format(site=SITE))

with open("assets/eula/eula-fr-content.md", "r", encoding="utf-8") as f:
    sources = f.read()

layout = html.Div(
    [
        content[0],
        utils.markdown_content(sources),
        content[1],
        rgpd_dash.RgpdDash(
            variant="options",
            trackingCode=config.tracking_code,
            isDebug=config.debug,
            locale=config.language,
        ),
        content[2],
    ]
)
