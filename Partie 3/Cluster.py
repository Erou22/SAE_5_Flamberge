import Donnees as data
import pandas as pd
from kmodes.kprototypes import KPrototypes
import matplotlib.pyplot as plt

# Chargement des données
df = data.films_genres

from sklearn.preprocessing import StandardScaler

# Select relevant columns for clustering (excluding 'annee')
df = data.films_genres[['titre', 'note', 'nbVotes', 'nomGenre']]

# Standardize numerical columns
scaler = StandardScaler()
df[['note', 'nbVotes']] = scaler.fit_transform(df[['note', 'nbVotes']])

# Convert DataFrame to array for K-prototype
data_array = df.values

# Specify categorical column indices
cat_columns = [0, 3]  # Assuming 'titre' and 'nomGenre' are categorical columns

# Choose the number of clusters (replace n_clusters with your desired number)
n_clusters = 10

# Perform clustering with K-prototype
kproto = KPrototypes(n_clusters=n_clusters, init='Cao', n_init=5, verbose=2, random_state=42)
clusters = kproto.fit_predict(data_array, categorical=cat_columns)

# Add the cluster labels to the original DataFrame
data.films_genres['cluster'] = clusters

# Display the resulting DataFrame with cluster labels
print(data.films_genres[['titre', 'note', 'nbVotes', 'nomGenre', 'cluster']])

# Save the resulting DataFrame to a CSV file
data.films_genres.to_csv('clusters.csv', index=False)