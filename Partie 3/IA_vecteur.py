import math
import Donnees as data
import time

def transformation_vecteur():
    vecteur = {}
    dfGroupeGenre = data.films_genres.groupby("idFilm")["nomGenre"].agg(list).reset_index()

    for i , row in dfGroupeGenre.iterrows() :
        idFilm = row["idFilm"]
        genres = row["nomGenre"]
        vecteur[idFilm] = []
        for j in data.genres["nomGenre"] :  
            if (j in genres) : 
                vecteur[idFilm].append(1)
            else : 
                vecteur[idFilm].append(0)
    
    return vecteur

def sim_eucli(A,B) :
    """
    Similarité sur la distance Euclidienne 
    """
    somme = 0 
    for i in zip(A,B) : 
        somme += (i[0] - i[1]) * (i[0] - i[1])

    if (somme > 0) : 
        rep = 1/math.sqrt(somme)
    else :
        rep = 1
    return rep

# User based

def prediction_user(A,B) : 
    somme_sur = 0
    somme_sous = 0
    liste_users = list(vecteur_users.keys())
    liste_users.remove(A)
    print(liste_users)
    for i in liste_users :  
        # print(i,"  ",note[i][B])
        simi = sim(vecteur_users[A],vecteur_users[i])
        # print(simi)
        somme_sur += note[i][B] * simi
        somme_sous += simi
    
    return somme_sur/somme_sous


# Item based

def prediction_item(A,B) : 
    somme_sur = 0
    somme_sous = 0
    liste_items = list(vecteur_items.keys())
    liste_items.remove(B)
    print(liste_items)
    for i in liste_items :  
        # print(i,"  ",note[A][i])
        simi = sim(vecteur_items[B],vecteur_items[i])
        # print(simi)
        somme_sur += note[A][i] * simi
        somme_sous += simi
    
    return somme_sur/somme_sous

vecteurs = transformation_vecteur()

while 1 : 
    recommandation = {}
    nom_film = input("Sur quel film voulez vous faire la recommandation ?\n")

    id_vecteur = data.films_genres.loc[data.films_genres['titre'] == nom_film, 'idFilm'].values[0]
    
    print(id_vecteur)

    start = time.time()

    for i in list(vecteurs.keys()) :
        recommandation[i] = sim_eucli(vecteurs[id_vecteur], vecteurs[i])

    recommandation_trie = dict(sorted(recommandation.items(), key=lambda item: item[1], reverse = True))

    recommandation_trie_test = dict(list(recommandation_trie.items())[:10])

    for i in recommandation_trie_test.keys() : 
        print(data.films_genres.loc[data.films_genres['idFilm'] == i, 'titre'].values[0])

    
    stop = time.time() - start

    print(recommandation_trie_test)
    print(stop)
