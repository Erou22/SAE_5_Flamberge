import pandas as pd
import sys
import path

sys.path.append(str(path.partie_3_path))

import Recommendation  # Assuming Recommendation is the module inside Partie_3 directory


from typing import Union
from fastapi import FastAPI
from fastapi.responses import JSONResponse


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


#Retourne les recommendations d'un film
@app.get("/recommendation/{item_id}")
def read_recommendation(item_id: int):
    recommendations_data = Recommendation.getRecommendation(item_id)
    
    if isinstance(recommendations_data, str):
        # Handle the case where getRecommendation returned an error message
        return JSONResponse(content={"error": recommendations_data}, media_type="application/json")
    else:
        # Extract relevant fields from the DataFrame
        recommendations_list = []
        for _, row in recommendations_data.iterrows():
            recommendation_dict = {
                "titre": row["titre"],
                "annee": row["annee"],
                "note": row["note"],
                "nbVotes": row["nbVotes"],
                "nomGenre": row["nomGenre"],
                "cluster": row["cluster"]
            }
            recommendations_list.append(recommendation_dict)
        
        # Create a dictionary with the recommendations
        result_dict = {"recommendations": recommendations_list}
        
        return JSONResponse(content=result_dict, media_type="application/json")
    


#Retourne un film
@app.get("/film/{item_id}")
def read_film(item_id: int):
    # Assuming Recommendation.getFilm(item_id) returns a Pandas Series or a string
    film_data = Recommendation.getFilm(item_id)
    
    if isinstance(film_data, str):
        # Handle the case where getFilm returned an error message
        return JSONResponse(content={"error": film_data}, media_type="application/json")
    else:
        # Extract relevant fields and convert to native Python types
        annee = film_data.get("annee", None).item()
        titre = film_data.get("titre", None)
        note = film_data.get("note", None).item()
        nbVotes = film_data.get("nbVotes", None).item()
        nomGenre = film_data.get("nomGenre", None)
        cluster = film_data.get("cluster", None).item()
        
        # Create a dictionary with the selected fields
        result_dict = {
            "annee": annee,
            "titre": titre,
            "note": note,
            "nbVotes": nbVotes,
            "nomGenre": nomGenre,
            "cluster": cluster
        }
        
        return JSONResponse(content=result_dict, media_type="application/json")
