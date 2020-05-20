import dash_html_components as html


def button(text, size="medium", kind="default", disabled=False):

    class_name = f"{kind}-button button-{size}"

    return html.Button(
        text, disabled=disabled, className=class_name
    )
