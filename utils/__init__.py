"""Utils functions"""
from .components import (
    MarkdownReader,
    graph,
    markdown_content,
    table_from_csv,
    table_from_df,
    table_from_md,
    takeaways,
    two_graphs,
)

__version__ = "1.4.2"
__all__ = (
    "__version__",
    "graph",
    "MarkdownReader",
    "markdown_content",
    "table_from_csv",
    "table_from_df",
    "table_from_md",
    "takeaways",
    "translations",
    "two_graphs",
)

translations = {"eula": {"fr": "Mentions légales", "en": "Terms of Use"}}
