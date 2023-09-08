import pandas as pd
import matplotlib.pyplot as plt

# Charger les données en spécifiant le séparateur ";"
data = pd.read_csv("/home/etuinfo/efertray/Documents/SAE/datasetIMDb.csv", sep=";")

# Supprimer les doublons de films en se basant sur le titre du film
data_unique = data.drop_duplicates(subset='nomFilm')

# Filtrer les données pour les années 2015, 2017 et 2019
filtered_data = data_unique[data_unique['annee'].isin([2015, 2017, 2019])]

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