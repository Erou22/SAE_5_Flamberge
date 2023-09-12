import pandas as pd
import matplotlib.pyplot as plt
from Data import data

# Supprimer les doublons de films en se basant sur le titre du film
data_unique = data.drop_duplicates(subset='nomFilm')

# Filtrer les données pour l'année 2017
filtered_data = data_unique[data_unique['annee'].isin([2017])]

dico = {}

genre = "Documentary"
nb_genre= 10

for i in filtered_data['genres']:
    if genre in i :
        if str(i) in dico :
            dico[str(i)]+=1
        else :
            dico[str(i)]=1

print(len(dico))
dico = {k: v for k, v in sorted(dico.items(),reverse=True ,key=lambda item: item[1])}

df_dico = pd.DataFrame.from_dict(dico, orient='index')


# Afficher le graphique à barres
plt.figure(figsize=(12, 6))  # Réglage de la taille du graphique
plt.bar(df_dico.head(nb_genre).index, df_dico.head(nb_genre)[0])
plt.xlabel('Types')
plt.ylabel('Number of films in the genre')
plt.title(f'Number of films with "{genre} in the genre"')
plt.xticks(rotation=60)  # Faire pivoter les étiquettes de l'axe des x pour une meilleure lisibilité
plt.show()
