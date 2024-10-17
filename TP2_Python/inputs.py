import logging

def obtenir_argent():
    """Demande combien d'argent il souhaite jouer."""
    while True:
        try:
            argent = float(input("Entrez la somme d'argent avec laquelle vous souhaitez jouer : "))
            return argent
        except ValueError:
            logging.warning("Entrée invalide : veuillez entrer un nombre valide.")

def obtenir_choix():
    """Demande de choisir un nombre entre 0 et 49."""
    while True:
        try:
            choix = int(input("Choisissez un nombre entre 0 et 49 : "))
            if 0 <= choix <= 49:
                return choix
            else:
                logging.warning("Entrée invalide : veuillez choisir un nombre valide.")
        except ValueError:
            logging.warning("Entrée invalide : veuillez entrer un nombre valide.")

def obtenir_mise(argent):
    """Demande à l'utilisateur de saisir une mise valide."""
    while True:
        try:
            mise = float(input("Entrez votre mise : "))
            if 0 < mise <= argent:
                return mise
            else:
                logging.warning("Entrée invalide : veuillez entrer une mise valide.")
        except ValueError:
            logging.warning("Entrée invalide : veuillez entrer une mise valide.")
