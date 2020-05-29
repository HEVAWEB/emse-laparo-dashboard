import dash_html_components as html
import utils

layout = html.Div([
    html.H1("Les composants"),
    utils.toolbar([]),
    html.H3("Code"),
    utils.markdown_content("""
    ```
    import foo
    foo.bar()
    ```""")

])
