# %% Import des modules
import random
import re 
import os  # Importer os pour vérifier l'existence des fichiers
import logging

# %%  Creation des fichiers
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
texte = (
    "This change is designed to make annotations in Python more performant and more usable in mostPython circumstances. "
    "The runtime cost for defining annotations Python is minimized, but it Python remains possible to introspect annotations at runtime. "
    "It is usually no longer necessary to enclose annotations in strings if they contain forward references. "
    "The Python new annotationlib module provides tools for inspecting deferred annotations. Annotations Python may be Python evaluated in the "
    "VALUE Python format (which evaluates annotations to runtime values, similar to the behavior in earlier Python versions), "
    "the Python FORWARDREF format (which replaces undefined names with special markers), and Python the STRING format (which returns annotations as strings). "
    "Related changes. The changes in Python 3.14 are designed to rework how __annotations__ works Python at runtime while minimizing breakage to code that contains annotations in source code and to code that reads __annotations__. "
    "However, if you rely Python on undocumented details of the annotation behavior or on private Python functions in the standard library, "
    "there are many ways in which Python your code may not work in Python 3.14. To safeguard your code against Python future changes,Python use only the documented Python functionality."
)

# Fragmenter le texte en phrases
phrases = texte.split('. ')
random.shuffle(phrases)  # Mélanger les phrases pour une distribution aléatoire

def creer_fichiers():
    for i in range(1, 4):
        filename = f"fichier_{i}.txt"
        # Vérifier si le fichier existe déjà
        if os.path.exists(filename):
            logging.info(f"Le fichier '{filename}' existe déjà. Il ne sera pas créé.")
            
            continue  # Passer au fichier suivant

        # Générer un nombre aléatoire de phrases à écrire
        nombre = random.randint(1, len(phrases))
        # Sélectionner des phrases aléatoires
        contenu = '. '.join(phrases[:nombre]) + '.'  # Ajouter un point final

        try:
            # Écrire le contenu dans le fichier
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(contenu.strip())  # Enlever l'espace à la fin
            logging.info(f"Fichier '{filename}' créé avec succès.")
        except Exception as e:
            logging.info(f"Erreur lors de la création du fichier '{filename}': {e}")
# %%  Creation des fichiers

def choisir_fichier():
    essais = 0
    max_essais = 3
    while essais < max_essais:
        filename = input("Entrez le nom du fichier à lire (fichier_1.txt, fichier_2.txt, fichier_3.txt) : ")
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                contenu = file.read()
                # Utiliser une expression régulière pour compter toutes les variations du mot "python"
                count = len(re.findall(r'\bpython\b', contenu, re.IGNORECASE))
                logging.info(f"Le mot 'python' apparaît {count} fois dans le fichier '{filename}'.")
                break
        except FileNotFoundError:
            essais += 1
            logging.info(f"Erreur : le fichier '{filename}' n'a pas été trouvé. Essai {essais}/{max_essais}.")

    if essais == max_essais:
        logging.info("Nombre maximum de tentatives atteint. Le programme va quitter.")