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

# Base si l'API est accessible
@app.get("/")
def read_root():
    return {"L'API": "Fonctione"}


# Retourne les recommendations d'un film
@app.get("/recommendations/{item_id}")
def read_recommendation(item_id: int):
    recommendations_data = Recommendation.getRecommendation(item_id)
    
    if isinstance(recommendations_data, str):
        # Handle the case where getRecommendation returned an error message
        return JSONResponse(content={"error": recommendations_data}, media_type="application/json")
    else:
        # Extract relevant fields from the DataFrame
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
        
        # Create a dictionary with the recommendations
        result_dict = {"recommendations": recommendations_list}
        
        return JSONResponse(content=result_dict, media_type="application/json")
    
# Retourne tous les films
@app.get("/films/")
def read_film():
    films_data = Recommendation.getAllFilm()
    if isinstance(films_data, str):
        return JSONResponse(content={"error": films_data}, media_type="application/json")
    else : 
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
        
        # Create a dictionary with the recommendations
        result_dict = {"Films": all_films_list}
        
        return JSONResponse(content=result_dict, media_type="application/json", status_code=200)



# Retourne un film
@app.get("/films/{item_id}")
def read_film(item_id: int):
    # Assuming Recommendation.getFilm(item_id) returns a Pandas Series or a string
    films_data = Recommendation.getFilm(item_id)
    
    if isinstance(films_data, str):
        # Handle the case where getFilm returned an error message
        return JSONResponse(content={"error": films_data}, media_type="application/json")
    else:
        # Extract relevant fields and convert to native Python types
        annee = films_data.get("annee", None).item()
        titre = str(str(films_data.get("titre", None)))
        note = films_data.get("note", None).item()
        nbVotes = films_data.get("nbVotes", None).item()
        nomGenre = films_data.get("nomGenre", None)
        
        # Create a dictionary with the selected fields
        result_dict = {
            "id film": item_id,
            "annee": annee,
            "titre": titre,
            "note": note,
            "nbVotes": nbVotes,
            "nomGenre": nomGenre
        }
        
        return JSONResponse(content=result_dict, media_type="application/json", status_code=200)



# Retourne tous les acteurs d'un film
@app.get("/acteurs/{item_id}")

def read_acteurs(item_id: int):
    actors_data = Donnees.getActeurs(item_id)
    
    if isinstance(actors_data, list):
        # Create a dictionary with the list of actors
        result_dict = {"actors": actors_data}
        return JSONResponse(content=result_dict, media_type="application/json", status_code=200)
    else:
        # Handle the case where getActeurs returned an error message
        return JSONResponse(content={"error": actors_data}, media_type="application/json", status_code=404)
    

# Retourne tous les realisateur d'un film
@app.get("/realisateurs/{item_id}")

def read_realisteur(item_id: int):
    directors_data = Donnees.getRealisateurs(item_id)
    
    if isinstance(directors_data, list):
        # Create a dictionary with the list of actors
        result_dict = {"director": directors_data}
        return JSONResponse(content=result_dict, media_type="application/json", status_code=200)
    else:
        # Handle the case where getActeurs returned an error message
        return JSONResponse(content={"error": directors_data}, media_type="application/json", status_code=404)
    
# Retourne la fiche complète d'un film
@app.get("/filmComplet/{item_id}")

def read_filmComplet(item_id: int):
    film_data = Donnees.getFilmComplet(item_id)
    
    if isinstance(film_data, list):
        # Create a dictionary with the list of actors
        result_dict = {"film": film_data}
        return JSONResponse(content=result_dict, media_type="application/json", status_code=200)
    else:
        # Handle the case where getActeurs returned an error message
        return JSONResponse(content={"error": film_data}, media_type="application/json", status_code=404)
    
# Retourne tous les films d'un acteur
@app.get("/films/acteur/{item_id}")

def read_filmsAvecActeur(item_id: int):
    films_data = Donnees.getFilmsAvecActeur(item_id)
    
    if isinstance(films_data, list):
        # Create a dictionary with the list of actors
        result_dict = {"films": films_data}
        return JSONResponse(content=result_dict, media_type="application/json", status_code=200)
    else:
        # Handle the case where getActeurs returned an error message
        return JSONResponse(content={"error": films_data}, media_type="application/json", status_code=404)
    

# Retourne tous les films d'un réalisateur
@app.get("/films/realisateur/{item_id}")

def read_filmsAvecRealisateur(item_id: int):
    films_data = Donnees.getFilmsAvecRealisateur(item_id)
    
    if isinstance(films_data, list):
        # Create a dictionary with the list of actors
        result_dict = {"films": films_data}
        return JSONResponse(content=result_dict, media_type="application/json", status_code=200)
    else:
        # Handle the case where getActeurs returned an error message
        return JSONResponse(content={"error": films_data}, media_type="application/json", status_code=404)
    

# Retourne tous les films avec un genre
@app.get("/genres/{nom_genre}")

def read_genre(nom_genre: str):
    films_data = Donnees.getFilmsGenre(nom_genre)
    
    if isinstance(films_data, list):
        # Create a dictionary with the list of actors
        result_dict = {"films": films_data}
        return JSONResponse(content=result_dict, media_type="application/json", status_code=200)
    else:
        # Handle the case where getActeurs returned an error message
        return JSONResponse(content={"error": films_data}, media_type="application/json", status_code=404)