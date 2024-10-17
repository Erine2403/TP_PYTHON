# Les sorties 
import random

def couleur_nombre(nombre):
    """Retourne la couleur du nombre."""
    return 'noir' if nombre % 2 == 0 else 'blanc'

def tirage_roulette():
    """Tire un nombre aléatoire entre 0 et 49."""
    return random.randint(0, 49)
