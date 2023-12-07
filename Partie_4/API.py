# python3 -m uvicorn API:app
import pandas as pd
import sys
import path

sys.path.append(str(path.partie_3_path))

import Recommendation
import Donnees

from typing import Union
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


app = FastAPI()

# "Hub" si retourne alors l'API est accessible
@app.get("/")
def read_root():
    return {"L'API": "Fonctione"}

# ============================================================================================
# ===================================== Retourne des films ===================================
# ============================================================================================

# Retourne les recommendations d'un film
@app.get("/recommendations/{item_id}")
def read_recommendation(item_id: int):
    recommendations_data = Recommendation.getRecommendation(item_id)
    
    if isinstance(recommendations_data, str):
        # Si il y a un message d'erreur de getRecommendation()
        return JSONResponse(content={"error": recommendations_data}, media_type="application/json")
    else:
        # Récupère les données et stock les données sous forme de dictionnaire
        recommendations_list = []
        for id, row in recommendations_data.iterrows():
            recommendation_dict = {
                "idFilm" : id,
                "titre": str(row["titre"]),
                "annee": row["annee"],
                "note": row["note"],
                "nbVotes": row["nbVotes"],
                "nomGenre": row["nomGenre"]
            }
            recommendations_list.append(recommendation_dict)
        
        # Creation d'un dictionnaire avec les recommendations
        result_dict = {"recommendations": recommendations_list}
        
        return JSONResponse(content=result_dict, media_type="application/json")


# Retourne tous les films
@app.get("/films/")
def read_film():
    films_data = Recommendation.getAllFilm()
    if isinstance(films_data, str):
        # Si il y a un message d'erreur de getAllFilm()
        return JSONResponse(content={"error": films_data}, media_type="application/json")
    else : 
         # Récupère les données et stock les données sous forme de dictionnaire
        all_films_list = []
        for id, row in films_data.iterrows():
            all_films_dict = {
                "idFilm" : id,
                "titre": str(row["titre"]),
                "annee": row["annee"],
                "note": row["note"],
                "nbVotes": row["nbVotes"],
                "nomGenre": row["nomGenre"]
            }
            all_films_list.append(all_films_dict)
        
        # Creation d'un dictionnaire avec tous les films
        result_dict = {"Films": all_films_list}
        
        return JSONResponse(content=result_dict, media_type="application/json")


# Retourne un film
@app.get("/films/{item_id}")
def read_film(item_id: int):
    films_data = Recommendation.getFilm(item_id)
    
    if isinstance(films_data, str):
        # Si il y a un message d'erreur de getFilm()
        return JSONResponse(content={"error": films_data}, media_type="application/json")
    else:
        # Extraction des champs utiles
        annee = films_data.get("annee", None).item()
        titre = str(films_data.get("titre", None))
        note = films_data.get("note", None).item()
        nbVotes = films_data.get("nbVotes", None).item()
        nomGenre = films_data.get("nomGenre", None)
        
        # Création d'un dictionnaire avec ces champs
        result_dict = {
            "id film": item_id,
            "annee": annee,
            "titre": titre,
            "note": note,
            "nbVotes": nbVotes,
            "nomGenre": nomGenre
        }
        
        return JSONResponse(content=result_dict, media_type="application/json")


# Retourne la fiche complète d'un film
@app.get("/films/{item_id}/fiche")
def read_filmComplet(item_id: int):
    film_data = Donnees.getFilmComplet(item_id)
    
    if isinstance(film_data, str):
        # Si il y a un message d'erreur de getFilmComplet()
        return JSONResponse(content={"error": film_data}, media_type="application/json")
    else:
         # Création d'un dictionnaire avec le résultat
        result_dict = {"film": film_data}
        return JSONResponse(content=result_dict, media_type="application/json")


# Retourne tous les films d'un acteur
@app.get("/films/acteur/{item_id}")
def read_filmsAvecActeur(item_id: int):
    films_data = Donnees.getFilmsAvecActeur(item_id)
    
    if isinstance(films_data, str):
        # Si il y a un message d'erreur de getFilmsAvecActeur()
        return JSONResponse(content={"error": films_data}, media_type="application/json")
    else:
        # Création d'un dictionnaire avec le résultat
        result_dict = {"films": films_data}
        return JSONResponse(content=result_dict, media_type="application/json")
   

# Retourne tous les films d'un réalisateur
@app.get("/films/realisateur/{item_id}")
def read_filmsAvecRealisateur(item_id: int):
    films_data = Donnees.getFilmsAvecRealisateur(item_id)
    
    if isinstance(films_data, str):
        # Si il y a un message d'erreur de getFilmsAvecRealisateur()
        return JSONResponse(content={"error": films_data}, media_type="application/json")
    else:
        # Création d'un dictionnaire avec le résultat
        result_dict = {"films": films_data}
        return JSONResponse(content=result_dict, media_type="application/json")
    

# Retourne tous les films avec le genre demandé
@app.get("/films/genre/{nom_genre}")
def read_genre(nom_genre: str):
    films_data = Donnees.getFilmsGenre(nom_genre)
    
    if isinstance(films_data, str):
        # Si il y a un message d'erreur de getFilmsGenre()
        return JSONResponse(content={"error": films_data}, media_type="application/json")
    else:
        # Création d'un dictionnaire avec le résultat
        result_dict = {"films": films_data}
        return JSONResponse(content=result_dict, media_type="application/json")
        

# ============================================================================================
# ==================================== Retourne des acteurs===================================
# ============================================================================================

# Retourne tous les acteurs d'un film
@app.get("/acteurs/{item_id}")
def read_acteurs(item_id: int):
    actors_data = Donnees.getActeurs(item_id)
    
    if isinstance(actors_data, str):
        # Si il y a un message d'erreur de getActeurs()
        return JSONResponse(content={"error": actors_data}, media_type="application/json")
    else:
        # Création d'un dictionnaire avec le résultat
        result_dict = {"actors": actors_data}
        return JSONResponse(content=result_dict, media_type="application/json")

# ============================================================================================
# ================================= Retourne des réalisateurs ================================
# ============================================================================================

# Retourne tous les realisateur d'un film
@app.get("/realisateurs/{item_id}")
def read_realisteur(item_id: int):
    directors_data = Donnees.getRealisateurs(item_id)
    
    if isinstance(directors_data, str):
        # Si il y a un message d'erreur de getRealisateurs
        return JSONResponse(content={"error": directors_data}, media_type="application/json")
    else:
        # Création d'un dictionnaire avec le résultat
        result_dict = {"director": directors_data}
        return JSONResponse(content=result_dict, media_type="application/json")