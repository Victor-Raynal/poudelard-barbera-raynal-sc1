from utils import input_utils
import chapitres

def lancer_chapitre(chapitre, joueur) :

    messages_chapitres = { 1 : "Lancer le chapitre 1 - L'arrivée dans le monde magique",
                           2 : "Lancer le chapitre 2 - Le voyage vers Poudlard",
                           3 : "Lancer le chapitre 3 - Les cours et la découverte de Poudlard"
                           4 : "Lancer le chapitre 4 - La finale de Quidditch"
                           5 : "Lancer le chapitre 5 - "
                           }

    choix = input_utils.demander_choix("Que souhaitez-vous faire ?", [messages_chapitres[chapitre], "Quitter le jeu"])

    if choix == "Quitter le jeu" :
        print("\n\n")
        print("Au revoir !")
        return


    if chapitre == 1 :
        chapitres.chapitre_1.lancer_chapitre_1()
    elif chapitre == 2 :
        chapitres.chapitre_2.lancer_chapitre_2(joueur)
    elif chapitre == 3 :
        chapitres.chapitre_3.lancer_chapitre_3(joueur)
    elif chapitre == 4 :
        chapitres.chapitre_4.lancer_chapitre_4(joueur)
    elif chapitre == 5 :
        chapitres.chapitre_5_extension.lancer_chapitre_5(joueur)
