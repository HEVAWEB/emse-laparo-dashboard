import dash_html_components as html


def button(
    text, size="medium", kind="default", disabled=False, left_icon=None, right_icon=None
):

    class_name = f"{kind}-button button-{size}"
    content = [html.Span(text)]

    if left_icon:
        content.insert(0, html.I(className=f"icon {left_icon}"))

    if right_icon:
        content.append(html.I(className=f"icon {right_icon}"))

    return html.Button(content, disabled=disabled, className=class_name)
