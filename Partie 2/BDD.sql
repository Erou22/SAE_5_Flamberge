DROP SCHEMA IF EXISTS flamberge CASCADE;
CREATE SCHEMA flamberge;
SET SCHEMA 'flamberge';

-- Tables

CREATE TABLE _film (
    idFilm SERIAL PRIMARY KEY,
    titre VARCHAR(100) NOT NULL,
    anneeSortie INTEGER,
    note FLOAT,
    nbVotes INTEGER
);

CREATE TABLE _artiste (
    idArtiste SERIAL PRIMARY KEY,
    nomArtiste VARCHAR(75)
);

CREATE TABLE _metier (
    idMetier SERIAL PRIMARY KEY,
    nomMetier VARCHAR(25)
);

CREATE TABLE _exerce_metier (
    idMetier INTEGER,
    idArtiste INTEGER,
    CONSTRAINT metier_fk FOREIGN KEY (idMetier) REFERENCES _metier(idMetier),
    CONSTRAINT artiste_fk FOREIGN KEY (idArtiste) REFERENCES _artiste(idArtiste),
    CONSTRAINT exerce_metier_pk PRIMARY KEY (idMetier,idArtiste)
);

CREATE TABLE _role (
    idFilm INTEGER,
    idArtiste INTEGER,
    nomRole VARCHAR(25),
    CONSTRAINT role_film_fk FOREIGN KEY (idFilm) REFERENCES _film(idFilm),
    CONSTRAINT role_artiste_fk FOREIGN KEY (idArtiste) REFERENCES _artiste(idArtiste),
    CONSTRAINT role_pk PRIMARY KEY (idFilm,idArtiste,nomRole)
);

CREATE TABLE _genre (
    idGenre SERIAL PRIMARY KEY,
    nomGenre VARCHAR(25)
);

CREATE TABLE _possede_genre (
    idGenre INTEGER,
    idFilm INTEGER,
    CONSTRAINT film_fk FOREIGN KEY (idFilm) REFERENCES _film(idFilm),
    CONSTRAINT genre_fk FOREIGN KEY (idGenre) REFERENCES _genre(idGenre),
    CONSTRAINT possede_genre_pk PRIMARY KEY (idGenre,idFilm)
);
-- Fonctions



-- Triggers



-- Peuplement

create table _temp(
    nomArtiste VARCHAR(75),
    metiers VARCHAR(100),
    titre VARCHAR(100),
    anneeSortie INTEGER,
    note FLOAT,
    nbVotes INTEGER,
    genres VARCHAR(100),
    role varchar(20)
);

WbimpoRT -FILE=../datasetIMDb.csv
        -TABLE=_TEMP
        -DELIMITER=';'
        -QUOTECHAR='"'
        -MODE=INSERT
        -filecolumns=$wb_skip$,titre,anneeSortie,$wb_skip$,genres,note,nbVotes,role,nomArtiste,$wb_skip$,metiers;
        
select * from _temp where titre like '%Semicolon%';
  
INSERT INTO _artiste (nomArtiste)
  SELECT DISTINCT nomArtiste
  FROM _temp;
  
INSERT INTO _film (titre, anneeSortie, note, nbVotes)
  SELECT DISTINCT titre, anneeSortie, note, nbVotes
  FROM _temp;

INSERT INTO _metier (nomMetier)
  SELECT DISTINCT unnest(string_to_array(metiers, ',')) AS nomMetier
  FROM _temp;

INSERT INTO _exerce_metier (idArtiste, idMetier)
  SELECT DISTINCT a.idArtiste, m.idMetier
  FROM _temp t
  JOIN _artiste a ON t.nomArtiste = a.nomArtiste
  JOIN _metier m ON m.nomMetier = ANY(string_to_array(t.metiers, ','));
  
INSERT INTO _genre (nomGenre)
  SELECT DISTINCT unnest(string_to_array(genres, ',')) AS nomGenre
  FROM _temp;
  
INSERT INTO _possede_genre (idGenre, idFilm)
  SELECT DISTINCT g.idGenre, f.idFilm
  FROM _temp t
  JOIN _film f ON t.titre = f.titre
  JOIN _genre g ON g.nomGenre = ANY(string_to_array(t.genres, ','));

INSERT INTO _role (idFilm, idArtiste, nomRole)
  SELECT DISTINCT f.idFilm, a.idArtiste, t.role
  FROM _temp t
  JOIN _film f ON t.titre = f.titre
  JOIN _artiste a ON t.nomArtiste = a.nomArtiste;
  
--DROP TABLE _temp;

-- Views

CREATE OR REPLACE VIEW global AS 
  SELECT * FROM _film NATURAL JOIN _possede_genre NATURAL JOIN _genre NATURAL JOIN _role NATURAL JOIN _artiste NATURAL JOIN _exerce_metier NATURAL JOIN _metier;

SELECT titre, anneeSortie, note, nbVotes, nomGenre, nomRole, nomArtiste, nomMetier FROM global;

CREATE OR REPLACE VIEW fgenres AS
  SELECT * from _film NATURAL JOIN _possede_genre NATURAL JOIN _genre;
  
SELECT titre, anneeSortie, note, nbVotes, nomGenre from fgenres;

CREATE OR REPLACE VIEW fartiste AS
  SELECT * from _film NATURAL JOIN _role NATURAL JOIN _artiste NATURAL JOIN _exerce_metier NATURAL JOIN _metier;
  
SELECT titre, anneeSortie, note, nbVotes, nomRole, nomArtiste, nomMetier FROM fartiste;

SELECT idArtiste, nomArtiste, nomRole FROM fartiste WHERE nomArtiste like '%Christopher Nolan%';
