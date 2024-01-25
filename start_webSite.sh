#!/bin/bash

# Lancer l'API en utilisant uvicorn
python3 -m uvicorn Partie_4.API:app --reload &

# Lancer le site en utilisant PHP
php -S localhost:8080 -t Partie_5
