import matplotlib.pyplot as plt
from collections import Counter
from itertools import combinations
from Data import data

# Supprimer les doublons de films en se basant sur le titre du film
data_unique = data.drop_duplicates(subset='nomFilm')

# Filtrer les données pour l'année 2017
filtered_data = data_unique[data_unique['annee'].isin([2017])]

# Diviser les genres multiples en genres individuels
data_drama = filtered_data['genres'].str.split(',')

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
plt.title('Paires de Genres Associées à "Drama" en 2017')
plt.show()