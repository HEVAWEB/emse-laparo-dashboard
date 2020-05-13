### Méthodologie

#### Sélection de la population d'étude

**Critères d'inclusion :**

La population d'étude regroupe les patients avec au moins un séjour avec un Diagnostic Principal (DP) ou Diagnostic Relié (DR) correspondant à un cancer d’intérêt :
- Poumon
- Sein
- Digestif haut
- Digestif bas
- Prostate
- Pancréas
- Urothélial
- Myélome
- Mélanome
- Glioblastome
- Gynécologique
- ORL
- Testicule
- Lymphome

Dans le cas de patients ayant deux diagnostics pour des cancers différents pendant l’année d’inclusion, ils seront classés dans le groupe du cancer le plus récent.

**Critères d’exclusion :**
- Patients âgés de moins de 18 ans

**Codes d'inclusion**

| Code CIM-10 | Thrombose veineuse |
|--:|--:|
| I80.0	| Phlébite et thrombophlébite des veines superficielles des membres inférieurs |
| I80.1	| Phlébite et thrombophlébite de la veine fémorale |
| I80.2	| Phlébite et thrombophlébite d'autres vaisseaux profonds des membres inférieurs |
| I80.3	| Phlébite et thrombophlébite des membres inférieurs, sans précision |
| I80.8	| Phlébite et thrombophlébite d'autres localisations |
| I80.9	| Phlébite et thrombophlébite de localisation non précisée |
| I82.0	| Syndrome de Budd-Chiari |
| I82.1	| Thrombophlébite migratrice |
| I63.6	| Infarctus cérébral dû à une thrombose veineuse cérébrale, non pyogène |
| I67.6 | Thrombose non pyogène du système veineux intracrânien |
| O22.2	| Thrombophlébite superficielle au cours de la grossesse |
| O22.3	| Phlébothrombose profonde au cours de la grossesse |
| O22.5	| Thrombose veineuse cérébrale au cours de la grossesse |
| O87.0	| Thrombophlébite superficielle au cours de la puerpéralité |
| O87.1	| Phlébothrombose profonde au cours de la puerpéralité |
| O87.3	| Thrombose veineuse cérébrale au cours de la puerpéralité |

| Code CIM-10 | Embolie |
|--:|--:|
| I26.0 | Embolie pulmonaire, avec mention de cœur pulmonaire aigu |
| I26.9 | Embolie pulmonaire, sans mention de cœur pulmonaire aigu |
| I82.2 | Embolie et thrombose de la veine cave |
| I82.3 | Embolie et thrombose de la veine rénale |
| I82.8 | Embolie et thrombose d'autres veines précisées |
| I82.9 | Embolie et thrombose d'une veine non précisée |
| O88.2 | Embolie obstétricale par caillot sanguin |

#### Sélection de la période d'étude

L’ensemble des séjours relatifs à la MTEV (séjours à définir) seront extraits sur la période de suivi de 2 ans pour chaque patient.
L'étude rétrospective sur l’année précédente permet d’étudier la durée d’évolution du cancer (temps entre le séjour d’inclusion et le premier diagnostic trouvé pour le même cancer).

<figure class="figure">
    <img src="assets/followup.png" class="img-responsive p-centered" alt="Figure. Schéma de la période d'étude"  style="max-height: 300px"/>
    <figcaption class="figure-caption text-center">Schéma de la période d'étude</figcaption>
</figure>

<figure class="figure">
    <img src="assets/comorbs.png" class="img-responsive p-centered" alt="Figure. Recherche des comorbidités"  style="max-height: 300px"/>
    <figcaption class="figure-caption text-center">Recherche des comorbidités</figcaption>
</figure>


Cette page présente des explications supplémentaires nécessaires à la bonne compréhension de la démarche de l'étude et des résultats.
Cela peut comprendre le plan d'analyse statistique, la justification de certaines hypothèses de base (par exemple l'exclusion d'un certain groupe de patients) ou bien encore des annexes et définitions.

Dans le cadre d'un suivi d'indicateurs, nous pouvons par exemple inclure dans cette page une définition exhaustive de leurs modalités de calcul :

#### Cohorte - critères d'inclusion
Les patients atteints de la maladie X seront repérés dans les données du SNDS en combinant plusieurs critères:
- *Traitement par le médicament Y*
- *Présence d'une ALD de la maladie X*
- *Au moins une hospitalisation avec le code CIM-10 de la maladie X*

#### Mesure de l'outcome / indicateur n°1

- *Définition brève* : Taux de réhospitalisation
- *Justification médicale/métier* : Les patients atteints de la maladie X développent fréquemment la complication Y
- *Sources de données* : PMSI/SNDS Années 2018-2019
- *Population d'application* : Patients de moins de 40 ans ayant eu une opération Z en 2018
- *Formule de calcul* : Diviser le nombre de patients ayant eu une hospitalisation classée Z par la taille de la population d'étude

#### Mesure de l'outcome / indicateur n°2

- *Définition brève* : Taux de décès
- *Justification médicale/métier* : L'étude du taux de patients décédés à 2 ans chez les patients atteint de la maladie X
- *Sources de données* : PMSI/SNDS/CépiDc Années 2018-2020
- *Population d'application* : toute la cohorte étudiée
- *Formule de calcul* : ratio

#### Méthodologie du TAK - Onglet Analyse des séquences de traitement

##### Objectifs

Nous proposons ici une représentation graphique permettant de visualiser la temporalité de l'enchaînement des cycles de traitements des patients.
Cette représentation est basée sur la méthode **TAK** (*Time-sequence Analysis through K-clustering, by HEVA*).
Elle permet de visualiser de manière synthétique les différents types de parcours présents dans la cohorte.
Pour produire ces représentations, elle repose sur un Clustering Hiérarchique Agglomératif à partir de la méthode de Ward et fonctionne en 3 étapes (décrites dans la section *Construction du TAK* sur cette même page).

Le cahier des charges à remplir comporte 3 points :

- Représenter l'*entièreté* de la cohorte
- En ayant une vision *temporelle précise*
- Tout en restant *lisible*

L'avantage majeur de cette approche est d'apporter des informations nouvelles sur les possibles corrélations temporelles entre les outcomes, grâce à une vision d'ensemble des parcours.
Chaque TAK est accompagné d'un **sunburst**, offrant une vue d'ensemble des schémas thérapeutiques.

##### Aide à la lecture du sunburst

[//]: # (section)

Le sunburst (figure à droite) représente l’*enchainement des traitements* des patients d’une cohorte.

Chaque patient commence son suivi au centre du sunburst puis prend un rayon pour direction et va vers l’extérieur du sunburst.

<p>Exemple du <span style="color:#548235;font-weight:bold">patient 1</span></p>
Il rencontre dans un premier temps l’arc de cercle rouge bordeaux, son premier traitement est donc le traitement A. Il ne rencontre aucun autre arc de cercle et finit donc son suivi après n’avoir eu aucun changement de traitement.

<p>Exemple du <span style="color:#8FAADC;font-weight:bold">patient 2</span></p>
Il rencontre dans l’ordre les arcs de cercles bordeaux, jaune et bordeaux à nouveau. Ses traitements durant les 2 années de suivi sont donc le traitement A, puis le traitement B, puis le traitement A à nouveau.

[//]: # (section)

##### Aide à la lecture du TAK

[//]: # (section)

Le TAK (figure à gauche) représente l’*enchainement des traitements* de chaque patient. Par rapport au sunburst il précise la notion de *temporalité*.

Sur l'exemple à gauche, chaque patient commence son suivi sur l’axe vertical à gauche du graphique, et se déplace vers la droite horizontalement à mesure que les 2 ans de suivi avancent.
On repère ainsi à chaque instant de son suivi quel était son traitement.
Le point de repère commun à tous les patients peut être :
- une date index d'inclusion (ex. : diagnostic d'une maladie)
- une date (ex. : mise sur le marché d'un médicament)
- un événement index (ex. : chirurgie de seconde ligne de traitement)

<p>Exemple du <span style="color:#FF5E0F;font-weight:bold"> patient 1</span></p>
Il commence par n’avoir aucun traitement (gris), pendant environ 3 mois, puis il prend le traitement A pendant environ 3 mois (bordeaux), puis n’est plus traité, jusqu’à la fin du suivi (gris).

<p>Exemple du <span style="color:#2BBDC8;font-weight:bold">patient 2</span></p>
Il prend le traitement A tout au long du suivi.

[//]: # (section)

##### Construction du TAK

La construction du TAK se fait en 3 temps :

1. Créer le vecteur modélisant le parcours de soin de chaque patient, sous la forme d'une frise chronologique centrée sur l'inclusion, sur laquelle chaque période sous traitement est renseignée
2. Mettre les uns au-dessus des autres les vecteurs de tous les patients dans un ordre « intelligent » pour faire apparaitre les motifs dans les séquences de soin à l'échelle de la cohorte (technique utilisée: clustering agglomératif)
3. Appliquer un flou sur l'image, réduire le bruit dû aux données de vie réelle et rendre plus lisibles les véritables tendances (technique utilisée: traitement d'image)







