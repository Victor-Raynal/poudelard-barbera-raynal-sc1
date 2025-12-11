from utils import input_utils
from univers import personnage
from utils.input_utils import afficher_texte


def introduction() :
    print('''Bienvenue cher joueur ! Nous vous proposons une histoire aussi magique que détaillée où vous serez plongé dans l'univers 
d'Harry Potter et vivrez à votre manière les moments les plus mémorables d'un élève débutant à Poudlard !

Cette chaude soirée d'août se clôt alors qu'une légère brise ébouriffe tes cheveux. La libération de l'été a rapidement fait place à l'ennui.
Après tout, chez les Dursley, mis à part les rares sorties qu'on t'autorise, le seul passe-temps toléré est la contemplation du cagibi.
D'un soupir, tu te hisses sur la balançoire, le fragile équilibre assuré par tes bras tendus, tu es penché en arrière et tes cheveux caressent le gazon. 
Alors que le sang afflue dans ta tête, tu remarques qu'il commence à faire sombre. Si tu ne souhaites pas subir les injures de ton tyrannique oncle
Vernon, il te faudra rentrer au plus vite. Tu prends cependant le temps d'observer le tableau qui se dessine devant toi : 
La tige d'un gris métallique de la balançoire, le sentier à peine discernable qui te raccompagnera, et ce chez-toi dont tu distingues la silhouette de loin. 
Cet endroit qui est ton foyer mais où tu es traité en étranger. Cela dit, un détail interpelle ton regard, un point blanc semble voltiger au-dessus du toit.
Poussé simultanément par ta curiosité et la peur d'être puni, tu rentres en vitesse. Alors que tu passes la boîte aux lettres, ton regard est attiré 
par ton reflet dans la fenêtre luisante. Ses quatre yeux ronds te fixent, et son expression chargée d'une profonde interrogation comme pour te demander :
"Au fond, qui es-tu ?"
''')
    return


def creer_personnage() :
    nom = input_utils.demander_texte("Entrez le nom de votre personnage : ")
    prenom = input_utils.demander_texte("Entrez le prénom de votre personnage : ")

    attributs = {"courage" : 0, "intelligence" : 0, "loyauté" : 0, "ambition" : 0}

    print()
    print("Choisissez vos attributs : ")
    attributs["courage"] = input_utils.demander_nombre("Niveau de courage (1-10) : ", 1, 10)
    attributs["intelligence"] = input_utils.demander_nombre("Niveau d'intelligence (1-10) : ", 1, 10)
    attributs["loyauté"] = input_utils.demander_nombre("Niveau de loyauté (1-10) : ", 1, 10)
    attributs["ambition"] = input_utils.demander_nombre("Niveau d'ambition (1-10) : ", 1, 10)

    joueur = personnage.initialiser_personnage(nom, prenom, attributs)

    personnage.afficher_personnage(joueur)

    return joueur


def recevoir_lettre() :
    texte = "Une chouette traverse la fenêtre et vous apporte une lettre scellée du sceau de Poudlard... "
    texte += "« Cher élève, Nous avons le plaisir de vous informer que vous avez été admis à l’école de sorcellerie "
    texte += "de Poudlard ! »"

    sauts = ["Poudlard...", "élève,"]
    input_utils.afficher_texte(texte, sauts)

    question = "Souhaitez-vous accepter l'invitation et partir pour Poudlard ?"
    options = ["Oui bien sûr !", "Non, je préfère rester avec l'oncle Vernon..."]
    choix = input_utils.demander_choix(question, options)

    if choix != "Oui bien sûr !" :

        texte = "Vous déchirez la lettre, l’oncle Vernon pousse un cri de joie: « EXCELLENT ! Enfin quelqu’un "
        texte += "de NORMAL dans cette maison ! » Le monde magique ne saura jamais que vous existiez..."
        sauts = ["joie:", "»"]
        input_utils.afficher_texte(texte, sauts)

        exit()


def rencontrer_hagrid(joueur) :
    texte = "Hagrid : «Salut " + str(joueur["Prénom"]) + " ! Je suis venu t’aider à faire tes achats sur le Chemin de Traverse.»"
    input_utils.afficher_texte(texte)

    question = "Voulez-vous suivre Hagrid ?"
    options = ["Oui", "Non"]
    choix = input_utils.demander_choix(question, options)

    if choix == "Oui" :
        input_utils.afficher_texte("Hagrid vous emmène avec lui.")
    else :
        input_utils.afficher_texte("Hagrid insiste gentiment et vous entraîne quand même avec lui!")


def acheter_fournitures(joueur) :
    print("\033[1mBienvenue sur le chemin de traverse !\033[1m")
    print("\033[0m\033[0m")

    texte_catalogue = "Catalogue des objets disponibles : "
    catalogue = input_utils.load_fichier("data/inventaire.json")
    for i in catalogue :
        texte_catalogue += i + ". " +catalogue[i][0] + " - " + str(catalogue[i][1]) + " galions "

    input_utils.afficher_texte(texte_catalogue, ["galions", ":"])

    objets_obligatoires = ["Baguette magique", "Robe de sorcier", "Manuel de potions"]
    montant_necessaire =   80

    while len(objets_obligatoires) != 0 and joueur["Argent"] >= montant_necessaire :

        print()
        print("Vous avez", joueur["Argent"], "galions")
        print("\033[1mObjets obligatoires restants à acheter : \033[1m", ", ".join(objets_obligatoires))

        achete = False
        while not achete :
            numero = input_utils.demander_nombre("\033[0mEntrez le numéro de l'objet à acheter : \033[0m", 1, 8)
            numero = str(numero)
            objet = catalogue[numero][0]
            montant = catalogue[numero][1]

            if joueur["Argent"] >= montant :

                achete = True
                personnage.modifier_argent(joueur, -montant)
                personnage.ajouter_objet(joueur, "Inventaire", objet)

                if objet in objets_obligatoires :
                    objets_obligatoires.remove(objet)
                    montant_necessaire -= montant

                print("Vous avez acheté : {} (-{} galions).".format(objet, montant))

            else :
                print("Cet objet est trop cher, veuillez en choisir un autre.")

    print()
    if len(objets_obligatoires) != 0 :
        print("\033[1mVous n'avez plus assez d'argent pour acheter les objets obligatoires. La partie est perdue.")
        exit()
    else :
        print("\033[1mTous les objets obligatoires ont été achetés !")



    print("\033[1mIl est temps de choisir votre animal de compagnie pour Poudlard !\033[1m")
    print("\033[0mVous avez\033[0m", joueur["Argent"], "galions")
    if joueur["Argent"] < 5 :
        print("Vous n'avez plus assez d'argent pour acheter un animal de compagnie. La partie est perdue.")
        exit()

    message = "Voici les animaux disponibles :"
    options = {"Chouette - 20 galions" : (20, "Chouette"), "Chat - 15 galions" : (15, "Chat"),
               "Rat - 10 galions" : (10, "Rat"), "Crapaud - 5 galions" : (5, "Crapaud")}
    achete = False
    while not achete :
        choix = input_utils.demander_choix(message, list(options.keys()))
        montant = options[choix][0]
        if joueur["Argent"] < montant :
            print("Vous n'avez pas assez d'argent pour acheter cet animal.")
            print()
        else :
            print("Vous avez choisi :", options[choix][1])
            personnage.modifier_argent(joueur, -montant)
            personnage.ajouter_objet(joueur, "Inventaire", options[choix][1])
            achete = True

    print("\033[1mTous les objets obligatoires ont été ajoutés avec succès !\033[1m \033[0mVoici votre inventaire final :\033[0m")
    print()
    personnage.afficher_personnage(joueur)


def lancer_chapitre_1() :
    introduction()
    joueur = creer_personnage()
    recevoir_lettre()
    rencontrer_hagrid(joueur)
    acheter_fournitures(joueur)

    print("\n\n\n")
    print("Fin du chapitre 1 ! Votre aventure commence à Poudlard.")

    return joueur

