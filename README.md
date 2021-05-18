# ProjetPythonFirstYear
Projet Python de première année de DUT Réseaux &amp; Telecommunication. Le but du jeu est de sortir du labyrinthe en trouvant des indices et en ouvrant les portes successivement en répondant à des questions.
>Python project in first year of DUT Networks &amp; Telecommunication. The goal is to get out the labyrinth by finding clues and opening doors by answering questions.

## Installation / Lancement du jeu (Installating / Lauching)

Avec n'importe quel IDE supportant le language Python
>With any Python IDE

```
Lancer le programme main.py
>Run the main.py program
```

## Bibliothèques utilisées / Librairies used

* Turtle
  * Bibliothèque basée sur tkinter, utilisant un "robot" traçant des formes complexes à partir d'instruction élémentaires répétées (https://docs.python.org/fr/3/library/turtle.html)
  * > Librairy based on tkinter, uses a "robot" drawing complex forms with successive elementary operation (https://docs.python.org/3/library/turtle.html)

* Enum
  * Une énumération est un ensemble de noms symboliques, appelés membres, liés à des valeurs constantes et uniques. Au sein d'une énumération, les membres peuvent être comparés entre eux et il est possible d'itérer sur l'énumération elle-même. (https://docs.python.org/fr/3/library/enum.html)
  * >An enumeration is a set of symbolic names (members) bound to unique, constant values. Within an enumeration, the members can be compared by identity, and the enumeration itself can be iterated over. (https://docs.python.org/3/library/enum.html)
 
## Construction / possibilité du jeu (Building / Possibilities in game)

* Organisation du projet: Le projet est scindé en sous programme s'occupant chacuns de leur point précis du jeu : (Main program is split in parts which manage a particular part)
  * DessinChateau.py qui se charge du dessin du labyrinthe (drawing the labyrinth)
  * Deplacement.py qui se charge du déplacement du personnage dans le labyrinthe (allow the player to move in the labyrinth) 
  * ReglesDuJeu.py qui s'occupe de gérer les règles du jeu et les événements qui y surviennent (manage the game's rules and the events in game)

* Possibilité en jeu (possibilities in game)
  * Un niveau jouable (unique level)
  * Déplacement jusqu'à l'arrivée détection de la victoire (move to the victory cell and victory detect)
  * Ramassage d'objet et questionnement aux portes (pick up objects and questionning at the doors)

## Meta

Alexandre T - alexandretornier6@gmail.com

Distributed under the CreativeCommons CC BY 4.0 license.

[MyGit](https://github.com/TornierCPE)
