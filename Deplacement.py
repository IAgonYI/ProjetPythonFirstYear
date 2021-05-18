"""
ProjetPythonFirstYear - Petit jeu de labyrinthe python/turtle
Auteur: Alexandre T.
Date: 18/05/2021

Rôle : Deplacement.py est le sous programme qui s'occupe de gérer le déplacement du personnage dans les quatres directions
       haut, bas, droite, gauche.

Entrée: Import du sous programme s'occupant du dessin du labyrinthe
        Import du sous programme s'occupant des règles du jeu

Variables utilisées (déclarées en fin de fichier) : MatricePlan, Pas, positionPersonnage.
"""

#===========================Imports des fichiers et des bibliothèques==================================================#

from CONFIGS import * # Toutes les variables imposées par l'énoncé
from turtle import * # Import de la bibliothèque Turtle
from enum import Enum # Import de la bibliothèque Enum
from DessinChateau import *
from ReglesDuJeu import *

#======================================================================================================================#

#=======================================Déclaration des fonctions======================================================#

def deplacer_haut():
    """
    Fonction qui se déclenche dans main.py, qui s'occupe du déplacement du personnage vers le haut
    lorsque le joueur appuie sur la flèche up de son clavier
    """
    global positionPersonnage  # Position du joueur déclaré en global, sinon elle n'est pas modifiable à chaque endroit souhaité dans le programme

    onkeypress(None, "Up")

    nouvellePosition = (positionPersonnage[0] - 1, positionPersonnage[1])  # Calcul des nouvelles positions
    positionPersonnage = deplacer(positionPersonnage, nouvellePosition)  # Deplace le personnage de l'ancienne position à la nouvelle

    if (positionPersonnage != None):  # Vérification si il y a une position retournée ou non afin d'éviter les erreurs de collisions
        onkeypress(deplacer_haut, "Up")

def deplacer_bas():
    """
    Fonction qui se déclenche dans main.py, qui s'occupe du déplacement du personnage vers le bas
    lorsque le joueur appuie sur la flèche down de son clavier
    """
    global positionPersonnage  # Position du joueur déclaré en global, sinon elle n'est pas modifiable à chaque endroit souhaité dans le programme

    onkeypress(None, "Down")

    nouvellePosition = (positionPersonnage[0] + 1, positionPersonnage[1])  # Calcul des nouvelles positions
    positionPersonnage = deplacer(positionPersonnage, nouvellePosition)  # Deplace le personnage de l'ancienne position à la nouvelle

    if (positionPersonnage != None):  # Vérification si il y a une position retournée ou non afin d'éviter les erreurs de collisions
        onkeypress(deplacer_bas, "Down")

def deplacer_droite():
    """
    Fonction qui se déclenche dans main.py, qui s'occupe du déplacement du personnage vers la droite
    lorsque le joueur appuie sur la flèche right de son clavier
    """
    global positionPersonnage  # Position du joueur déclaré en global, sinon elle n'est pas modifiable à chaque endroit souhaité dans le programme

    onkeypress(None, "Right")

    nouvellePosition = (positionPersonnage[0], positionPersonnage[1] + 1)  # Calcul des nouvelles positions
    positionPersonnage = deplacer(positionPersonnage,nouvellePosition)  # Deplace le personnage de l'ancienne position à la nouvelle

    if (positionPersonnage != None):  # Vérification si il y a une position retournée ou non afin d'éviter les erreurs de collisions
        onkeypress(deplacer_droite, "Right")


def deplacer_gauche():
    """
    Fonction qui se déclenche dans main.py, qui s'occupe du déplacement du personnage vers la gauche
    lorsque le joueur appuie sur la flèche left de son clavier
    """
    global positionPersonnage  # Position du joueur déclaré en global, sinon elle n'est pas modifiable à chaque endroit souhaité dans le programme

    onkeypress(None, "Left")

    nouvellePosition = (positionPersonnage[0], positionPersonnage[1] - 1) # Calcul des nouvelles positions
    positionPersonnage = deplacer(positionPersonnage,nouvellePosition)  # Deplace le personnage de l'ancienne position à la nouvelle

    if (positionPersonnage != None):  # Vérification si il y a une position retournée ou non afin d'éviter les erreurs de collisions
        onkeypress(deplacer_gauche, "Left")

def deplacer(positionInit, positionFin):
    """
    Cette fonction permet de déplacer le compteur sur la case voulue (suivant l'appuie des flèches).

    position: Type : Tuple / position actuelle du joueur
    mouvement: Type : Tuple / position désirée du joueur après déplacement
    Returns: Tuple | Player position (changed or unchanged)
    """
    if (victoire(positionInit)):  # Si le joueur a gagné (se trouve sur la case victoire)
        onkeypress(None, "Left")
        onkeypress(None, "Right")
        onkeypress(None, "Up")
        onkeypress(None, "Down")

        bye()  # On ferme le jeu
        return None
    elif (casePossible(positionFin)):  # Si le joueur n'a pas gagné et qu'il peut se déplacer
        characterDot.clear() #Efface le précédent personnage pour ne pas se retrouver avec un labyrinthe plein de point rouge.

        coordMouvement = coordonnes(positionFin, Pas)  # Tupple des nouvelles coordonnées turtle

        characterDot.up()
        characterDot.goto(coordMouvement[0] + Pas / 2, coordMouvement[1] + Pas / 2)
        characterDot.down()
        characterDot.dot(Pas * RATIO_PERSONNAGE, COULEUR_PERSONNAGE)

        update()

        return positionFin
    else:  # Si le joueur ne peut pas jouer
        return positionInit

#======================================================================================================================#

#==================================Déclaration des variables===========================================================#

MatricePlan = lireFichier(fichier_plan)
Pas = calculer_pas(MatricePlan)
positionPersonnage = POSITION_DEPART  # Position initiale du joueur dans le labyrinthe

#======================================================================================================================#

#==================================Définition des robots turtle========================================================#

characterDot = Turtle()  # Définition du turtle qui s'occupe de l'affichage dynamique de notre joueur
characterDot.ht()

#======================================================================================================================#

#==================================Lancement des fonctions utiles======================================================#

deplacer(POSITION_DEPART, POSITION_DEPART)

#======================================================================================================================#