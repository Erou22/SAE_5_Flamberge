import pandas as pd
import sys
from pathlib import Path

# Get the absolute path to the Partie_3 directory
partie_3_path = Path("~/Documents/SAE/Repo/SAE_5_Flamberge/Partie_3").expanduser().resolve()
sys.path.append(str(partie_3_path))

import Recommendation  # Assuming Recommendation is the module inside Partie_3 directory


from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/film/{item_id}")
def read_item(item_id: int):
    return Recommendation.getFilm(item_id).to_json(orient="split")