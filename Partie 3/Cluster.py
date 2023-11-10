import Donnees as data
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib .pyplot as plt

#Clustering

df_safe=data.films_genres
df_safe = df_safe[df_safe.columns [:18]]

model = KMeans( n_clusters =6)

model.fit(df_safe)

"""
K = [i for i in range(2, 10)]
list_inertie=[]
for i in K :
    list_inertie.append(KMeans(n_clusters =i).fit(df).inertia_)

plt.plot(K, list_inertie)
plt.show ()
"""
print(model.labels_)
print(model.inertia_)

for i in range(6) :
    print("Cluster :",i)
    dfit = df_safe[model.labels_==i].head(10)
    print(dfit[['name','nomGenre','note']])