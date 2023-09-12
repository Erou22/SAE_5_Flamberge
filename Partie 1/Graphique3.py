import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from itertools import combinations
from Data import data

# Supprimer les doublons de films en se basant sur le titre du film
data_unique = data.drop_duplicates(subset='nomFilm')

def graphique_couple(nom_genre:str, year:list, nombre_afficher:int) :

    # Filtrer les données pour les années 2015, 2017 et 2019
    years_of_interest = year
    filtered_data = data_unique[data_unique['annee'].isin(years_of_interest)]

    # Diviser les genres multiples en genres individuels
    data_genre = filtered_data['genres'].str.split(',')

    # Créer un compteur de paires de genres
    pair_counts = Counter()

    # Parcourir chaque film
    for genres in data_genre:
        # Vérifier si le genre est présent dans la liste des genres du film
        if nom_genre in genres:
            # Générer toutes les combinaisons de paires de genres possibles pour ce film
            pairs = combinations(genres, 2)
            # Filtrer les paires de genres pour inclure uniquement celles avec le genre
            pairs_with_genre = [pair for pair in pairs if nom_genre in pair]
            # Mettre à jour le compteur avec les paires de genres de ce film
            pair_counts.update(pairs_with_genre)

    # Sélectionner les paires de genres les plus fréquentes (par exemple, les 10 premières)
    top_pairs = pair_counts.most_common()
    top_pairs = pd.DataFrame.from_records(list(dict(top_pairs).items()), columns=['Genres','counts'])

    #the top xx
    final_df = top_pairs[:nombre_afficher].copy()

    print(len(top_pairs))

    if (len(top_pairs) > nombre_afficher) :
        #others
        new_row = pd.DataFrame(data = {
            'Genres' : ['others'],
            'counts' : [top_pairs['counts'][nombre_afficher:].sum()]
        })

        #combining the top xx with others
        final_df = pd.concat([final_df, new_row])

    # Créer un diagramme circulaire pour les paires de genres
    plt.figure(figsize=(8, 8))  # Réglage de la taille du graphique
    plt.pie(final_df["counts"], labels=final_df["Genres"], autopct='%1.1f%%', startangle=140)
    plt.title(f'Paires de Genres Associées à "{nom_genre}"')
    plt.show()


# Drama,2017,11
# Documentary,2017,9
# Adult",[2015],11
graphique_couple("Documentary",[2017],11)
