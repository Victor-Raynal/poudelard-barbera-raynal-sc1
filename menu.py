from utils import input_utils
from sauvegarde import sauvegarde_utils
from chapitres import chapitre_1
from chapitres import chapitre_2
from chapitres import chapitre_3
from chapitres import chapitre_4

def lancer_chapitre(chapitre, joueur, maisons) :

    if chapitre == 1 :
        return chapitre_1.lancer_chapitre_1()
    elif chapitre == 2 :
        chapitre_2.lancer_chapitre_2(joueur)
    elif chapitre == 3 :
        chapitre_3.lancer_chapitre_3(joueur, maisons)
    elif chapitre == 4 :
        chapitre_4.lancer_chapitre_4(joueur, maisons)


def lancer_chapitre_suivant(chapitre, joueur, maisons) :

    if chapitre == 5 :
        print()
        print()
        print("Votre aventure est terminée !")
        print("Merci d'avoir joué au jeu...")
        exit()

    messages_chapitres = {
                           2 : "Lancer le chapitre 2 - Le voyage vers Poudlard",
                           3 : "Lancer le chapitre 3 - Les cours et la découverte de Poudlard",
                           4 : "Lancer le chapitre 4 - La finale de Quidditch",
                           }

    options = [messages_chapitres[chapitre], "Sauvegarder et quitter", "Quitter sans sauvegarder"]
    choix = input_utils.demander_choix("Que souhaitez-vous faire ?", options)

    if choix == "Quitter sans sauvegarder" :
        exit()
    elif choix == "Sauvegarder et quitter" :
        sauvegarde_utils.sauvegarder(chapitre, joueur, maisons)
        exit()

    lancer_chapitre(chapitre, joueur, maisons)


def demander_continuer_partie() :

    options = ["Reprendre la partie sauvegardée", "Démarrer une nouvelle partie", "Quitter le jeu"]
    choix = input_utils.demander_choix("Que souhaitez-vous faire ?", options)

    if choix == "Quitter le jeu" :
        exit()
    elif choix == "Reprendre la partie sauvegardée" :
        chapitre, joueur, maisons = sauvegarde_utils.load_sauvegarde()

        if chapitre == None :
            print("Aucune sauvegarde trouvée")
            exit()

        lancer_chapitre(chapitre, joueur, maisons)
        return chapitre, joueur, maisons
    else :
        joueur = lancer_chapitre(1, None, None)
        return 1, joueur, {"Gryffondor" : 0, "Serpentard" : 0, "Poufsouffle": 0, "Serdaigle" : 0}


def lancer_menu() :
    chapitre, joueur, maisons = demander_continuer_partie()

    while True :
        chapitre += 1
        lancer_chapitre_suivant(chapitre, joueur, maisons)