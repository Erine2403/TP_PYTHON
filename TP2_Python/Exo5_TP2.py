import random

def couleur_nombre(nombre):
    """Retourne la couleur du nombre."""
    return 'noir' if nombre % 2 == 0 else 'blanc'

def jeu_zcasino():
    """Fonction principale pour le jeu ZCasino."""
    argent = float(input("Entrez la somme d'argent avec laquelle vous souhaitez jouer : "))
    
    while argent > 0:
        # Choix du nombre
        try:
            choix = int(input("Choisissez un nombre entre 0 et 49 : "))
            if choix < 0 or choix > 49:
                print("Veuillez choisir un nombre valide.")
                continue
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            continue
        
        # Mise
        try:
            mise = float(input("Entrez votre mise : "))
            if mise <= 0 or mise > argent:
                print("Veuillez entrer une mise valide.")
                continue
        except ValueError:
            print("Veuillez entrer une mise valide.")
            continue
        
        # Tirage de la roulette
        nombre_roulette = random.randint(0, 49)
        print(f"La roulette a tiré le nombre : {nombre_roulette} ({couleur_nombre(nombre_roulette)})")

        # Vérification des gains
        if choix == nombre_roulette:
            gain = mise * 3
            argent += gain
            print(f"Félicitations ! Vous avez gagné {gain} €. Il vous reste {argent} €.")
        elif couleur_nombre(choix) == couleur_nombre(nombre_roulette):
            gain = mise * 0.5
            argent += gain
            print(f"Vous avez gagné {gain} €. Il vous reste {argent} €.")
        else:
            argent -= mise
            print(f"Dommage, vous avez perdu votre mise. Il vous reste {argent} €.")

        # Option de rejouer
        if argent > 0:
            continuer = input("Voulez-vous miser à nouveau ? (oui/non) : ").lower()
            if continuer != 'oui':
                break
        else:
            print("Vous n'avez plus d'argent. Merci d'avoir joué !")
            break


jeu_zcasino()
