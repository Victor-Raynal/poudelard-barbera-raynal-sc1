from utils import input_utils
from univers import maison
from univers import personnage

def rencontrer_amis(joueur) :

    print()
    texte = "Vous montez à bord du Poudlard Express. Le train démarre lentement en direction du Nord... Un garçon roux "
    texte += "entre dans votre compartiment, l'air amical."
    input_utils.afficher_texte(texte, ["Nord..."])

    print(" - Salut ! Moi c'est Ron Weasley. Tu veux bien qu'on s'assoie ensemble ?")
    message = "Que répondez-vous ?"
    options = ["Bien sûr, assieds-toi !", "Désolé, je préfère voyager seul."]
    choix = input_utils.demander_choix(message, options)

    if choix == "Bien sûr, assieds-toi !" :
        joueur["Attributs"]["loyauté"] += 1
        print("Ron sourit : - Génial ! Tu verras, Poudlard, c'est incroyable !")
    else :
        joueur["Attributs"]["ambition"] += 1
        print(" - Bon... eh bien à une prochaine peut-être !")



    print()
    print("Une fille rentre ensuite, portant déjà une pile de livres.")
    replique = " - Bonjour, je m'appelle Hermione Granger. Avez-vous déjà lu 'Histoire de la magie' ? "
    input_utils.afficher_texte(replique)
    options = ["Oui, j'adore apprendre de nouvelles choses !", "Euh... non, je préfère les aventures aux bouquins"]
    choix = input_utils.demander_choix(message, options)

    if choix == "Oui, j'adore apprendre de nouvelles choses !" :
        joueur["Attributs"]["intelligence"] += 1
        print(" - Il n'y a rien de mieux qu'un bon livre pour passer le temps !")
    else :
        joueur["Attributs"]["courage"] += 1
        print("Hermione fronce les sourcils : - Il faudrait pourtant s'y mettre un jour !")



    print()
    print("Puis un garçon blond entre avec un air arrogant.")
    replique = " - Je suis Drago Malefoy. Mieux vaut bien choisir ses amis dès le départ n'est-ce pas ?"
    input_utils.afficher_texte(replique)
    message = "Comment réagissez-vous ?"
    options = ["Je lui sert la main poliment.", "Je l'ignore complètement.", "Je lui réponds avec arrogance."]
    choix = input_utils.demander_choix(message, options)

    if choix == "Je lui sert la main poliment." :
        joueur["Attributs"]["ambition"] += 1
        print("Drago sourit d'un air satisfait : - Je suis sûr que nous pourrons nous entendre...")
    elif choix == "Je l'ignore complètement." :
        joueur["Attributs"]["loyauté"] += 1
        print("Drago fronce les sourcils, vexé. - Tu le regretteras !")
    else :
        joueur["Attributs"]["courage"] += 1
        texte = " - Oui, et mon petit doigt me dit que t'avoir comme ami serait un très mauvais choix."
        texte += " - Je peux te promettre que tu le regretteras le jour où je serais plus fort que toi en magie !"
        input_utils.afficher_texte(texte, ["choix."])


    texte = "Le train continue sa route. Le château de Poudlard se profile à l'horizon... Vos choix semblent déjà "
    texte += "en dire long sur votre personnalité ! Vos attributs ont été modifiés : "
    input_utils.afficher_texte(texte, ["l'horizon...", "!"])
    for i in joueur["Attributs"] :
        print("-", i, ":", joueur["Attributs"][i])



def mot_de_bienvenue() :
    return



def ceremonie_repartition(joueur) :
    questions = [
        (
            "Vous voyez un ami en danger. Que faites-vous ?",
            ["Je fonce l'aider", "Je réfléchis à un plan", "Je cherche de l’aide", "Je reste calme et j’observe"],
        ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
        ),
        (
            "Quel trait vous décrit le mieux ?",
            ["Courageux et loyal", "Rusé et ambitieux", "Patient et travailleur", "Intelligent et curieux"],
             ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
        ),
        (
            "Face à un défi difficile, vous...",
            ["Foncez sans hésiter", "Cherchez la meilleure stratégie",
             "Comptez sur tes amis", "Analysez le problème"],
            ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
        )
    ]

    print()
    print("La cérémonie de répartition commence dans la Grande Salle...")
    print("Le choixpeau magique t'observe longuement avant de poser ses question : ")

    maison_choisie = maison.repartition_maison(joueur, questions)

    print()
    print("Le Choixpeau s'exclame :", maison_choisie, "!!!")
    print("Tu rejoins les élèves de", maison_choisie, "sous les acclamations !")
    joueur["Maison"] = maison_choisie



def installation_salle_commune(joueur) :
    fichier_maisons = input_utils.load_fichier("data/maisons.json")

    print()
    print(fichier_maisons[joueur["Maison"]]["emoji"], fichier_maisons[joueur["Maison"]]["description"])
    print(fichier_maisons[joueur["Maison"]]["message_installation"])
    print("Les couleurs de votre maison sont :", fichier_maisons[joueur["Maison"]]["couleurs"][0], "et", fichier_maisons[joueur["Maison"]]["couleurs"][1])

    for i in fichier_maisons[joueur["Maison"]]["bonus_attributs"] :
        joueur["Attributs"][i] += fichier_maisons[joueur["Maison"]]["bonus_attributs"][i]

    print()
    print("Vos attributs ont été mis à jour.")
    personnage.afficher_personnage(joueur)



def lancer_chapitre_2(joueur) :
    rencontrer_amis(joueur)
    mot_de_bienvenue()
    ceremonie_repartition(joueur)
    installation_salle_commune(joueur)

    print("\n\n")
    print("Vous avez terminé le chapitre 2 avec succès ! Les cours à Poudlard peuvent à présent démarrer.")