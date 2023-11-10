import math 

vecteur_items = {
    "R" : [1,1,0,1,1,1,1,1,0],
    "J" : [1,1,1,0,1,2,0,0,2],
    "B" : [1,1,1,1,1,1,0,0,0]
}

vecteur_users = {
    "U1" : [1,0,1],
    "U2" : [1,2,1],
    "U3" : [1,0,1]
}


note = {
    "U1" : {
        "R" : 8,
        "J" : 9,
        "B" : 7
    },
    "U2" : {
        "R" : 2,
        "J" : 3,
        "B" : 4
    },
    "U3" : {
        "R" : 7.5,
        "J" : None,
        "B" : 7
    }
}

note_item = {
    0 : [8,2,7.5],
    1 : [9,3,None],
    2 : [7,4,7]
}

def sim(A,B) :
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

print(prediction_user("U3","J"))


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

print(prediction_item("U3","J"))