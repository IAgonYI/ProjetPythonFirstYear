"""
ProjetPythonFirstYear - Petit jeu de labyrinthe python/turtle
Auteur: Alexandre T.
Date: 18/05/2021

Rôle : ReglesDuJeu est le sous programme qui s'occupe de tout ce qui concerne les règles du jeu, les évenements comme les objets et les
       portes, ainsi que la victoire.

Entrée: Import du sous programme s'occupant du dessin du labyrinthe

Variables utilisées (déclarées en fin de fichier) : MatricePlan, Pas, TotalObjet , DictObjets, DictQuestions, coordInventaire
"""

#=================================Import des fichiers et bibliothèques=================================================#

from CONFIGS import * # Toutes les variables imposées par l'énoncé
from turtle import * # Import de la bibliothèque Turtle
from enum import Enum # Import de la bibliothèque Enum
from DessinChateau import *

#======================================================================================================================#

#=========================================Déclaration des fonctions====================================================#

def creer_dictionnaire(fichier_des_objets):
    """
    Fonction servant à lire des fichiers et récupérer les données qu'ils contiennent

    fichier_des_objets: type = String / Fichier que l'on souhaite lire afin d'en récupérer les données

    Returns: type = Dictionnaire / Dictionnaire (objet ou questions) en fonction de l'appel de la fonction en fin de page,
             format = case:objet/question (tuple:string)
    """
    dico = {}  # Création du dictionnaire

    with open(fichier_des_objets, mode="r", encoding="utf-8") as file:
        donnes = file.readlines()

        for i in donnes:
            case, objet = eval(i)
            dico[case] = objet

    return dico


def casePossible(case):
    """
    Fonction permettant en premier lieu de savoir si une case est atteignable ou non
    Dans un second temps en fonction du type de la case, on execute une action particulière

    case: type = Tuple / Case concernée

    Return: type = Boolean / Indique si le joueur peut se déplacer sur la case
    """
    try:
        typeOfCase = MatricePlan[case[0]][case[1]]  # Integer which will have the number of the type of cell
    except:  # Gère le cas improbable ou le joueur essayerait de sortir du plan
        return False

    if (typeOfCase == Case.LAMBDA.value):  # 0 = Case lambda
        return True
    elif (typeOfCase == Case.VICTOIRE.value):  # 2 = Case correspondant à la sortie du labyrinthe
        messageVictoire()
        return True
    elif (typeOfCase == Case.PORTE.value):  # 3 = Case correspondant à une porte
        if (poser_question(case)):
            return True
        else:
            return False
    elif (typeOfCase == Case.OBJET.value):  # 4 = Case contenant un objet
        ramasser_objet(case)
        return True
    else:  # Autre cas 1 = Mur infranchissable
        return False


def ramasser_objet(case):
    """
    Fonction servant à gérer les cases contenant un objet, affichant l'objet ramasser et en l'affichant dans l'inventaire

    case: type = Tuple / Case concernée

    Il n'y a pas de "return" mais la fonction a bien permit de ramasser l'objet et a remplacer la couleur objet par une couleur de case normale
    permettant de savoir qu'il n'y a plus d'objet à ramasser à cet endroit
    """
    global TotalObjet  # Variable stockant l'information du nombre d'objets trouvé dans le labyrinthe, global afin de pouvoir la modifier
                            # à d'autre endroits du code

    inventaire.up()
    inventaire.goto(coordInventaire[0], coordInventaire[1] - 15 * TotalObjet)  # -15 simulant un saut de ligne
    inventaire.down()
    inventaire.write("N°" + str(TotalObjet + 1) + ": " + DicoObjets[case], font=("Arial", 10, "normal"))

    evenement.clear()
    evenement.write("Bien vu l'aveugle, vous avez trouvé: " + DicoObjets[case], font=("Arial", 12, "bold"))  # Affiche l'annonce de découverte de l'objet

    TotalObjet += 1
    tracer_case(case, COULEUR_CASES, Pas)
    MatricePlan[case[0]][case[1]] = 0  # Passe la case de case objet à case lambda


def poser_question(case):
    """
    Cette fonction sert à poser la question correspondante à la case au joueur

    case: type = Tuple / Case concernée

    Returns: type = Boolean / Renvoie si la réponse donnée par le joueur est la bonne ou non
    """
    evenement.clear()
    evenement.write("Cette porte est fermée, il vous faut répondre à la question.", font=("Arial", 12, "bold"))

    reponse = textinput("Porte", DicoQuestions[case][0])  # Récupère la réponse du joueur
    listen()  # Attends la réponse du joueur

    if (reponse == DicoQuestions[case][1]):  # Si la réponse est bonne
        tracer_case(case, COULEUR_CASES, Pas)
        MatricePlan[case[0]][case[1]] = 0  # Il n'y a plus de porte la case devient donc lambda
        evenement.clear()
        evenement.write("Bien joué sherlock, *la porte s'ouvre*", font=("Arial", 12, "bold"))

        return True
    else:  # Si la réponse est mauvaise
        evenement.clear()
        evenement.write("Aïe Aïe Aïe, heuresement vous pouvez réessayer, *une voix ricane au loin*", font=("Arial", 12, "bold"))
        return False


def messageVictoire():
    """
    Fonction servant à afficher le message de victoire du jeu au joueur, pas de return.
    """
    evenement.clear()
    evenement.write("Eh bah quand même ! En plus y'a même pas de minautore, bien joué !", font=("Arial", 12, "bold"))


def victoire(case):
    """
    Fonction detectant si on se trouve sur la case de victoire

    case: type = Tuple / Case correspondante

    Returns: type = Boolean / Permet de savoir si le joueur a gagné ou non.
    """
    if (MatricePlan[case[0]][case[1]] == Case.VICTOIRE.value):
        return True
    else:
        return False


class Case(Enum):
    """
    Enumeration des cases, permet de limitée les erreurs lors de l'utilisation des types de cases. On ne compare
    pas des chaines de caractères où les erreurs d'orthographes sont vites arrivées et plante le programme
    on compare des nombres type = Int
    """
    LAMBDA = 0
    MUR = 1
    VICTOIRE = 2
    PORTE = 3
    OBJET = 4

#======================================================================================================================#

#=======================================Déclaration des variables======================================================#

MatricePlan = lireFichier(fichier_plan)
Pas = calculer_pas(MatricePlan)
TotalObjet = 0
DicoObjets = creer_dictionnaire(fichier_objets)  # Dictionnaire contenant les objets, format = case/objet (Tuple/String)
DicoQuestions = creer_dictionnaire(fichier_questions)  # Dictionnaire contenant les questions, format = case/réponse (Tuple/String)
coordInventaire = (POINT_AFFICHAGE_INVENTAIRE[0], POINT_AFFICHAGE_INVENTAIRE[1] - 15)  # Coordonnées turtle de la première ligne de l'inventaire

#======================================================================================================================#

#====================================Définition des robots turtle======================================================#
inventaire = Turtle()  # Définition du turtle qui va s'occuper de l'inventaire
inventaire.ht()
inventaire.up()
inventaire.goto(POINT_AFFICHAGE_INVENTAIRE[0], POINT_AFFICHAGE_INVENTAIRE[1])
inventaire.down()
inventaire.write("Inventaire", font=("Arial", 10, "bold"))

evenement = Turtle()  # Définition du turtle s'occupant des annonce au joueur
evenement.ht()
evenement.up()
evenement.goto(POINT_AFFICHAGE_ANNONCES[0], POINT_AFFICHAGE_ANNONCES[1])
evenement.down()

#======================================================================================================================#

#==================================Lancement des fonctions utiles======================================================#

afficher_plan(MatricePlan)

#======================================================================================================================#