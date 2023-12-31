"""Utils functions"""


from . import html
from .components import (
    MarkdownReader,
    graph,
    markdown_content,
    table_from_csv,
    table_from_df,
    table_from_md,
    takeaways,
    toolbar,
    two_graphs,
)

__version__ = "1.6.0-dev"
__all__ = (
    "__version__",
    "graph",
    "MarkdownReader",
    "markdown_content",
    "table_from_csv",
    "table_from_df",
    "table_from_md",
    "takeaways",
    "toolbar",
    "translations",
    "two_graphs",
    "html",
)

translations = {"eula": {"fr": "Mentions légales", "en": "Terms of Use"}}
