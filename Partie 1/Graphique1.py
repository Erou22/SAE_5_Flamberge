import matplotlib.pyplot as plt
from Data import data

# Supprimer les doublons de films en se basant sur le titre du film
data_unique = data.drop_duplicates(subset='nomFilm')

# Compter le nombre de films par année
film_count_by_year = data_unique.groupby('annee').size().reset_index(name='nombre_de_films')

# Afficher le graphique à barres
plt.figure(figsize=(12, 6))  # Réglage de la taille du graphique
plt.plot(film_count_by_year['annee'], film_count_by_year['nombre_de_films'], marker='o', linestyle='solid')
plt.xlabel('Année')
plt.ylabel('Nombre de films')
plt.title('Nombre de films par année (films uniques)')
plt.xticks(rotation=45)  # Faire pivoter les étiquettes de l'axe des x pour une meilleure lisibilité
plt.show()