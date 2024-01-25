@echo off

:: Lancer l'API en utilisant uvicorn
start python3 -m uvicorn Partie_4.API:app --reload

:: Lancer le site en utilisant PHP
start php -S localhost:8080 -t Partie_5
