from utils import input_utils
from univers import maison
from univers import personnage
import random

def creer_equipe(maison, equipe_data, est_joueur = False, joueur = None) :

    equipe = {"nom" : maison, "score" : 0, "a_marque" : 0, "a_stoppe" : 0, "attrape_vifdor" : False}
    joueurs = equipe_data[maison]["joueurs"]

    if est_joueur :
        joueurs[0] = joueur["Prénom"] + " " + joueur["Nom"] + " (Attrapeur)"
    equipe["joueurs"] = joueurs

    return equipe


def tentative_marque(equipe_attaque, equipe_defense, joueur_est_joueur = False) :

    proba_but = random.randint(1, 10)

    if proba_but >= 6 :
        equipe_attaque["score"] += 10
        if joueur_est_joueur :
            print(equipe_attaque["joueurs"][0], "marque un but pour", equipe_attaque["nom"], "(+10 points)")
        else :
            print(random.choice(equipe_attaque["joueurs"]), "marque un but pour", equipe_attaque["nom"], "(+10 points)")

    else :
        equipe_defense["a_stoppe"] += 1
        print(equipe_defense["nom"], "bloque l'attaque !")


def apparition_vifdor() :
    if random.randint(1, 6) == 6 :
        return True
    else :
        return False


def attraper_vifdor(e1, e2) :

    if random.randint(1, 2) == 1 :
        e1["score"] += 150
        e1["attrape_vifdor"] = True
        print("Le Vif d'Or a été attrapé par", e1["nom"], "! (+150 points)")
        return e1
    else :
        e2["score"] += 150
        e2["attrape_vifdor"] = True
        print("Le Vif d'Or a été attrapé par", e2["nom"], "! (+150 points)")
        return e2


def afficher_score(e1, e2) :
    print("Score actuel :")
    print("->", e1["nom"], ":", e1["score"], "points")
    print("->", e2["nom"], ":", e2["score"], "points")


def afficher_equipe(maison, equipe) :
    print("Equipe de", maison, ":")
    for i in equipe["joueurs"] :
        print("-", i)


def match_quidditch(joueur, maisons) :
    equipe_data = input_utils.load_fichier("data/equipes_quidditch.json")

    equipe_joueur = creer_equipe(joueur["Maison"], equipe_data, True, joueur)

    ls_maisons = list(maisons.keys())
    ls_maisons.remove(joueur["Maison"])
    maison_adverse = random.choice(ls_maisons)

    equipe_adverse = creer_equipe(maison_adverse, equipe_data, False)

    print("Match de Quidditch :", joueur["Maison"], "contre", maison_adverse, "!")
    input("Appuyez sur entrée pour continuer")

    print()
    afficher_equipe(joueur["Maison"], equipe_joueur)
    print()
    afficher_equipe(maison_adverse, equipe_adverse)

    print()
    print("Vous jouez pour", joueur["Maison"], "en tant qu'Attrapeur")
    input("Appuyez sur entrée pour continuer")

    i = 1
    fin_match = False
    while i <= 20 and not fin_match :

        print("--- Tour", i, "---")
        tentative_marque(equipe_joueur, equipe_adverse, True)
        tentative_marque(equipe_adverse, equipe_joueur, False)

        print()
        afficher_score(equipe_joueur, equipe_adverse)

        if apparition_vifdor() :
            attraper_vifdor(equipe_joueur, equipe_adverse)
            fin_match = True
        else :
            print()
            input("Appuyez sur entrée pour continuer")

        i += 1

    print()
    print("Fin du match !")

    afficher_score(equipe_joueur, equipe_adverse)
    input("Appuyez sur entrée pour continuer")

    equipe_gagnante = None
    if equipe_joueur["score"] > equipe_adverse["score"] :
        equipe_gagnante = equipe_joueur
    elif equipe_adverse["score"] > equipe_joueur["score"] :
        equipe_gagnante = equipe_adverse

    print()
    print("L'équipe de", equipe_gagnante["nom"], "gagne le match !")
    maison.actualiser_points_maison(maisons, equipe_gagnante["nom"], 500)

    if equipe_gagnante["attrape_vifdor"] :
        maison.actualiser_points_maison(maisons, equipe_gagnante["nom"], 150)
    else :
        maison.actualiser_points_maison(maisons, equipe_gagnante["nom"], equipe_gagnante["score"])

    print()
    maison.afficher_maison_gagnante(maisons)


def lancer_chapitre_4(joueur, maisons) :
    print()
    print()
    print("Chapitre 4 : Finale du match de quidditch de la coupe des quatre maisons")

    match_quidditch(joueur, maisons)

    print("Fin du chapitre 4.")
    print()
    personnage.afficher_personnage(joueur)