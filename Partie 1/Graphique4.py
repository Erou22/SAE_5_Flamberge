import matplotlib.pyplot as plt
from Data import data


# Supprimer les doublons de films en se basant sur le titre du film
data_unique = data.drop_duplicates(subset='nomFilm')

# Filtrer les données pour les années 2017
filtered_data = data_unique[data_unique['annee'].isin([2017])]

# Diviser les genres multiples en genres individuels
filtered_data['genres'] = filtered_data['genres'].str.split(',')

# Utiliser la fonction explode pour diviser les listes de genres en plusieurs lignes
filtered_data = filtered_data.explode('genres')

# Filtrer les lignes avec '\N' dans la colonne 'note'
filtered_data = filtered_data[filtered_data['note'] != '\\N']
filtered_data = filtered_data[filtered_data['genres'] != '\\N']

print(filtered_data)

# Convertir la colonne 'note' en type float
filtered_data['note'] = filtered_data['note'].astype(float)

filtered_data = filtered_data[filtered_data['note'] >= 0]

# Calculer la moyenne des notes par genre
moyenne_par_genre = filtered_data.groupby('genres')['note'].mean().reset_index()

# Créer un graphique à barres pour afficher les notes moyennes par genre
plt.figure(figsize=(12, 6))

plt.bar(moyenne_par_genre['genres'], moyenne_par_genre['note'])
plt.xlabel('Genres')
plt.ylabel('Average score')
plt.title('Average score by genres')
plt.xticks(rotation=45, ha='right')

plt.show()
