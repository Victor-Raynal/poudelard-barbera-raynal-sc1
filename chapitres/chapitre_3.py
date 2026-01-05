import random
from univers import personnage
from utils import input_utils
from univers import maison

def pool_sorts (data) :
    Nombre_sorts = len(data)
    l_sorts_off = []
    l_sorts_def = []
    l_sorts_util = []

    for id_sort in range(Nombre_sorts):
        if data[id_sort]['type'] == 'Offensif' :
            l_sorts_off.append(id_sort)
        elif data[id_sort]['type'] == 'Défensif' :
            l_sorts_def.append(id_sort)
        elif data[id_sort]['type'] == 'Utilitaire' :
            l_sorts_util.append(id_sort)
    return l_sorts_off, l_sorts_def, l_sorts_util

def apprendre_sorts (joueur, chemin_fichier = 'data/sorts.json') :
    data = input_utils.load_fichier(chemin_fichier)
    l_pool_sorts = pool_sorts(data)
    sorts_appris = []
    sorts_appris.append(data[random.choice(l_pool_sorts[0])])
    sorts_appris.append(data[random.choice(l_pool_sorts[1])])
    for i in range (3) :
        sorts_appris.append(data[random.choice(l_pool_sorts[2])])
    for i in range (len(sorts_appris)) :
        joueur['Sortilèges'].append(sorts_appris[i]['nom'])
    dialogue(sorts_appris)

def dialogue(sorts_appris) :
    print ("Tu commences tes études à Poudlard...")
    for i in range(len(sorts_appris)) :
        print("Tu viens d'apprendre le sortilège : {} ({}) ".format(sorts_appris[i]['nom'], sorts_appris[i]['type']))

        input("Appuie sur la touche Entrée pour continuer...")
    print('\n', 'Tu as terminé ton apprentissage de base à Poudlard !')
    print('voici les sortilèges que tu maîtrises désormais : ', '\n')
    for i in range(len(sorts_appris)) :
        print ('- {} ({}) : {}'.format(sorts_appris[i]['nom'], sorts_appris[i]['type'], sorts_appris[i]['description']))

def quiz_magie(joueur, chemin_fichier = 'data/quiz_magie.json') :
    quiz = input_utils.load_fichier(chemin_fichier)
    print('\n', "Bienvenu au quiz de magie de poudlard !", '\n',"Réponds correctementaux 4 questions pour faire gagner des points à ta maison. ")
    compteur_de_points = 0
    l_questions = []
    for i in range (4) :
        seed = random.randint(0, len(quiz)-1)
        while seed in l_questions :
            seed = random.randint(0, len(quiz)-1)
        l_questions.append(seed)
        question = quiz[seed]['question']
        reponse = quiz[seed]['reponse']
        print("{}. {}".format(i+1,question).strip())
        reponse_util = input('> ')
        if reponse_util.lower().strip()  != reponse.lower().strip() :
            print('Mauvaise réponse. La bonne réponse était : {}'.format(reponse))
        else :
            compteur_de_points += 25
            print('Bonne réponse ! +25 points pour ta maison.')
    print('Score obtenu : {} points'.format(compteur_de_points))
    joueur['Score'] = compteur_de_points


def lancer_chapitre_3(joueur, maisons):
    apprendre_sorts(joueur, chemin_fichier='data/sorts.json')
    quiz_magie(joueur,chemin_fichier='data/quiz_magie.json')
    maison.actualiser_points_maison(maisons,joueur['Maison'], joueur['Score'])
    maison.afficher_maison_gagnante(maisons)
    personnage.afficher_personnage(joueur)

