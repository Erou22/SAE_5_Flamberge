import pandas as pd
import distance

df = pd.read_csv("Partie 3/clusters.csv", delimiter =",")
# print(df)

def chercher_film_par_titre(dataframe, titre):
    try:
        dataframe["contains"] = dataframe["titre"].str.contains(titre, case=False)
        films = dataframe[dataframe["contains"] == True]
        films['distance_edit'] = films['titre'].apply(lambda x: distance.levenshtein(titre, str(x)))
        return films.sort_values(by=['distance_edit']).head(5)
    except KeyError:
        print(f"Aucun film trouvé avec le titre {titre}")
        return None

while True:
    titre = input("Sur quel film voulez-vous faire la recommandation (titre) ? (Entrez -1 pour quitter)\n")

    if titre == "-1":
        break
    
    film_trouve = chercher_film_par_titre(df, titre)
    
    if film_trouve is not None:
        print(film_trouve)
        