#début du chapitre 3
#on va faire les cours et la découverte de poudlard
import random
from utils import input_utils

def pool_sorts (data) :
    Nombre_sorts = len(data)
    l_sorts_off = []
    l_sorts_def = []
    l_sorts_util = []
#on distingue les différents pools de sorts disponibles
    for id_sort in range(Nombre_sorts):
        if data[id_sort]['type'] == 'Offensif' :
            l_sorts_off.append(id_sort)
        elif data[id_sort]['type'] == 'Défensif' :
            l_sorts_def.append(id_sort)
        elif data[id_sort]['type'] == 'Utilitaire' :
            l_sorts_util.append(id_sort)
    return (l_sorts_off, l_sorts_def, l_sorts_util)

def apprendre_sorts (l_pool_sorts,data) :
    sorts_appris = []
    sorts_appris.append(data[random.choice(l_pool_sorts[0])])
    sorts_appris.append(data[random.choice(l_pool_sorts[1])])
    for i in range (3) :
        sorts_appris.append(data[random.choice(l_pool_sorts[2])])
    return sorts_appris

def dialogue(sorts_appris) :
    print ("Tu commences tes études à Poudlard...")
    #faut mettre un time ici
    for i in range(len(sorts_appris)) :
        print("Tu viens d'apprendre le sortilège : {} ({}) ".format(sorts_appris[i]['nom'], sorts_appris[i]['type']))
        #time ici
        input("Appuie sur la touche Entrée pour continuer...")
    print('\n', 'Tu as terminé ton apprentissage de base à Poudlard !')
    #time ici
    print('voici les sortilèges que tu maîtrises désormais : ', '\n')
    for i in range(len(sorts_appris)) :
        print ('- {} ({}) : {}'.format(sorts_appris[i]['nom'], sorts_appris[i]['type'], sorts_appris[i]['description']))
        #time ici

def quiz_magie(joueur, chemin_fichier = '../data/quiz_magie.json') :
    quiz = input_utils.load_fichier(chemin_fichier)
    print('\n', "Bienvenu au quiz de magie de poudlard !", '\n',"Réponds correctementaux 4 questions pour faire gagner des points à ta maison. ")
    compteur_de_points = 0
    l_questions = []
    print(quiz)
    for i in range (4) :
        seed = random.randint(0, len(quiz)-1)
        while seed in l_questions :
            seed = random.randint(0, len(quiz)-1)
        l_questions.append(seed)
        question = quiz[seed]['question']
        reponse = quiz[seed]['reponse']
        print("{}. {}".format(i,question).strip().lower())
        reponse_util = input('>')
        if reponse_util  != reponse.lower():
            print('Mauvaise réponse. La bonne réponse était : {}'.format(reponse))
        else :
            compteur_de_points += 1
            print('Bonne réponse ! +25 points pour ta maison.')




def chap3(joueur, chemin_fichier = "../data/sorts.json"):
    data = input_utils.load_fichier(chemin_fichier)
    print('f1')
    l_pool_sorts = pool_sorts(data)
    print('f2')
    sorts_appris = apprendre_sorts(l_pool_sorts,data)
    print('f3')
    '''
    for i in range (len(sorts_appris)) :
        joueur['Sortilèges'].append(sorts_appris[i]['nom'])'''
    dialogue(sorts_appris)
    print('f4')
    quiz_magie(joueur)
# A activer quand faudra jouer au jeu. désactiver pour tester localement les fonctions


chap3('a', '../data/sorts.json')