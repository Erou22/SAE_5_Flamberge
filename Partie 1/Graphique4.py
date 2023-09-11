import matplotlib.pyplot as plt
from Data import data

# Supprimer les doublons de films en se basant sur le titre du film
data_unique = data.drop_duplicates(subset='nomFilm')

# Filtrer les données pour les années 2015, 2017 et 2019
filtered_data = data_unique[data_unique['annee'].isin([2015, 2017, 2019])]

# Diviser les genres multiples en genres individuels
filtered_data['genres'] = filtered_data['genres'].str.split(',')

# Utiliser la fonction explode pour diviser les listes de genres en plusieurs lignes
filtered_data = filtered_data.explode('genres')
