import logging
from .logger import configurer_logging
from .inputs import obtenir_argent, obtenir_choix, obtenir_mise
from .utils import couleur_nombre, tirage_roulette

# Configurer le logging
configurer_logging()

def jeu_casino():
    """Fonction principale pour le jeu ZCasino."""
    argent = obtenir_argent()
    
    while argent > 0:
        choix = obtenir_choix()
        mise = obtenir_mise(argent)
        
        nombre_roulette = tirage_roulette()
        logging.info(f"La roulette a tiré le nombre : {nombre_roulette} ({couleur_nombre(nombre_roulette)})")

        if choix == nombre_roulette:
            gain = mise * 3
            argent += gain
            logging.info(f"Félicitations ! Vous avez gagné {gain} €. Il vous reste {argent} €. ")
        elif couleur_nombre(choix) == couleur_nombre(nombre_roulette):
            gain = mise * 0.5
            argent += gain
            logging.info(f"Vous avez gagné {gain} €. Il vous reste {argent} €. ")
        else:
            argent -= mise
            logging.info(f"Dommage, vous avez perdu votre mise. Il vous reste {argent} €. ")

        if argent > 0:
            continuer = input("Voulez-vous miser à nouveau ? (oui/non) : ").lower()
            if continuer != 'oui':
                break
        else:
            logging.info("Vous n'avez plus d'argent. Merci d'avoir joué !")
            break

if __name__ == "__main__":
    jeu_casino()
#python -m TP2_Python.main ( si je veux lancer le jeux dans le terminal)