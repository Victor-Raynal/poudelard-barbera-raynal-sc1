import json

def demander_texte(message) :
    texte = ""
    while texte == ""  :
        texte = input(message).strip()
    return texte


def demander_nombre(message, min_val = None, max_val = None) :
    valide = False
    nombre = ""

    while not valide :
        nombre = input(message)
        nombre = nombre.strip()
        valide = True
        i = 0

        if nombre == "" or nombre == "-" :
            valide = False
            print()
            print("Le nombre saisi n'est pas correct")

        while i < len(nombre) and valide :
            if nombre[i] not in "0123456789" :

                if not(nombre[i] == '-' and i == 0) :
                    valide = False

                    print()
                    print("Le nombre saisi n'est pas correct.")

            i += 1

        if min_val != None and valide :
            if int(nombre) < min_val and valide :
                valide = False

                print()
                print("Veuillez entrer un nombre compris entre {} et {}.".format(min_val, max_val))

        if max_val != None and valide:
            if max_val < int(nombre) :
                valide = False

                print()
                print("Veuillez entrer un nombre compris entre {} et {}.".format(min_val, max_val))

    return int(nombre)


def demander_choix(message, options) :
    for i in range(len(options)) :
        message += '\n' + str(i+1) + ". " + options[i]
    message += '\n' + "Votre choix : "

    return options[demander_nombre(message, 1, len(options)) - 1]


def load_fichier(chemin_fichier) :
    with open(chemin_fichier, "r", encoding = "utf-8") as f :
        donnes = json.load(f)
    return donnes


def afficher_texte(texte, sauts_obligatoires = None, longueur_max = None, largeur_max = 150) :
    print()
    liste_mots = texte.split()
    liste_lignes = [liste_mots[0]]

    if sauts_obligatoires == None :
        sauts_obligatoires = []

    i = 1
    while i < len(liste_mots) :

        if liste_mots[i-1] in sauts_obligatoires :

            liste_lignes += [liste_mots[i]]

        elif len(  liste_lignes[len(liste_lignes)-1]) + len(liste_mots[i]) +1 > largeur_max :

            liste_lignes += [liste_mots[i]]

        else :

            liste_lignes[len(liste_lignes)-1] += " "  + liste_mots[i]
        i += 1

    if longueur_max == None :
        for i in liste_lignes :
            print(i)
    else :
        i = 0
        while i < len(liste_lignes) :
            if i%longueur_max == 0 and i != 0 :
                input()
            print(liste_lignes[i])
            i += 1

