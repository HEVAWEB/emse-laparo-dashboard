# Artemis reference

## Contents
1. [Contents](#contents)
2. [References](#references)
3. [Getting Started : how to create a dashboard?](#getting-started--how-to-create-a-dashboard)
   1. [Create your project on Gitlab](#create-your-project-on-gitlab)
      1. [New repository](#new-repository)
      2. [**Option 1**: Command line](#option-1-command-line)
      3. [**Option 2** : Sourcetree](#option-2--sourcetree)
   2. [Tame your Python 🐍](#tame-your-python-)
   3. [Compile stylesheet to correctly render the dashboard](#compile-stylesheet-to-correctly-render-the-dashboard)
4. [Instructions](#instructions)
   1. [Where to start with ARTEMIS?](#where-to-start-with-artemis)
   2. [How to include text documents in the dashboard?](#how-to-include-text-documents-in-the-dashboard)
   3. [How to create interactives graphs?](#how-to-create-interactives-graphs)
      1. [1. Plotly Graphing Libraries](#1-plotly-graphing-libraries)
      2. [2. Dash Callbacks](#2-dash-callbacks)
      3. [3. Export graphs](#3-export-graphs)
   4. [What file(s) do I need to modify to\...](#what-files-do-i-need-to-modify-to)
      1. [Add/Remove a page?](#addremove-a-page)
      2. [Include an asset?](#include-an-asset)
      3. [Include graphs?](#include-graphs)
      4. [Define a callback in an app?](#define-a-callback-in-an-app)
      5. [Share something across apps?](#share-something-across-apps)
   5. [How to deploy a dashboard](#how-to-deploy-a-dashboard)
   6. [How to update your dashboard with the template\'s latest developments](#how-to-update-your-dashboard-with-the-templates-latest-developments)
   7. [How to update the template with something from your dashboard](#how-to-update-the-template-with-something-from-your-dashboard)
   8. [What if my question is not listed here?](#what-if-my-question-is-not-listed-here)

## References

-   [Plotly Python](https://plotly.com/python/)
-   [Dash Documentation](https://plotly.com/dash/)
-   [Gunicorn](https://gunicorn.org/)
-   [Markdown Syntax](https://commonmark.org/help/)

## Getting Started : how to create a dashboard?

### Create your project on Gitlab

First of all, create a copy of this Git repository ("web/dashboard-template") in your own GitLab group (ex.: in "Data Science").
You shall follow the steps below to do so.

#### New repository

Create a new **empty** GitLab repository in the correct group/subgroup (from the internet interface of GitLab).

**Warning**: do not select the box **Initialize repository with a README**.
The template's README file contains a checklist you should keep.

> You should choose a friendly name: how about
> **client-study-dashboard**?

Note: once created, your new repository has an URL, most likely: `https://gitlab.hevaweb.com/data_science/client-study-dashboard`.
This is another reason to follow the naming convention above.


#### **Option 1**: Command line

Create a local copy of the template repository with the following command lines:

1. Choose a directory on your computer, this is where your dashboard will be stored (ex: `C:\Users\MPRODEL\Documents\Missions`).

2. `git clone -o upstream https://gitlab.hevaweb.com/web/dashboard-template <your friendly name>` with `<your friendly name>` being **client-study-dashboard**
    for example.
3.  `cd <your friendly name>`
4.  `git remote add origin <your new gitlab repo url>` with the
    URL we got from step **1** (most likely: https://gitlab.hevaweb.com/data_science/client-study-dashboard)
5.  `git push -u origin master`

🎉 Tada! You are good to go.
We needed those steps to be able to update your dashboard and the template from one to another.

> **Please note that the steps above are for creating a dashboard.**

If you want to clone an existing dashboard (already on GitLab), you should do these steps instead:

1.  `git clone <your url>`
2.  `cd <your dashboard>`
3.  **Optional**: `git remote add upstream https://gitlab.hevaweb.com/web/dashboard-template`

#### **Option 2** : Sourcetree

1. Clone the template with Sourcetree
    - Use the template URL
    - Give it the name you want (the friendly name for coherence)
    - Choose the correct path on your file system

2. Create the **upstream** remote
    - **Settings** (top right) > **Remote** tab
    - Select `origin` (it should have the template URL) > **Edit**
    - Uncheck **Default remote**
    - Replace `origin` with `upstream`

3. Create the **origin** remote
    - **Settings** (top right) > **Remote** tab > **Add**
    - Name: `origin`, check **Default remote**, URL: your GitLab project URL from step 1
    -Validate

4. Push the content to `origin`


🎉 Tada! You are good to go. We needed those steps to be able to update your dashboard and the template from one to another.

> **Please note that the steps above are for creating a dashboard.**

If you want to clone an existing dashboard (already on GitLab), you should do these steps instead:

1. Clone the template with Sourcetree
    - Use the template URL
    - Choose the correct path on your file system

2. **Optional**: create the **upstream** remote
    - **Settings** (top right) > **Remote** tab > **Add**
    - Name: `upstream`, **do not check Default remote**, URL: the dashboard template URL on GitLab
    -Validate

### Tame your Python 🐍

1.  Get your Python settings up-to-date 💻

    Requires **Python 3.7**. For the following steps, you must go in the local directory in which you synchronised your project (ex: with SourceTree).

    1.  Create & activate a virtual environment (very important if you currently have several Python projects on your computer)

        1)  Windows (with Windows -\> \'cmd\')

            ```bash
            python -m venv venv
            venv\Scripts\activate
            ```

        2)  OSX

            ```bash
            python3 -m venv venv
            source venv/bin/activate
            ```

    2.  Compile & install Python dependencies (all the required packages)
        1. Install pip-tools in your venv (which installs pip-compile command)
        ```
        pip install pip-tools
        ```
        2. Compile the `requirements.txt` which suits your needs
        ```bash
        pip-compile reqs/base.in -o requirements.txt --no-emit-index-url --upgrade
        ```
        You can add layers to the the final `requirements.txt` file to add curated libraries.
        The `reqs/base.in` file contains the minimum needed for a dashboard.
        You may add functionnalities to your dashboard in your virtual environment by adding files from the `reqs` folder.
        Let us say for example that you want to create a dashboard with maps.
        Your `requirements.txt` should be generated with:
        ```
        pip-compile reqs/base.in reqs/maps.in -o requirements.txt --no-emit-index-url --upgrade
        ```
        > It is encouraged during development to add the `reqs/dev.in` layer

        ```
        pip-compile reqs/base.in reqs/dev.in -o requirements-dev.txt --no-emit-index-url --upgrade
        ```

        3. Finally, install the dependencies in the virtual environment with pip:
        ```
        pip-sync
        ```
        or
        ```
        pip-sync requirements-dev.txt
        ```

    3.  Run a development server (Windows & Unix)

        * Go into your work directory (where your dashboard is)
        * Open a Windows cmd invite (tip: just write 'cmd' in the path at the top of the screen)
        * Type:

        ```bash
        python index.py
        ```

        > You may also use the utility script provided `launch_artemis.bat` if you are not using a virtual environment.

        * By default, you can now open your ugly (for now!) dashboard at [http://127.0.0.1:8050/](http://127.0.0.1:8050/)
        * Warning: do not close your Windows invite, otherwise it closes the dashboard.

    4.  **Optional** On Unix platforms, run production server with

        ```bash
        gunicorn index:app.server
        ```

    5.  Exit virtual environment (whenever you stop working on this project)

        ```bash
        deactivate
        ```

### Compile stylesheet to correctly render the dashboard

1. Install latest LTS Node.js version https://nodejs.org/ and make sure `npm` is added to the system PATH
2. **Optional**: you may install the yarn package manager for quicker install with `npm install -g yarn`
3. For each dashboard you should do the following steps at least once:
    1. Open a terminal in root folder install stylus with `npm install` or `yarn`
    2. Compile the final .css file with `npm run build` or `yarn build`. Please be aware that this command should be runned every time you change a `.styl` file.
    3. **Optional**: for long coding sprints on style, it could be handier to use the watcher with `yarn watch:stylus` or `npm run watch:stylus`.

## Instructions

### Where to start with ARTEMIS?

In the root directory of any Artemis project you should see a bunch of files and sub-directories.
Here are the ones you should know about:

- The directory `apps`: define the pages' content, layout, intreactivity of the dashboard
- The directory `assets`: text contents, images, fonts, etc.
- The directory `builds`: Plotly graphs
- The file `index.py`: general info (name, menu)

### How to include text documents in the dashboard?

The easy way is to include a **markdown** file in `assets/contents/`.
This template gives an example in `assets/contents/demo.md`.
Then, the Python file `apps/context.py` loads and adds this file.

See also <https://dash.plotly.com/dash-core-components/markdown>.

Note: instead of using Markdown, you could write all the text you need in Python using Dash's HTML components for structure (**not recommended**).

### How to create interactives graphs?

This is a two-step answer: (1) use Plotly graphing library and (2) add some Dash callbacks (to make interactive graphs :green_heart:).

#### 1. Plotly Graphing Libraries

The reference to discover Plotly examples in Python is [here](https://plotly.com/python/).
A graph created with thoses libraries can be used in a Dash dashboard.
The tricky part to get a nice Plotly graph in your online dashboard is to create it **in the bubble**, export it on your computer with Filezilla, and then put it on the server (you should never export the raw data from the bubble and then create a graph).
This is important because Dash is designed to serve the data online and then to generate the graph on-the fly.
**The consequence is the need to precompute all graphs before leaving the bubble**.

As for the export format, Plotly graphs can be safely serialised to **Json**, though it may be quite handy to use the **pickle** protocol for Python users to bundle several graphs together.

#### 2. Dash Callbacks

Plotly graphs already have some builtin interactivity like "zooming" or "panning", but we are too ambitious to settle for this 🚀.
We want to update a graph with menus, sliders, add sunbursts, etc.
This is exactly what Dash was designed for.

Each interaction must be implemented as a Python function in its dedicated app (folder `apps/`).
Here is the idea: each specific component has an unique *id* and some internal properties.
A Dash callback is simply a function defined around **inputs** and an **output**, that will update the **output** component designated property.
This property can be:

-   the entire graph
-   the layout
-   a stylistic element

Here is a simple example of a layout with a lateral menu and a content placeholder with:

```python
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app

layout = html.Div(
    [
        dcc.Location(id="url", refresh=False),
        html.Div(
            [
               # Content
            ],
            className="columns col-gapless",
        ),
    ]
)

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/context" or pathname == "/":
        return html.H1("first page")
    elif pathname == "/outcome":
        return html.H1("second page")
```

Do you see how the `layout` is a very basic HTML structure?
An important element to notice here is the `dcc.Location`, a particular Dash component which keeps track of the webpage URL with its unique id `"url"`.

Next we have the lines in the same file beggining with `@app.callback`: here is how to define a callback.
This one will update the `children` property of the `page-content` element based on the `pathname` property state for the `url` component which is as seen above the browser URL.
When the user navigate through the link in the menu, this will trigger this callback which will update the content of the website with the content of the corresponding app in `apps/`.
The actual application object `app` is instanciated in the `app.py` file, but you do not need to give it any tought beside importing it.

Using the very same principles, this is how we can allow our user to interact with graphs using buttons, slider, dropdown menus, etc.

See also <https://dash.plotly.com/getting-started-part-2>.

#### 3. Export graphs

The prefered export format for graphs is **json**, although Python users may use pickled graphs if they want.

1.  Python export

At some point, you shoud have a Plotly figure with something like this:

```python
import plotly.graph_objects as go

# we create data & layout here

fig = go.Figure(data, layout)
```

You may export this figure to a **json** file using the following snippet:

```python
with open("<output-path>", "w", encoding="utf-8") as f:
    # prefered way
    fig.write_json(f)
```

2.  Graph layout

**Please note that your Plotly graphs should have the bare minimum layout!**

The dashboard has a built-in HEVA theme to apply to every graph.
Try to specify only titles and readability elements, not colors & fonts for example.

### What file(s) do I need to modify to\...

#### Add/Remove a page?

-   Add/Remove the corresponding app in `apps/`
-   Add/Remove the assets used (images, `.md` files, etc.)
-   In `index.py`
    -   Add/Remove the app import
    -   Add/Remove the menu link in the two relevant dictionaries

#### Include an asset?

Assets are (but not limited to):

-   images
-   markdown files
-   stylesheets
-   javascript files

All assets except for graphs should be stored in the `assets/` folder.
You may access an asset in an app with the `assets/<filename>` path.
Please note that the Dash server automatically serves `.css`, `.ico` & `.js` files.

#### Include graphs?

Graphs & data to generate them on-the-fly should be stored in the `builds/` folder.
We separate them from standard assets because they can be quite heavy.
You may access a graph in an app with the `builds/<filename>` path.

We usually store graphs using **json** or **pickle** formats.

1.  Json

```python
import json
import plotly.graph_objects as go

with open("<path to your file>", "r", encoding="utf-8") as f:
    graph = go.Figure(json.load(f))
    graph.update_layout(template="heva_theme")
```

2.  Pickle

```python
import pickle
import plotly.graph_objects as go

with open("<path to your file>", "rb") as f:
    graph = go.Figure(pickle.load(f))
    graph.update_layout(template="heva_theme")
```

A few words on the codes above, we build a new Plotly figure with
`go.Figure()` on the loaded figure: it allows us to easily interact with the figure.
For example here we override the layout with HEVA's theme.
This is why graphs in the dashboard may look different from the ones you exported earlier.
However, the internal validations done by the `Figure` class can be really slow with heavy plots.
If speed is an issue, you should keep your graph as Python dicts (but apply the HEVA theme nonetheless).

#### Define a callback in an app?

You may do exactly as in the **Dash Callbacks** section.
Just remember that you need to import the Dash global application with `from app import app` to access the callback decorator `@app.callback()` to decorate your function.

#### Share something across apps?

Since all apps can access the `app.py` module namespace, if you need an asset in multiple apps (let us say a logo for instance), you can define it in `app.py` or **even better, in a third file in the `apps/` folder** and import it in every layout where it is needed.

### How to deploy a dashboard

1.  Change the default authentication credentials in `identifiants.csv`
2.  Push your changes to GitLab
3.  Enable the `deployer_heva_dashboard` key (Git -> Settings -> Repository -> Deploys keys)
4.  In **CI/CD** > **Pipelines**, wait for the job(s) to finish and then use the **Manual job** button on the right to deploy your dashboard.

Feel free to reach a dev for help.

### How to update your dashboard with the template\'s latest developments

We may need to update the template with bug fixes, design improvements or just dependencies upgrades.
In order to benefit on your dashboard from these developments, you need to do the following procedure:

1. If not done already, add upstream remote to your git repository `git remote add upstream https://gitlab.hevaweb.com/web/dashboard-template`. You can check that the upstream was properly added with `git remote -v`
1.  Fetch upstream latest developments `git fetch upstream`
2.  Merge upstream master on top of your current branch
    `git merge upstream/master`
3.  Resolve potential git conflicts

You could do step **3.** on an isolated branch in order to deal with potentials conflicts without stress.

### How to update the template with something from your dashboard

When working on your own dashboard, you could code something the template may benefit from (such as a bug fix, an ui improvement, etc.).

You can create a Merge Request on GitLab from your dashboard to the template with the following steps:

1. If not done already, add upstream remote to your git repository `git remote add upstream https://gitlab.hevaweb.com/web/dashboard-template`.
2. You can check that the upstream was properly added with `git remote -v`
3.  Fetch upstream latest developments `git fetch upstream`
4.  Create a new local branch from upstream with
    `git checkout -b <new-branch-name> upstream/master`
5.  Squash your modifications on top of your current new branch
    `git merge --squash <branch_with_modifications>`
6.  Resolve potential git conflicts & **remove all code/graphs/whatever related to your study**. You do not want to merge your graphs into
    the template!
7.  `git push --set-upstream origin <new-branch-name>`
8.  Go to <https://gitlab.hevaweb.com/web/dashboard-template> and open a
    Merge Request. Thank you kindly for your contribution!

### What if my question is not listed here?

-   Feel free to come to us! :)
-   Take a look at the references above
