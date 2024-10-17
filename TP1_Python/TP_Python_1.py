# %% Import des modules
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# %% Lecture des fichiers

#Lecture du fichier cities
df_cities = pd.read_csv(r"C://Users//ErineZANO//Documents//TP PYTHON BROUILLON/cities.csv")
print(df_cities.head())
#Lecture du fichier population#### 
df_population=pd.read_csv(r"C://Users//ErineZANO//Documents//TP PYTHON BROUILLON/Population_data.csv")
print (print(df_population.head()))

# %% QUESTION 1 : Ajouter une colonne "Latitude totale" et "Longitude totale" dans le fichier cities.csv############
df_cities['Latitude totale'] = 0.0
df_cities['Longitude totale'] = 0.0
print(df_cities.head())

#Calculons la latitude totale et ajoutons là au fichier pandas ##########################
'Affichons les columns en amont'
print(df_cities.columns)
#Renommons les colonnes en enlevant les espaces et guillemets######
df_cities.columns = df_cities.columns.str.replace('"', '').str.strip()
print(df_cities.columns)
# %% Calculons la latitude totale
df_cities['Latitude totale'] = (
    df_cities['LatD'] + 
    (df_cities['LatM'] / 60) + 
    (df_cities['LatS'] / 3600)
)
print(df_cities.head())
# Calculons la longitude totale
df_cities['Longitude totale'] = (
    df_cities['LonD'] + 
    (df_cities['LonM'] / 60) + 
    (df_cities['LonS'] / 3600)
)
print(df_cities.head())

# %% QUESTION 2 :  Filtrer les villes situées dans l'hémisphère Nord####

" Affichons d'abord les valeur de la colonne NS"
df_cities['NS'].values
#On va remplacer les valeurs de la colonnes "N" par N
df_cities['NS'] = df_cities['NS'].str.replace('"', '').str.strip()
print(df_cities['NS'][0])
"Mise des villes de l'hemisphère nord dans un dataFrame "
villes_hemisphere_nord = df_cities[df_cities['NS'] == 'N']
print(villes_hemisphere_nord.head())
print(villes_hemisphere_nord["City"].values)

# %% QUESTION 3 : Fusionner les deux DataFrames sur la colonne "City"###############
df_cities['City'] = df_cities['City'].str.strip()
df_population['City'] = df_population['City'].str.strip()
merged_df = pd.merge(df_cities, df_population, on='City', how='left')
print(merged_df)
# %% QUESTION 4 :Calculer la population projetée pour 2025
merged_df['Population_2025'] = merged_df['Population_2020'] * (1 + merged_df['Growth_rate'] / 100) ** 5
print(merged_df[['City', 'Population_2020', 'Growth_rate', 'Population_2025']])
# %% QUESTION 5 : Afficher les villes avec une population projetée supérieure à 1 million en 2025
cities_sup_million = merged_df[merged_df['Population_2025'] > 1000000]

# Afficher les résultats
print(cities_sup_million[['City', 'Population_2025']], "le nombre total de villes est :", cities_sup_million.shape[0])

# %% QUESTION 6 : Créer un graphique de la population projetée pour 2025
'Trions les villes par Population_2025 et sélectionner les 10 plus élevées'
top_10_cities = merged_df.nlargest(10, 'Population_2025')

'Créons le graphique à barres horizontales'
plt.figure(figsize=(12, 6))
plt.barh(top_10_cities['City'], top_10_cities['Population_2025'], color='RED')

'Ajoutons des titres et des labels'
plt.title('Top 10 Villes par Population Projetée en 2025')
plt.xlabel('Population Projetée')
plt.ylabel('Villes')
'Affichons le graphique'
plt.tight_layout()
plt.show()
# %% QUESTION 7 : Calculer la densité de population des villes
np.random.seed(0)
merged_df['Area'] = np.random.randint(50, 2001, size=len(merged_df))
merged_df['Densité_population'] = merged_df['Population_2025'] / merged_df['Area']
print(merged_df[['City', 'Population_2025', 'Area', 'Densité_population']])
# %% QUESTION 8 :  Trouver la ville avec la plus grande et la plus petite population
"l'indice de la ville avec la plus grande population en 2025 "
ville_max_population = merged_df.loc[merged_df['Population_2025'].idxmax()]

"l'indice de la ville avec la plus petite population"
ville_min_population = merged_df.loc[merged_df['Population_2025'].idxmin()]

print("Ville avec la plus grande population en 2025 :")
print(ville_max_population[['City', 'Population_2025']])

print("\nVille avec la plus petite population en 2025:")
print(ville_min_population[['City', 'Population_2025']])
# %% QUESTION 9 :  Filtrer les villes avec une densité de population supérieure à 5000 habitants/km²
villes_haute_densite = merged_df[merged_df['Densité_population'] > 5000]
print(villes_haute_densite[['City', 'Densité_population']], "le nombre total de villes est :", villes_haute_densite.shape[0])

# %% QUESTION 10 :  Trouver la moyenne et la médiane de la population des villes
'Calculons la moyenne de la population'
moyenne_population = merged_df['Population_2025'].mean()

'Calculons la médiane de la population'
mediane_population = merged_df['Population_2025'].median()
' Affichons les résultats'
print(f"Moyenne de la population des villes : {moyenne_population:.3f}")
print(f"Médiane de la population des villes : {mediane_population:.3f}")
# %% QUESTION 11 :Créer une nouvelle colonne pour la population normalisée
' Calculons les valeurs min et max de la population'
min_population = merged_df['Population_2025'].min()
max_population = merged_df['Population_2025'].max()

'Normalisons les valeurs de la population'
merged_df['Population_normalisée'] = (merged_df['Population_2025'] - min_population) / (max_population - min_population)

'Affichons les résultats'
print(merged_df[['City', 'Population_2025', 'Population_normalisée']])

# %% QUESTION 12 :Utiliser NumPy pour créer un tableau de statistiques descriptive
population = merged_df['Population_2025'].to_numpy()

'Calculons les statistiques descriptives'
moyenne = np.mean(population)
ecart_type = np.std(population)
minimum = np.min(population)
maximum = np.max(population)

'Créeons un tableau de statistiques sous forme de dictionnaire'
statistiques = {
    'Moyenne': moyenne,
    'Écart-type': ecart_type,
    'Minimum': minimum,
    'Maximum': maximum
}
'Transformons le dictionnaire en DataFrame'
statistiques_df = pd.DataFrame(statistiques, index=[0])
print(statistiques_df)

'Transformer le dictionnaire en tableau NumPy'
statistiques_array = np.array(list(statistiques.values()))

'Affichons le tableau NumPy des statistiques'
print(statistiques_array)
'Ajoutons à présent le fichier sur git '