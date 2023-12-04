import Donnees as data
import pandas as pd
from kmodes.kprototypes import KPrototypes
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Chargement des données
df = data.films_genres

# Select relevant columns for clustering (excluding 'annee')
df = data.films_genres[['note', 'nomGenre']]

# Standardize numerical columns
scaler = StandardScaler()
df[['note']] = scaler.fit_transform(df[['note']])

# Convert DataFrame to array for K-prototype
data_array = df.values

# Specify categorical column indices
cat_columns = [1]  # Assuming 'titre' and 'nomGenre' are categorical columns

# Choosing optimal K
cost = []
for i in range(2, 10):
    kproto = KPrototypes(n_clusters=i, init='Cao', n_init=2, verbose=2, random_state=42)
    kproto.fit_predict(data_array, categorical=cat_columns)
    cost.append(kproto.cost_)

# Plot the elbow curve
plt.plot(range(2, 10), cost, marker='o')
plt.xlabel('Number of clusters (K)')
plt.ylabel('Inertia (Cost)')
plt.title('Elbow Method for Optimal K')
plt.show()


# # Choose the number of clusters (replace n_clusters with your desired number)
# n_clusters = 10

# # Perform clustering with K-prototype
# kproto = KPrototypes(n_clusters=n_clusters, init='Cao', n_init=2, verbose=2, random_state=42)
# clusters = kproto.fit_predict(data_array, categorical=cat_columns)

# # Add the cluster labels to the original DataFrame
# data.films_genres['cluster'] = clusters

# # Save the resulting DataFrame to a CSV file
# data.films_genres.to_csv('Partie 3/clusters.csv', index=False)