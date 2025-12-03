from utils import input_utils

def actualiser_points_maison(maisons, nom_maison, points) :
    if nom_maison not in maisons.keys() :
        print("Cette maison n'existe pas !")
    else :
        maisons[nom_maison] += points
        if points >= 0 :
            print("La maison {} gagne {} points pour un total de {} points.".format(nom_maison, points, maisons[nom_maison]))
        else :
            print("La maison {} perd {} points pour un total de {} points.".format(nom_maison, points, maisons[nom_maison]))


def afficher_maison_gagnante(maisons) :

    score_max = maisons["Gryffondor"]
    for i in maisons :
        if maisons[i] > score_max :
            score_max = maisons[i]

    liste_gagnants = []
    for i in maisons :
        if maisons[i] == score_max :
            liste_gagnants += [i]

    if len(liste_gagnants) == 1 :
        print("La maison gagnante est {} avec un total de {} points.".format(liste_gagnants[0], score_max))
    else :
        print("Les maisons gagnantes sont : ", end="")
        for i in liste_gagnants :
            print(i, end=", ")
        print("avec un total de {} points.".format(score_max))


def repartition_maison(joueur, questions) :
    points = {"Gryffondor" : 0, "Serpentard" : 0, "Poufsouffle" : 0, "Serdaigle" : 0}

    points["Gryffondor"] += 2 * joueur["Attributs"]["courage"]
    points["Serpentard"] += 2 * joueur["Attributs"]["ambition"]
    points["Poufsouffle"] += 2 * joueur["Attributs"]["loyauté"]
    points["Serdaigle"] += 2 * joueur["Attributs"]["intelligence"]

    for q in questions :
        print()
        choix = input_utils.demander_choix(q[0], q[1])

        for j in range(len(q[1])) :
            if q[1][j] == choix :
                points[q[2][j]] += 3

    score_max = 0
    maison_choisie = ""

    print()
    print("Résumé des scores :")
    for i in points :
        if points[i] > score_max :
            score_max = points[i]
            maison_choisie = i
        print(i, ":", points[i], "points")

    return maison_choisie

