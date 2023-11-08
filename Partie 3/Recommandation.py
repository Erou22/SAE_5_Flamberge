import pandas as pd
import psycopg2
import connect

# Connexion à la base de données
conn = connect.conn

cur = conn.cursor()

#
# Charger le jeu de données dans une structure de données Pandas (DataFrame).
#

# Films
cur.execute(f"SELECT * FROM {connect.schema}._film")
films = pd.DataFrame(cur.fetchall())
films.columns = ['idFilm', 'titre', 'annee', 'note', 'nbVotes']

# Genres
cur.execute(f"SELECT * FROM {connect.schema}._genre")
genres = pd.DataFrame(cur.fetchall())
genres.columns = ['idGenre', 'nomGenre']

# Films-Genres
cur.execute(f"SELECT * FROM {connect.schema}._possede_genre")
film_genre = pd.DataFrame(cur.fetchall())
film_genre.columns = ['idFilm', 'idGenre']

# Artistes
cur.execute(f"SELECT * FROM {connect.schema}._artiste")
artistes = pd.DataFrame(cur.fetchall())
artistes.columns = ['idArtiste', 'nomArtiste']

# Roles
cur.execute(f"SELECT * FROM {connect.schema}._role")
roles = pd.DataFrame(cur.fetchall())
roles.columns = ['idFilm', 'idArtiste', 'nomRole']

print(films)