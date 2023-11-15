import pandas as pd
from sklearn.cluster import KMeans
import matplotlib .pyplot as plt

df = pd.read_csv("Partie 3/clusters.csv", delimiter =",")
print(df)

id_film="1"

# Fixe l'index sur l'ID du film
df.set_index('idFilm', inplace=True)

# Recherche de film par ID
def chercher_film_par_id(dataframe, film_id):
    try:
        film = dataframe.loc[film_id]
        return film
    except KeyError:
        print(f"Aucun film trouvé avec l'ID {film_id}")
        return None


# Recherche de films par cluster
def chercher_films_par_cluster(dataframe, cluster):
    try:
        films_du_cluster = dataframe[dataframe['cluster'] == int(cluster)]
        if not films_du_cluster.empty:
            return films_du_cluster
        else:
            print(f"Aucun film trouvé dans le cluster {cluster}")
            return None
    except KeyError:
        print(f"Aucun film trouvé dans le cluster {cluster}")
        return None


# Programme principal
while True:
    id_film = input("Sur quel film voulez-vous faire la recommandation (id) ? (Entrez -1 pour quitter)\n")

    if id_film == "-1":
        break

    film_trouve = chercher_film_par_id(df, int(id_film))

    if film_trouve is not None:
        df_filtre = chercher_films_par_cluster(df,film_trouve["cluster"])
        print(df_filtre)
