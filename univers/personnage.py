def initialiser_personnage(nom, prenom, attributs) :
    personnage = {
                    "Nom" : nom,
                    "Prénom" : prenom,
                    "Argent" : 100,
                    "Inventaire" : [],
                    "Sortilèges" : [],
                    "Attributs" : attributs
                    }
    return personnage


def afficher_personnage(joueur) :

    print("Profil du personnage :")
    print()
    for i in joueur :
        print(i, end = " : ")

        if type(joueur[i]) == dict :
            print()
            for j in joueur[i] :
                print("-", j, ":", joueur[i][j])

        elif type(joueur[i]) == list :

            for j in range(len(joueur[i])) :
                joueur[i][j] = str(joueur[i][j])

            print(", ".join(joueur[i]))

        else :

            print(joueur[i])


def modifier_argent(joueur, montant) :
    joueur["Argent"] += montant


def ajouter_objet(joueur, cle, objet) :
    joueur[cle] += [objet]