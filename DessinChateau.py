"""
ProjetPythonFirstYear - Petit jeu de labyrinthe python/turtle
Auteur: Alexandre T.
Date: 18/05/2021

Rôle : DessinChateau est le sous programme s'occupant de dessiner le labyrinthe avec de cases de bonnes tailles

Entrée: N.A.

Variables utilisées (déclarées en fin de fichier) : MatricePlan, Pas.
"""

#============================Imports des fichiers et des bibliothèques=================================================#

from CONFIGS import * # All constant variables
from turtle import * # Turtle Python Module
from enum import Enum # Allows you to create the enum of the cells

#======================================================================================================================#

#=============================Définition des fonctions=================================================================#

def lireFichier(fichier):
    """
    Récupères le fichier texte contenant les positions de chaque cases ainsi que leurs types (mur, couloir, porte..)

    fichier: type = String / Fichier que l'on souhaite lire afin d'en récupérer les données

    Returns: type : Matrice 2D / Chaque sous liste de la matrice contient le "plan du chateau ligne par ligne.

    Exemple : Si le fichier est de la forme : 0 1 0 0 0 1 1 1 1 0 1 0 1
                                              1 0 0 1 3 0 0 0 1 1 0 0 1
                                              1 0 1 0 4 1 1 1 1 1 0 0 0

              Alors la matrice de sortie sera de la forme : [[0,1,0,0,0,1,1,1,1,0,1,0,1], [1,0,0,1,3,0,0,0,1,1,0,0,1], [1,0,1,0,4,1,1,1,1,1,0,0,0]]
    """

    listePlan = []  #Liste de listes, matrice 2 dimensions, contenant les coordonnées/types de cases du labyrinthe

    with open(fichier) as file:
        donnees = file.readlines()  # Contains all rows as a list (1 row = 1 item)

    for i in donnees:  # i will have the line
        list_temp = []  # Matrix which will contain in item integer
        for j in i.split():  # j will have each digit of the line i
            list_temp.append(int(j))

        listePlan.append(list_temp)

    return listePlan


def calculer_pas(matrice):
    """
    Cette fonction calcule la taille à donner aux cases du labyrinthe pour que le labyrinthe rentre dans la fenêtre qui lui ait dédiée

    matrice: type : Matrice 2D / Liste contenant les listes représentant ligne par ligne le chateau (définit par la fonction précédente)

    Returns: type : Float / La valeur calculée pour la taille d'une case
    """
    hauteur = len(matrice)  # Hauteur du plan du labyrinthe
    largeur = len(matrice[0])  # largeur du plan du labyrinthe

    largeurMax = abs(ZONE_PLAN_MINI[0]) + abs(ZONE_PLAN_MAXI[0])  # Largeur maximale du plan en coordonnées turtle
    hauteurMax = abs(ZONE_PLAN_MINI[1]) + abs(ZONE_PLAN_MAXI[1])  # Hauteur maximale du plan en coordonnées turtle

    taille = min(largeurMax / largeur, hauteurMax / hauteur)

    return taille


def coordonnes(case, pas):
    """
    Cette fonction calcule les coordonnées en pixels turtle du coin inférieur gauche d'une case du labyrinthe

    case: type : Tuple / Numéro de la case
    pas: type : Float / Dimension d'une case

    Returns: type : Tuple / Coordonnées du coin inférieur gauche de la case passée en argument

    Exemple : La case (43, 0) aura pour coordonnées du coin inférieur gauche (-240,-240)
    """
    coinInfG_coord = []  # Liste qui va contenir temporairement les coordonnées x,y du coin inférieur gauche avant
                         # de la transformer en tuple pour la rendre immuable.

    coinInfG_coord.append(ZONE_PLAN_MINI[0] + case[1] * pas)
    coinInfG_coord.append(ZONE_PLAN_MAXI[1] - pas - case[0] * pas)

    return tuple(coinInfG_coord)


def tracer_carre(dimension):
    """
    Fonction servant à tracer les carrés qui représentent les cases du labyrinthe

    dimension: type : Float / Dimension en pixel turtle du carré à tracer

    Il n'y a pas de "return" mais la fonction trace bien un carré dans la fenêtre turtle.
    """
    traceurCarre.begin_fill()
    for i in range(4):  # In range 4 allows to draw the 4 sides of the square
        traceurCarre.forward(dimension)
        traceurCarre.left(90)
    traceurCarre.end_fill()


def tracer_case(case, couleur, pas):
    """
    Fonction positionnant notre traceur turtle à la bonne position et en préparant la bonne couleur pour tracer notre case.

    case: type : Tuple / Couple de coordonnées définissant la case du labyrinthe à tracer
    couleur: type : String / Définit la couleur de la case à tracer
    pas: type : Float / Récupères la dimension du carré à tracer

    Il n'y a pas de "return" mais la fonction trace bien le carré au bon endroit et avec la bonne couleur dans la fenêtre turtle.
    """
    coord = coordonnes(case, pas)  # TUple contenant les coordonnées turtle

    traceurCarre.color("black", couleur)  # fonction de remplissage en couleur de la case

    traceurCarre.up()
    traceurCarre.goto(coord[0], coord[1])
    traceurCarre.down()

    tracer_carre(pas)


def afficher_plan(matrice):
    """
    Fonction finale de ce fichier python affichant le plan complet du labyrinthe dans la fenêtre turtle.

    matrice: type : Matrice 2D | Plan créé au début du fichier contenant les listes définissant les cases lignes par lignes du chateau
    """
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            tracer_case((i, j), COULEURS[matrice[i][j]], Pas)


    update() #Permet de rafraichir la fenêtre turtle

tracer(0, 0) #gain de temps sur le tracage du chateau

#======================================================================================================================#

#==============================Déclaration des variables utiles========================================================#

MatricePlan = lireFichier(fichier_plan)
Pas = calculer_pas(MatricePlan)

#======================================================================================================================#

#==============================Définitions des robots turtle===========================================================#

traceurCarre = Turtle() # Définition du turtle qui s'occupe de tracer les carrés dans ce fichier DessinChateau
traceurCarre.ht()
traceurCarre.speed(10)

#======================================================================================================================#

