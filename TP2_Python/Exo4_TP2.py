import logging

# Configuration du logging
logging.basicConfig(level=logging.INFO)

def harmonic_sum(n):
    # Si n <= 0, interrompons le programme 
    if n <= 0:
        raise ValueError("Le paramètre doit être un entier strictement positif.")

    # Si n = 1
    if n == 1:
        logging.info(f"Calcul de la somme harmonique pour n = {n}")
        return 1, "1"
    else:
        # Si n > 1
        logging.info(f"Calcul de la somme harmonique pour n = {n}")

        # Appel récursif avec n - 1
        nbre_prec, nbre_prec_text = harmonic_sum(n - 1)
        #print(f"Pour n = {n} alors: {nbre_prec}, {nbre_prec_text}")
        # Calcul de la somme actuelle et du texte correspondant
        nbre_actuel = nbre_prec + 1 / n
        nbre_actuel_text = nbre_prec_text + f" + (1/{n})"
        
        #print(f"Pour n = {n}: {nbre_actuel}, {nbre_actuel_text}")
        
        return nbre_actuel, nbre_actuel_text

harmonic_sum(4)
