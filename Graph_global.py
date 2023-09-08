# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


"""NOMBRE DE FILMS PAR ANNEE"""

import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from itertools import combinations

# Charger les données en spécifiant le séparateur ";"
data = pd.read_csv("/home/etuinfo/maallain/Documents/SAE/Graph/datasetIMDb.csv", sep=";")


# Supprimer les doublons de films en se basant sur le titre du film
data_unique = data.drop_duplicates(subset='nomFilm')

# Compter le nombre de films par année
film_count_by_year = data_unique.groupby('annee').size().reset_index(name='nombre_de_films')

# Afficher le graphique à barres
plt.figure(figsize=(12, 6))  # Réglage de la taille du graphique
plt.bar(film_count_by_year['annee'], film_count_by_year['nombre_de_films'])
plt.xlabel('Année')
plt.ylabel('Nombre de films')
plt.title('Nombre de films par année (films uniques)')
plt.xticks(rotation=45)  # Faire pivoter les étiquettes de l'axe des x pour une meilleure lisibilité
plt.show()

"""GENRES SUR 2015/2017/2019"""

# Filtrer les données pour les années 2015, 2017 et 2019
years_of_interest = [2015, 2017, 2019]
filtered_data = data_unique[data_unique['annee'].isin(years_of_interest)]

# Diviser les genres multiples en genres individuels
filtered_data['genres'] = filtered_data['genres'].str.split(',')

# Utiliser la fonction explode pour diviser les listes de genres en plusieurs lignes
filtered_data = filtered_data.explode('genres')

# Créer un tableau croisé dynamique (pivot table) pour compter le nombre de films de chaque genre pour chaque année
pivot_table = filtered_data.pivot_table(index='annee', columns='genres', aggfunc='size', fill_value=0)


# Utiliser la palette de couleurs automatique
ax = pivot_table.plot(kind='bar', colormap='tab20')

plt.xlabel('Année')
plt.ylabel('Nombre de films')
plt.title('Nombre de films par genre par année')
plt.xticks(rotation=0)  # Réinitialiser la rotation des étiquettes de l'axe des x
plt.legend(title='Genre', bbox_to_anchor=(1.05, 1), loc='upper left')  # Légende
plt.show()

"""COUPLE DE GENRES (DRAMA/XX) SUR 2017"""

# Diviser les genres multiples en genres individuels
data_drama = data['genres'].str.split(',')

# Créer un compteur de paires de genres
pair_counts = Counter()

# Parcourir chaque film
for genres in data_drama:
    # Vérifier si "Drama" est présent dans la liste des genres du film
    if "Drama" in genres:
        # Générer toutes les combinaisons de paires de genres possibles pour ce film
        pairs = combinations(genres, 2)
        # Filtrer les paires de genres pour inclure uniquement celles avec "Drama"
        pairs_with_drama = [pair for pair in pairs if "Drama" in pair]
        # Mettre à jour le compteur avec les paires de genres de ce film
        pair_counts.update(pairs_with_drama)

# Sélectionner les paires de genres les plus fréquentes (par exemple, les 10 premières)
top_pairs = pair_counts.most_common(15)

# Extraire les paires de genres et leurs comptages
pairs, counts = zip(*top_pairs)

# Créer un diagramme circulaire pour les paires de genres
plt.figure(figsize=(8, 8))  # Réglage de la taille du graphique
plt.pie(counts, labels=pairs, autopct='%1.1f%%', startangle=140)
plt.title('Paires de Genres Associées à "Drama"')
plt.show()



