"""
ProjetPythonFirstYear - Petit jeu de labyrinthe python/turtle
Auteur: Alexandre T.
Date: 18/05/2021

Rôle : main.py est le programme principal qui lance le jeu

Entrée: Import du sous programme s'occupant des déplacement du personnage
"""

from Deplacement import *

listen() #Fonction permettant d'attendre les entrées utilisateurs au clavier

#Les 4 fonctions suivantes permettent de définir le rôle des touches qu'on autorise dans le jeu, ici les flèches directionelles du clavier.
onkeypress(deplacer_gauche, "Left")
onkeypress(deplacer_droite, "Right")
onkeypress(deplacer_haut, "Up")
onkeypress(deplacer_bas, "Down")

mainloop()