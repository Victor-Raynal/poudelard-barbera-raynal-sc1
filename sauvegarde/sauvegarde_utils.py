from utils import input_utils
import json

def load_sauvegarde() :
    dico_sauvegarde = input_utils.load_fichier("sauvegarde/fichier_sauvegarde.json")
    if dico_sauvegarde == {} :
        return None, None, None
    return dico_sauvegarde["chapitre"], dico_sauvegarde["joueur"], dico_sauvegarde["maisons"]


def sauvegarder(chapitre, joueur, maisons) :
    dico_sauvegarde = {"chapitre" : chapitre, "joueur" : joueur, "maisons" : maisons}
    with open("sauvegarde/fichier_sauvegarde.json", "w") as f :
        json.dump(dico_sauvegarde, f)