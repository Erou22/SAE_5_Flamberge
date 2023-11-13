import math
import Donnees as data

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

def sim(A,B) :
    """
    Similarité sur la distance Euclidienne 
    """
    somme = 0 
    for i in zip(A,B) : 
        somme += (i[0] - i[1]) * (i[0] - i[1])

    if (somme > 0) : 
        rep = 1/math.sqrt(somme)
    else :
        rep = 0
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
        simu = sim(vecteur_users[A],vecteur_users[i])
        # print(simu)
        somme_sur += note[i][B] * simu
        somme_sous += simu
    
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
        simu = sim(vecteur_items[B],vecteur_items[i])
        # print(simu)
        somme_sur += note[A][i] * simu
        somme_sous += simu
    
    return somme_sur/somme_sous

vecteurs = transformation_vecteur()