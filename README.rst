Dashboard Template
==================

.. contents:: Contents
    :depth: 3
    :backlinks: top

Getting Started
---------------

Requires **Python 3.7**

1. Create & activate a virtual environment

   1) Windows

    .. code-block:: bash

        python -m venv venv
        venv/Scripts/activate

   2) OSX

    .. code-block:: bash

        python3 -m venv venv
        source venv/bin/activate

2. Install dependencies

    .. code-block:: bash

        pip install -r requirements.txt

3. Run development server (Windows & Unix)

    .. code-block:: bash

        python index.py

4. **Optional** On Unix platforms, run production server with

    .. code-block:: bash

        gunicorn index:app.server

5. Exit virtual environment

    .. code-block:: bash

        deactivate

References
----------

- `Plotly Python <https://plot.ly/python/>`_
- `Plotly R <https://plot.ly/r/>`_
- `Dash Documentation <https://dash.plot.ly/>`_
- `Gunicorn <https://gunicorn.org/>`_
- `Markdown Syntax <https://commonmark.org/help/>`_

Instructions
------------

How to use this project
~~~~~~~~~~~~~~~~~~~~~~~

First of all, you need to fork this repository to your own organisation.
To do so, just click on the *Fork* button at the top of this projet homepage.
You should then rename your fork to a friendler name.
How about `client-study` ?

    Please note that your projet name should be url friendly: avoid using special characters.

To rename a GitLab project, go to **Settings** > **General** > **Advanced** > **Rename Repository**.
This will rename **both** the project name displayed and its URL.

You may now clone the project and add files & code to create your specific dashboard.

How to include text documents
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You could write all the text you need in Python using Dash's HTML components for structure, but an easier way is to include a **Markdown** file stored in ``assets/``.
An example is given in ``apps/context.py`` using ``assets/demo.md``.


See also `<https://dash.plot.ly/dash-core-components/markdown>`_.


How to create interactives graphs?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is a two-steps answer: use Plotly graphing library and add some Dash callbacks.

1. Plotly Graphing Libraries
............................

Two libraries are listed in the references: Plotly for Python & R.
A graph created with thoses libraries can be used in a Dash dashboard.
The tricky part is that we need to export such a graph from our secure environment to the web server where the Dash backend is running.
The consequence of this statement is that we need to precompute all graphs beforehand.

As for the export format, Plotly graphs can be safely serialised to **Json**, though it may be quite handy to use the **pickle** protocol for Python users to bundle several graphs together.
We will maybe feel the need to develop a script to ease the packaging of R-created graphs.

2. Dash Callbacks
.................

Plotly graphs already have some builtin interactivity like zooming or panning but we are looking for something a bit more ambitious such as updating a graph with menus, sliders, etc.
This is exactly what Dash was designed for.

Each interaction must be implemented as a Python function in its dedicated app (folder ``apps/``).
The idea is quite simple: each specific component has an unique *id* and some internal properties.
A Dash callback is simply a function defined around **inputs** and an **output** that will update the **output** component designated property.
This property can be:

- the entire graph
- the layout
- a stylistic element

An exemple is in ``index.py``.
A global layout is defined with a lateral menu and a content placeholder with:

.. code-block:: python

    app.layout = html.Div(
        [
            dcc.Location(id="url", refresh=False),
            html.Div(
                children=[
                    html.H1("Dashboard"),
                    html.Ul(
                        children=[
                            html.Li(dcc.Link("Context", href="/context")),
                            html.Li(dcc.Link("Outcome", href="/outcome")),
                            ...
                        ]
                    ),
                ],
                className="two columns",
            ),
            html.Div(id="page-content", className="ten columns"),
        ]
    )

Do you see how the layout is composed of a very basic HTML structure with div blocks, title and links?
An important element to notice is the `dcc.Location`, a particular Dash component which keeps track of the webpage URL with an unique id.

Next we have these lines:

.. code-block:: python

    @app.callback(Output("page-content", "children"), [Input("url", "pathname")])
    def display_page(pathname):
        if pathname == "/context" or pathname == "/":
            return context.layout
        elif pathname == "/outcome":
            return outcome.layout
        ...


Here is how a callback is defined. This one will update the ``children`` property of the ``page-content`` element based on the ``pathname`` property state for the ``url`` component which is as seen above the browser URL.
When the user navigate through the link in the menu, this will trigger this callback which will update the content of the website with the content of the corresponding app in ``apps/``.

Using the very same principles, this is how we can allow our user to interact with graphs using buttons, slider, dropdown menus, etc.

See also `<https://dash.plot.ly/getting-started-part-2>`_.

What file(s) do I need to modify to...
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Add/Remove a page?
..................

- Add/Remove the corresponding app in ``apps/``
- Add/Remove the assets used (images, ``.md`` files, etc.)
- In ``index.py``

  - Add/Remove the app import
  - Add/Remove the menu link
  - Add/Remove the callback condition

Include an asset?
.................

Assets are (but not limited to):

- images
- markdown files
- stylesheets
- javascript files


All assets except for graphs should be stored in the ``assets/`` folder.
You may access an asset in an app with the ``assets/<filename>`` path.
Please note that ``.css`` & ``.js`` files are automatically served by the Dash server.

Include graphs?
...............

Graphs should be stored in the ``builds/`` folder.
We separate them from standard assets because they can be quite heavy and we are still thinking how we should specifically handle them.
You may access a graph in an app with the ``builds/<filename>`` path.

Define a callback in an app?
............................

You may do exactly as in the **Dash Callbacks** section.
Just remember that you need to import the Dash global application with ``from app import app`` to access the callback decorator ``@app.callback()`` to decorate your function.

Share something across apps?
................................

Since all apps can access the ``app.py`` module namespace, if you need an asset in multiple apps (let us say a logo for instance), you can define it in ``app.py`` and import it in every app where it is needed.

How to deploy a dashboard
~~~~~~~~~~~~~~~~~~~~~~~~~

1. Ask the devs to create the `.hevaweb.com` subdomain (same as the project name on GitLab)
2. Change the default authentication credentials in `identifiants.csv`
3. Push your changes to GitLab
4. In **CI/CD** > **Pipelines**, wait for the job(s) to finish and then use the **Manual job** button on the right to deploy your dashboard.

Please note that you also follow the procedure described `here <https://gitlab.hevaweb.com/heva/docker-images>`_. Feel free to reach a dev for help.

How to update a fork with the latest developments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We may need to update the template with bug fixes, design improvements or just dependencies upgrades.
In order to benefit on your fork from these developments, you need to do the following procedure:

1. Add upstream remote to your git repository ``git remote add upstream https://gitlab.hevaweb.com/web/dashboard-template``. You can check that the upstream was properly added with ``git remote -v``
2. Fetch upstream latest developments ``git fetch upstream``
3. Merge upstream master on top of your current branch ``git merge upstream/master``
4. Resolve potential git conflict

You could do step **3.** on an isolated branch in order to deal with potentials conflicts without stress.

What if my question is not listed here?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Feel free to come to us! :)
- Take a look at the references above
