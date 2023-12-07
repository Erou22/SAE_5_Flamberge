# SAE_5_Flamberge
Création d'un système de recommandation 

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

* __/__ : Voit si l'API est en fonctionnement 
* __/recommendations/{item_id}__ : La recommandation de plusieurs films pour un identifiant de film donné
* __/films/__
* __/films/{item_id}__
* __/films/acteur/{item_id}__
* __/films/realisateur/{item_id}__
* __/filmComplet/{item_id}__
* __/genres/{nom_genre}__
* __/acteurs/{item_id}__
* __/realisateur/{item_id}__