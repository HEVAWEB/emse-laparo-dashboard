import dash_html_components as html

import utils

SITE = "https://dashboard-template.hevaweb.com"

with open("assets/eula/eula-fr.md", "r", encoding="utf-8") as f:
    content = utils.MarkdownReader(f.read().format(site=SITE))

with open("assets/eula/eula-fr-content.md", "r", encoding="utf-8") as f:
    sources = f.read()

layout = html.Div([content[0], utils.markdown_content(sources), content[1]])