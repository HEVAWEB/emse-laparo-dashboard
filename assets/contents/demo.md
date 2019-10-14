Voyons ensemble comment créer du contenu pour un Dashboard Artémis 🏹.

Tout le contenu textuel d'un dashboard doit être écrit en [Markdown](https://commonmark.org/help/).
Le Markdown est un format de texte simple très utilisé sur le Web (Reddit, Slack, Discord, etc.).
Il permet de créer une mise en page sommaire à partir notamment de titres, liens et listes.

### Titres

Un titre commence par le caractère `#` suivi d'un espace puis du texte.
Le nombre de `#` successifs détermine le niveau de titre (de 1 à 6).

**Note**: nous conseillons d'utiliser les niveaux de titre de *3* à *5* dans Artémis, les niveaux 1 et 2 étant réservés pour d'autre éléments dans le design de l'outil.

Ainsi, pour créer un titre de niveau 4 :

```markdown
#### Définition de la population d'étude
```
apparait comme ceci sur la page actuelle :

#### Définition de la population d'étude

### Listes

Le Markdown permet de créer des listes ordonnées et non ordonnées assez facilement (et même imbriquées !):

```markdown
1. Premier élément ordonné
2. Second élément ordonné
    - Premier élément non ordonné
    - Second élément non ordonné
```

1. Premier élément ordonné
2. Second élément ordonné
    - Premier élément non ordonné
    - Second élément non ordonné

### Emphase et liens

Markdown possède deux niveaux d'emphase de texte.
```markdown
*emphase simple*
**emphase double**
```
Au lieu des traditionnels italique et gras, ici nous avons *l'emphase simple* et **l'emphase double**, pratique pour mettre des éléments en valeur !

Il est également possible d'insérer des liens externes :

```markdown
[Markdown](https://commonmark.org/help/)
```

apparait comme ceci : [Markdown](https://commonmark.org/help/).

### Tables

Nous commençons ici à attaquer les choses sérieuses.
Il est possible de définir une table en Markdown avec la syntaxe suivante :

```markdown
| Tables |  Are | Cool |
|----------|:-------------:|------:|
| col 1 is | left-aligned | $1600 |
| col 2 is | centered | $12 |
| col 3 is | *right-aligned* |**$1** |
```

| Tables |  Are | Cool |
|----------|:-------------:|------:|
| col 1 is | left-aligned | $1600 |
| col 2 is | centered | $12 |
| col 3 is | *right-aligned* |**$1** |

Avez-vous remarqué que nous avons choisi l'alignement des colonnes et ajouter de l'emphase sur des cellules ?

Notons également que nous fournissons un moyen simple d'intégrer un fichier `.csv` comme un graphe à partir du code Python :

```python
import utils

# À ajouter bien sûr au layout de la page
utils.table_from_csv("builds/iris.csv", "Un exemple de table")
```

[//]: # (section)

### Citations et conclusions

Une citation est insérée comme ceci :

```markdown
> Il ne faut pas croire tout ce qu'on lit sur Internet. Albert Einstein, 1928
```

> Il ne faut pas croire tout ce qu'on lit sur Internet. Albert Einstein, 1928

Nous avons également créé un composant de conclusion ou point-clé.
Il doit être appelé en Python comme ceci :

```python
import utils

# À ajouter bien sûr au layout de la page
utils.takeaways("Le Markdown c'est cool.")
```

[//]: # (section)

Il existe d'autres fonctionnalités disponibles en Markdown, mais celles que nous venons de décrire sont les plus importantes.

À noter cependant une dernière chose : nous avons mis en place un composant permettant de découper le contenu d'un fichier `.md` en plusieurs sections pour pouvoir intercaler des graphes et autres (à l'image de la table plus haut ou de la conclusion juste au-dessus) sans devoir découper le contenu textuel en plusieurs fichiers.

Il suffit de délimiter les sections avec `[//]: # (section)` (précédé et suivi d'une ligne vide), pour pouvoir utiliser le code suivant :

```python
import utils

with open("assets/contents/demo.md", "r", encoding="utf-8") as f:
    content = utils.MarkdownReader(f.read())


# À ajouter bien sûr au layout de la page
content[0]      # Première section du fichier
content[1]      # Seconde section du fichier
content.full()  # Fichier en entier
content[:]      # Fichier en entier
```

Le résultat est la page sur laquelle vous vous trouvez actuellement. 😀

### Les graphes

Écrire du texte c'est bien, mais je suis persuadé que ce qui vous intéresse ce sont les graphes interactifs !

Admettons ici que nous avons un graphe `simpleplot` sérialisé en `json` présent dans le dossier `builds`. Nous pouvons afficher ce graphe dans une page en utilisant la fonction suivante :

```python
import json # 1
import plotly.graph_objects as go
import utils


with open("builds/simpleplot.json", "r", encoding="utf-8") as f:
    figure = go.Figure(json.load(f))  # 2
    figure.update_layout(template="heva_theme")  # 3

# À ajouter bien sûr au layout de la page
utils.graph(figure)
```

[//]: # (section)

Voyons ensemble de quoi sont composées ces quelques lignes :

1. Nous rajoutons davantage d'imports. Pour charger un fichier `.json` nous avons besoin du module `json`. Pour modifier des graphes Plotly nous importons le module `plotly.graph_objects` que nous renommons en `go` par commodité.
2. Nous lisons comme précédemment le fichier, à la différence que nous devons le comprendre comme un fichier `json` et non un fichier texte. C'est pourquoi nous utilisons plus la méthode `f.read()`, mais `json.load(f)`. Enfin, nous créons une figure Plotly à partir de ce résultat.
3. À l'aide de cette ligne, nous modifions le thème du graphe pour utiliser celui de HEVA. Cela a notamment pour effet de changer les couleurs utilisées pour coller au mieux à la charte graphique HEVA.

Nous pouvons également mettre deux graphes côte à côte facilement avec :

```python
utils.two_graphs(
    utils.graph(figure),
    utils.graph(figure)
)
```

[//]: # (section)

Avec ces quelques exemples d'utilisation nous espérons avoir montré la simplicité d'utilisation d'Artémis.
Il reste de nombreuses choses à voir concernant l'interactivité des boutons mais cette page devrait donner un point de départ satisfaisant pour la rédaction de contenu textuel pour un dashboard.

**En bonus**, voici le code complet (finalement très court) utilisé pour avoir une page telle que celle-ci :

```python
import dash_html_components as html
import plotly.graph_objects as go

import utils

# Load markdown text content
with open("assets/contents/demo.md", "r", encoding="utf-8") as f:
    content = utils.MarkdownReader(f.read())

# Make the simple plot
simple_fig = go.Figure(
    data=[go.Scatter(x=[0, 1, 2, 3, 4], y=[2, 3, 4, 6, 1])],
    layout=dict(title="Un graphe simple"),
)

# Define the page's content
layout = html.Div(
    [
        content[0],
        utils.table_from_csv("builds/iris.csv"),
        content[1],
        utils.takeaways("Le Markdown c'est cool."),
        content[2],
        utils.graph(simple_fig),
        content[3],
        utils.two_graphs(utils.graph(simple_fig), utils.graph(simple_fig)),
        content[4]
    ]
)
```
