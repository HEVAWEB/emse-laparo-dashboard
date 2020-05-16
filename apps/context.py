import dash_html_components as html

import utils

# Load markdown text content
with open("assets/contents/md_context.md", "r", encoding="utf-8") as f:
    content = utils.MarkdownReader(f.read())

# Define the page's content
layout = html.Div([content[0], content[1]])
