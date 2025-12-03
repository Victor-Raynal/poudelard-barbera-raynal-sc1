from utils import input_utils
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

