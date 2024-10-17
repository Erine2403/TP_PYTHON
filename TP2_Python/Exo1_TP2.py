# Import des modules

import random
import re 
import os  # Importer os pour vérifier l'existence des fichiers
import logging

# %% EXO 1

def devine_le_nombre():
    nombre_secret = random.randint(1, 100)
    essais = 0
    print(" Un nombre a été choisi entre 1 et 100.")

    while True:
        try:
            # l'utilisateur doit faire une proposition
            proposition = int(input("Faites votre proposition : "))
            essais += 1

            if proposition < nombre_secret:
                print("Trop petit !")
            elif proposition > nombre_secret:
                print("Trop grand !")
            else:
                print(f"Bravo ! Vous avez trouvé le nombre {nombre_secret} en {essais} essais.")
                break
        except ValueError:
            print("Veuillez entrer un nombre valide.")
