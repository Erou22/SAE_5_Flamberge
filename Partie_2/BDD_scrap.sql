DROP SCHEMA IF EXISTS flamberge_V2 CASCADE;
CREATE SCHEMA flamberge_V2;
SET SCHEMA 'flamberge_V2';

-- Tables

CREATE TABLE flamberge_V2._film (
    idFilm SERIAL PRIMARY KEY,
    titre VARCHAR(250) NOT NULL,
    isAdult INTEGER,
    anneeSortie INTEGER,
    poster VARCHAR(250),
    description VARCHAR(1000),
    dureeMinutes VARCHAR(10),
    note FLOAT,
    nbVotes INTEGER
);

CREATE TABLE flamberge_V2._artiste (
    idArtiste SERIAL PRIMARY KEY,
    nomArtiste VARCHAR(75)
);

CREATE TABLE flamberge_V2._metier (
    idMetier SERIAL PRIMARY KEY,
    nomMetier VARCHAR(25)
);

CREATE TABLE flamberge_V2._exerce_metier (
    idMetier INTEGER,
    idArtiste INTEGER,
    CONSTRAINT metier_fk FOREIGN KEY (idMetier) REFERENCES flamberge_V2._metier(idMetier),
    CONSTRAINT artiste_fk FOREIGN KEY (idArtiste) REFERENCES flamberge_V2._artiste(idArtiste),
    CONSTRAINT exerce_metier_pk PRIMARY KEY (idMetier,idArtiste)
);

CREATE TABLE flamberge_V2._role (
    idFilm INTEGER,
    idArtiste INTEGER,
    nomRole VARCHAR(25),
    CONSTRAINT role_film_fk FOREIGN KEY (idFilm) REFERENCES flamberge_V2._film(idFilm),
    CONSTRAINT role_artiste_fk FOREIGN KEY (idArtiste) REFERENCES flamberge_V2._artiste(idArtiste),
    CONSTRAINT role_pk PRIMARY KEY (idFilm,idArtiste,nomRole)
);

CREATE TABLE flamberge_V2._genre (
    idGenre SERIAL PRIMARY KEY,
    nomGenre VARCHAR(25)
);

CREATE TABLE flamberge_V2._possede_genre (
    idGenre INTEGER,
    idFilm INTEGER,
    CONSTRAINT film_fk FOREIGN KEY (idFilm) REFERENCES flamberge_V2._film(idFilm),
    CONSTRAINT genre_fk FOREIGN KEY (idGenre) REFERENCES flamberge_V2._genre(idGenre),
    CONSTRAINT possede_genre_pk PRIMARY KEY (idGenre,idFilm)
);
-- Fonctions



-- Triggers



-- Peuplement

create table flamberge_V2._temp(
    nomArtiste VARCHAR(75),
    metiers VARCHAR(100),
    titre VARCHAR(250),
    anneeSortie INTEGER,
    poster VARCHAR(250),
    description VARCHAR(1000),
    isAdult INTEGER,
    dureeMinutes VARCHAR(10),
    note FLOAT,
    nbVotes INTEGER,
    genres VARCHAR(100),
    role varchar(20)
);

WbimpoRT -FILE=../30K_csv_test.csv
        -TABLE=flamberge_V2._TEMP
        -DELIMITER=';'
        -QUOTECHAR="'"
        -MODE=INSERT
        -filecolumns=$wb_skip$,$wb_skip$,isAdult,titre,poster,description,anneeSortie,dureeMinutes,genres,note,nbVotes,$wb_skip$,role,nomArtiste,metiers;
        
select * from flamberge_V2._temp where titre like '%Semicolon%';
  
INSERT INTO flamberge_V2._artiste (nomArtiste)
  SELECT DISTINCT nomArtiste
  FROM flamberge_V2._temp;
  
INSERT INTO flamberge_V2._film (titre, isAdult, anneeSortie, poster, description, dureeMinutes, note, nbVotes)
  SELECT DISTINCT titre, isAdult, anneeSortie, poster, description, dureeMinutes, note, nbVotes
  FROM flamberge_V2._temp;

INSERT INTO flamberge_V2._metier (nomMetier)
  SELECT DISTINCT unnest(string_to_array(metiers, ',')) AS nomMetier
  FROM flamberge_V2._temp;

INSERT INTO flamberge_V2._exerce_metier (idArtiste, idMetier)
  SELECT DISTINCT a.idArtiste, m.idMetier
  FROM flamberge_V2._temp t
  JOIN flamberge_V2._artiste a ON t.nomArtiste = a.nomArtiste
  JOIN flamberge_V2._metier m ON m.nomMetier = ANY(string_to_array(t.metiers, ','));
  
INSERT INTO flamberge_V2._genre (nomGenre)
  SELECT DISTINCT unnest(string_to_array(genres, ',')) AS nomGenre
  FROM flamberge_V2._temp;
  
INSERT INTO flamberge_V2._possede_genre (idGenre, idFilm)
  SELECT DISTINCT g.idGenre, f.idFilm
  FROM flamberge_V2._temp t
  JOIN flamberge_V2._film f ON t.titre = f.titre
  JOIN flamberge_V2._genre g ON g.nomGenre = ANY(string_to_array(t.genres, ','));

INSERT INTO flamberge_V2._role (idFilm, idArtiste, nomRole)
  SELECT DISTINCT f.idFilm, a.idArtiste, t.role
  FROM flamberge_V2._temp t
  JOIN flamberge_V2._film f ON t.titre = f.titre
  JOIN flamberge_V2._artiste a ON t.nomArtiste = a.nomArtiste;
  
--DROP TABLE _temp;

-- Views

CREATE OR REPLACE VIEW flamberge_V2.global AS 
  SELECT * FROM flamberge_V2._film NATURAL JOIN flamberge_V2._possede_genre NATURAL JOIN flamberge_V2._genre NATURAL JOIN flamberge_V2._role NATURAL JOIN flamberge_V2._artiste NATURAL JOIN flamberge_V2._exerce_metier NATURAL JOIN flamberge_V2._metier;

SELECT titre, anneeSortie, note, nbVotes, nomGenre, nomRole, nomArtiste, nomMetier FROM flamberge_V2.global;

CREATE OR REPLACE VIEW flamberge_V2.fgenres AS
  SELECT * from flamberge_V2._film NATURAL JOIN flamberge_V2._possede_genre NATURAL JOIN flamberge_V2._genre;
  
SELECT titre, anneeSortie, note, nbVotes, nomGenre from flamberge_V2.fgenres;

CREATE OR REPLACE VIEW flamberge_V2.fartiste AS
  SELECT * from flamberge_V2._film NATURAL JOIN flamberge_V2._role NATURAL JOIN flamberge_V2._artiste NATURAL JOIN flamberge_V2._exerce_metier NATURAL JOIN flamberge_V2._metier;
  
SELECT titre, anneeSortie, note, nbVotes, nomRole, nomArtiste, nomMetier FROM flamberge_V2.fartiste;

SELECT idArtiste, nomArtiste, nomRole FROM flamberge_V2.fartiste WHERE nomArtiste like '%Christopher Nolan%';

SELECT idFilm, nomGenre FROM flamberge_V2.fgenres WHERE idFilm = 1; 
