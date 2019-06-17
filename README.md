# Artemis

✨🏹✨

## Contents

- [Contents](#contents)
- [References](#references)
- [Getting Started : how to create a dashboard ?](#getting-started--how-to-create-a-dashboard-)
  - [Create your project on Gitlab](#create-your-project-on-gitlab)
  - [Prepare your Python 🐍](#prepare-your-python-)
- [Instructions](#instructions)
  - [How to include text documents in the dashboard](#how-to-include-text-documents-in-the-dashboard)
  - [How to create interactives graphs?](#how-to-create-interactives-graphs)
    - [1. Plotly Graphing Libraries](#1-plotly-graphing-libraries)
    - [2. Dash Callbacks](#2-dash-callbacks)
    - [3. Export graphs](#3-export-graphs)
  - [What file(s) do I need to modify to\...](#what-files-do-i-need-to-modify-to)
    - [Add/Remove a page?](#addremove-a-page)
    - [Include an asset?](#include-an-asset)
    - [Include graphs?](#include-graphs)
    - [Define a callback in an app?](#define-a-callback-in-an-app)
    - [Share something across apps?](#share-something-across-apps)
  - [How to deploy a dashboard](#how-to-deploy-a-dashboard)
  - [How to update your dashboard with the template\'s latest developments](#how-to-update-your-dashboard-with-the-templates-latest-developments)
  - [How to update the template with something from your dashboard](#how-to-update-the-template-with-something-from-your-dashboard)
  - [What if my question is not listed here?](#what-if-my-question-is-not-listed-here)

## References

-   [Plotly Python](https://plot.ly/python/)
-   [Dash Documentation](https://dash.plot.ly/)
-   [Gunicorn](https://gunicorn.org/)
-   [Markdown Syntax](https://commonmark.org/help/)

## Getting Started : how to create a dashboard ?


### Create your project on Gitlab

First of all, create a copy of this Git repository (in "Web") in your own GitLab group (ex.: in "Data Science").
It is mandatory since forking is not an option because of GitLab's limitations (unfortunately).
To do so:

1.  Create a new **empty** GitLab repository in the correct
    group/subgroup.

    > You should choose a friendly name: how about
    > **client-study-dashboard**?

2.  Create a local copy of the template repository with the following
    command lines:

    1.  `git clone -o upstream https://gitlab.hevaweb.com/web/dashboard-template <your friendly name>` with `<your friendly name>` being **client-study-dashboard**
        for example.
    2.  `cd <your friendly name>`
    3.  `git remote add origin <your new gitlab repo url>` with the
        URL we got from step **1.**
    4.  `git push -u origin master`

    🎉 Tada! You are good to go. We needed those steps to be able to
    update your dashboard and the template from one to another.

    > **Please note that the steps above are for creating a dashboard.**

    If you want to clone an existing dashboard (already on GitLab),
    you should do these steps instead:

    1.  `git clone <your url>`
    2.  `cd <your dashboard>`
    3.  `git remote add upstream https://gitlab.hevaweb.com/web/dashboard-template`

### Prepare your Python 🐍

1.  Get your Python settings up-to-date 💻

    Requires **Python 3.7**. For the following steps, you must go in the
    local directory in which you synchronised your project (ex: with SourceTree).

    1.  **Optional**: Create & activate a virtual environment (very
        important if you currently have several Python projects on your
        computer)

        1)  Windows (with Windows -\> \'cmd\')

            ```bash
            python -m venv venv
            venv/Scripts/activate
            ```

        2)  OSX

            ```bash
            python3 -m venv venv
            source venv/bin/activate
            ```

    2.  Install Python dependencies (all the required packages)

        ```bash
        pip install -r requirements.txt
        ```

    3.  Run a development server (Windows & Unix)

        ```bash
        python index.py
        ```

    4.  **Optional** On Unix platforms, run production server with

        ```bash
        gunicorn index:app.server
        ```

    5.  Exit virtual environment (whenever you stop working on this project)

        ```bash
        deactivate
        ```

## Instructions

### How to include text documents in the dashboard

The easy way is to include a **Markdown**
file stored in `assets/` (or `assets/contents/`). An example is given in
`apps/context.py` using `assets/contents/demo.md`. You could write all
the text you need in Python using Dash\'s HTML components for structure.

See also <https://dash.plot.ly/dash-core-components/markdown>.

### How to create interactives graphs?

This is a two-steps answer: (1) use Plotly graphing library and (2) add some
Dash callbacks.

#### 1. Plotly Graphing Libraries

The reference to discover Plotly examples in Python is [here](https://plot.ly/python/).
A graph created with thoses libraries can be used in a Dash dashboard.
The tricky part to get a nice Plotly graph in your online dashboard is to create it **in the bubble**, and then to export it on your computer with Filezila, and then you put it on the server (please never export the data from the bubble and then create a graph). This is important because Dash is designed to put the data online and then to generate the graph.
**The consequence is the need to precompute all graphs before leaving the bubble**.

As for the export format, Plotly graphs can be safely serialised to **Json**, though it may be quite handy to use the **pickle** protocol for Python users to bundle several graphs together.

#### 2. Dash Callbacks

Plotly graphs already have some builtin interactivity like "zooming" or "panning", but we are more ambitious than these 🚀. We want to update a graph with menus, sliders, add sunbursts, etc.
This is exactly what Dash was designed for.

Each interaction must be implemented as a Python function in its dedicated app (folder `apps/`).
Here is the idea: each specific component has an unique *id* and some internal properties.
A Dash callback is simply a function defined around **inputs** and an **output** that will update the **output** component designated property.
This property can be:

-   the entire graph
-   the layout
-   a stylistic element

An exemple is in `index.py`.
A global layout is defined with a lateral menu and a content placeholder with:

```python
app.layout = html.Div(
    [
        dcc.Location(id="url", refresh=False),
        html.Div(
            [
               # Content
            ],
            className="columns col-gapless",
        ),
        html.Footer([f"{__version__}"]),
    ]
)
```

Do you see how the layout is composed of a very basic HTML structure?
An important element to notice is the `dcc.Location`, a particular Dash component which keeps
track of the webpage URL with an unique id.

Next we have these lines:

```python
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/context" or pathname == "/":
        return context.layout
    elif pathname == "/outcome":
        return outcome.layout
    ...
```

Here is how a callback is defined. This one will update the `children`
property of the `page-content` element based on the `pathname` property
state for the `url` component which is as seen above the browser URL.
When the user navigate through the link in the menu, this will trigger
this callback which will update the content of the website with the
content of the corresponding app in `apps/`.

Using the very same principles, this is how we can allow our user to
interact with graphs using buttons, slider, dropdown menus, etc.

See also <https://dash.plot.ly/getting-started-part-2>.

#### 3. Export graphs

The prefered export format for graphs is **json**, although Python users may use pickled graphs if they want.

1.  Python export

At some point, you shoud have a Plotly figure with something like this:

```python
fig = go.Figure(data, layout)
```

You may export this figure to a **json** file using the following
snippet:

```python
import json
from homemade.utils import NumpyEncoder

with open("<output-path>", "w", encoding="utf-8") as f:
    json.dump(fig.to_dict(), f, cls=NumpyEncoder)
```

2.  Graph layout

**Please note that your Plotly graphs should have the bare minimum
layout!**

The dashboard has a built-in HEVA theme to apply to every graph. Try to
specify only titles and readability elements, not colors & fonts for
example.

### What file(s) do I need to modify to\...

#### Add/Remove a page?

-   Add/Remove the corresponding app in `apps/`
-   Add/Remove the assets used (images, `.md` files, etc.)
-   In `index.py`
    -   Add/Remove the app import
    -   Add/Remove the menu link
    -   Add/Remove the callback condition

#### Include an asset?

Assets are (but not limited to):

-   images
-   markdown files
-   stylesheets
-   javascript files

All assets except for graphs should be stored in the `assets/` folder.
You may access an asset in an app with the `assets/<filename>` path.
Please note that `.css`, `.ico` & `.js` files are automatically served
by the Dash server.

#### Include graphs?

Graphs should be stored in the `builds/` folder. We separate them from
standard assets because they can be quite heavy and we are still
thinking if we should specifically handle them. You may access a graph
in an app with the `builds/<filename>` path.

Graphs are typically stored using **json** or **pickle** formats.

1.  Json

```python
import json
import plotly.graph_objs as go

with open("<path to your file>", "r", encoding="utf-8") as f:
    graph = go.Figure(json.load(f))
```

2.  Pickle

```python
import pickle
import plotly.graph_objs as go

with open("<path to your file>", "rb") as f:
    graph = go.Figure(pickle.load(f))
```

A few words on the codes above, we build a new Plotly figure with
`go.Figure()` on the loaded figure for a good reason: it allows us to
override the layout with the HEVA theme. This is why graphs in the
dashboard look different from the ones you exported earlier.

#### Define a callback in an app?

You may do exactly as in the **Dash Callbacks** section. Just remember
that you need to import the Dash global application with
`from app import app` to access the callback decorator `@app.callback()`
to decorate your function.

#### Share something across apps?

Since all apps can access the `app.py` module namespace, if you need an
asset in multiple apps (let us say a logo for instance), you can define
it in `app.py` and import it in every app where it is needed.

### How to deploy a dashboard

1.  Ask a developper to create the [.hevaweb.com]{.title-ref} subdomain
    (same as the project name on GitLab)
2.  Change the default authentication credentials in
    [identifiants.csv]{.title-ref}
3.  Push your changes to GitLab
4.  In **CI/CD** \> **Pipelines**, wait for the job(s) to finish and
    then use the **Manual job** button on the right to deploy your
    dashboard.

Please note that you also follow the procedure described
[here](https://gitlab.hevaweb.com/heva/docker-images). Feel free to
reach a dev for help.

### How to update your dashboard with the template\'s latest developments

We may need to update the template with bug fixes, design improvements
or just dependencies upgrades. In order to benefit on your dashboard
from these developments, you need to do the following procedure:

1\. If not done already, add upstream remote to your git repository
`git remote add upstream https://gitlab.hevaweb.com/web/dashboard-template`.
You can check that the upstream was properly added with `git remote -v`

2.  Fetch upstream latest developments `git fetch upstream`
3.  Merge upstream master on top of your current branch
    `git merge upstream/master`
4.  Resolve potential git conflicts

You could do step **3.** on an isolated branch in order to deal with
potentials conflicts without stress.

### How to update the template with something from your dashboard

When working on your own dashboard, you could code something the
template may benefit from (such as a bug fix, an ui improvement, etc.).

You can create a Merge Request on GitLab from your dashboard to the
template with the following steps:

1. If not done already, add upstream remote to your git repository
`git remote add upstream https://gitlab.hevaweb.com/web/dashboard-template`. You can check that the upstream was properly added with `git remote -v`

2.  Fetch upstream latest developments `git fetch upstream`
3.  Create a new local branch from upstream with
    `git checkout -b <new-branch-name> upstream/master`
4.  Squash your modifications on top of your current new branch
    `git merge --squash <branch_with_modifications>`
5.  Resolve potential git conflicts & **remove all code/graphs/whatever
    related to your study**. You do not want to merge your graphs into
    the template!
6.  `git push --set-upstream origin <new-branch-name>`
7.  Go to <https://gitlab.hevaweb.com/web/dashboard-template> and open a
    Merge Request. Thank you kindly for your contribution!

### What if my question is not listed here?

-   Feel free to come to us! :)
-   Take a look at the references above
