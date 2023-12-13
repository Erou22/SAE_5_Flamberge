# SAE_5_Flamberge
Création d'un système de recommandation 

## .gitignore
__path.py__
``` py
from pathlib import Path

partie_3_path = Path("/home/etuinfo/userIUT/Documents/SAE_5/git/SAE_5_Flamberge/Partie_3/").expanduser().resolve()
```

__connect.py__
``` py
import psycopg2

conn = psycopg2.connect(
    host=host,
    database=database,
    user=user,
    password=password)

clusters_path = "/home/etuinfo/userIUT/Documents/SAE_5/git/SAE_5_Flamberge/Partie_3/clusters.csv"
vecteurs_path = "/home/etuinfo/userIUT/Documents/SAE_5/git/SAE_5_Flamberge/Partie_3/vecteurs.json"
```

## Analyse des données 
Un graphique par fichier :
* __1__ : Nombre de films par année de 2015 à 2020
* __2__ : Nombre de film par genre par année, sur les années 2015, 2017 et 2019 
* __3__ : Proportion des pairs de genres qui sont associées au genre "Drama" sur les années 2015, 2017 et 2019
* __3Bis__ : Nombre de film avec "Documentary" dans les genres du film
* __4__ : Notes moyennes pour tous les genres 

## Base de Données
Fichier sql de la création et du peuplement de la BDD. Il faut le fichier __datasetIMDb.csv__ à la racine du projet 

## Création de la Recommendation via IA
* __IA_vecteur.py__ et __recommandation.py__ sont les 2 scripts qui font une recommandation ! 
* __IA_vecteur__ utilise la similarité entre 2 vecteurs, ici que sur les genres. 
* __Recommandation__ utilise les clusters pour faire la reco. 
* __Donnees.py__ va servir à charger les données depuis la BDD 
* __Cluster.py__ sert à faire les clusters et clusters.csv est le résultat obtenu. 
* __Recherche.py__ sert pour recommandation.py, il fait la recherche du nom de film le plus proche. 

## API 
Données au format __JSON__

### GET
* __/__ : Voit si l'API est en fonctionnement 
* __/recommendations/{id_film}__ : Renvoie la recommandation de plusieurs films pour un identifiant de film donné
* __/recommendations/similarite/{id_film}__ : Renvoie la recommandation de plusieurs films pour un identifiant de film donné utilisant la méthode de similarite
* __/films/__ : Renvoie la liste de tous les films 
* __/films/{id_film}__ : Renvoie le film lié à l'identifiant donné
* __/films/{id_film}/fiche__ : Renvoie la fiche complète du film lié à l'identifiant donné (Info base + acteurs + realisateurs + autres personnes liées)
* __/films/acteur/{id_acteur}__ : Renvoie les films où a joué l'acteur donné
* __/films/realisateur/{id_realisateur}__ : Renvoie les films qui ont été réalisés le réalisateur donné
* __/films/genre/{nom_genre}__ : Renvoie tous les films pour un genre donné
* __/films/recherche/{titre}__ : Renvoie des films qui ont un titre proche du titrre donné
* __/acteurs/{id_film}__ : Renvoie les acteurs d'un film 
* __/realisateurs/{id_film}__ : Renvoie les réalisateurs d'un film