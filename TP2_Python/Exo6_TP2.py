import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime

def recuperer_temperature(ville):
    url = f"https://meteofrance.com/previsions-meteo-france/{ville}/75000"
    
    try:
        reponse = requests.get(url)
        reponse.raise_for_status()  # Vérifie si la requête a réussi

        soup = BeautifulSoup(reponse.text, 'html.parser')

        # Chercher toutes les balises <temperature>
        temperatures = soup.findAll('temperature')

        # Obtenir l'heure actuelle
        heure_actuelle = datetime.now().hour

        temperature_actuelle = None

        for temperature in temperatures:
            temperature_text = temperature.text.strip()
            # Chercher l'heure mentionnée dans le texte
            match = re.search(r'(\d+)\s*degrés.*vers\s*(\d+)\s*heures?', temperature_text)
            print("match", match)
            if match:
                temp = match.group(1)
                print("temp",temp)
                heure = int(match.group(2))
                print("heure",heure)
                if heure == heure_actuelle:
                    temperature_actuelle = temp
                    break

        if temperature_actuelle:
            print(f"La température actuelle à {ville} est : {temperature_actuelle} degrés.")
        else:
            print("Impossible de trouver la température pour l'heure actuelle.")

    except requests.exceptions.RequestException:
        print("Échec de la récupération des données. Veuillez réessayer plus tard.")

def main():
    ville = input("Entrez le nom d'une ville (ex. paris) : ")
    recuperer_temperature(ville)

main()
