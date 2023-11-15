import Donnees as data
import pandas as pd
from kmodes.kprototypes import KPrototypes
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# Chargement des données

dfGenres = data.films_genres.groupby('idFilm')['nomGenre'].agg(list).reset_index()

# Trier les genres par ordre alphabétique
dfGenres['nomGenre'] = dfGenres['nomGenre'].apply(lambda x: sorted(x))

# Convertir la liste de genres en chaîne de caractères
dfGenres['nomGenre'] = dfGenres['nomGenre'].apply(lambda x: ','.join(x))

dftout = pd.merge(data.films, dfGenres, on='idFilm')

# Sélectionner les colonnes pertinentes pour le clustering
df = dftout[['titre', 'note', 'nomGenre']]

# Centrer et réduire les colonnes numériques
scaler = StandardScaler()
df[['note']] = scaler.fit_transform(df[['note']])

# Convertir le DataFrame en array
data_array = df.values

# Colonnes catégorielles
cat_columns = [0, 2]

# Choisir le nombre de clusters
n_clusters = 10

# Effectuer le clustering avec K-prototype
kproto = KPrototypes(n_clusters=n_clusters, init='Cao', n_init=1, verbose=2, random_state=42)
clusters = kproto.fit_predict(data_array, categorical=cat_columns)

# Choosing optimal K
# cost = []
# for i in range(2, 10):
#     kproto = KPrototypes(n_clusters=i, init='Cao', n_init=1, verbose=2, random_state=42)
#     kproto.fit_predict(data_array, categorical=cat_columns)
#     cost.append(kproto.cost_)

# # Plot the elbow curve
# plt.plot(range(2, 10), cost, marker='o')
# plt.xlabel('Number of clusters (K)')
# plt.ylabel('Inertia (Cost)')
# plt.title('Elbow Method for Optimal K')
# plt.show()

# Ajouter les clusters au DataFrame original
dftout['cluster'] = clusters

# Sauvegarder les clusters dans un fichier CSV
dftout.to_csv('Partie 3/clusters.csv', index=False)