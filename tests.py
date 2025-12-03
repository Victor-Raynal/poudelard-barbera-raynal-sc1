from chapitres import chapitre_1
from univers import maison
from utils import input_utils

#chapitre_1.lancer_chapitre_1()

def test_bornes (nombre, min_val=None,max_val=None):
    if (min_val is not None and int(nombre) < min_val) or (max_val is not None and int(nombre) > max_val):
        return False
    return True

def test_pas_vide (nombre):
    if nombre == '' :
        return False
    return True

def test_moins (nombre):
    cpt =  0
    for i in nombre :
       if i == '-' :
           cpt+= 1
       if cpt > 1 :
           return False
    if nombre == '' :
        return False
    return True

def test_cara_valides (nombre):
    caracteres_valides = [ord('-'), ord('0'), ord('1'), ord('2'), ord('3'), ord('4'), ord('5'), ord('6'), ord('7'),ord('8'), ord('9')]
    for i in nombre :
        if ord(i) not in caracteres_valides:
            return False
    return True

def demander_nombre (message, min_val = None, max_val = None):
    while True:
        nombre = input(message).strip()
        if test_pas_vide(nombre) :
            if test_moins(nombre) :
                if test_cara_valides(nombre) :
                    if test_bornes(nombre, min_val, max_val):
                        return int(nombre)
        print("Le nombre saisi n'est pas correct.")
    return int(nombre)

demander_nombre('Nombre de -20 à 20 ', -20, 20)
