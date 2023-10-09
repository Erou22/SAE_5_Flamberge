DROP SCHEMA IF EXISTS flamberge CASCADE;
CREATE SCHEMA flamberge;
SET SCHEMA 'flamberge';

-- Tables

CREATE TABLE _films (
    idFilm SERIAL PRIMARY KEY,
    titre VARCHAR(100) NOT NULL,
    anneeSortie INTEGER,
    noteIMDb FLOAT,
    nbVotes INTEGER
);

CREATE TABLE _artiste (
    idArtiste SERIAL PRIMARY KEY,
    nomArtiste VARCHAR(75)
);

CREATE TABLE _metier (
    idMetier SERIAL PRIMARY KEY,
    nomMetier VARCHAR(15)
);

CREATE TABLE _est_metier (
    idMetier INTEGER,
    idArtiste INTEGER,
    CONSTRAINT metier_fk FOREIGN KEY (idMetier) REFERENCES _metier(idMetier),
    CONSTRAINT artiste_fk FOREIGN KEY (idArtiste) REFERENCES _artiste(idArtiste),
    CONSTRAINT est_metier_pk PRIMARY KEY (idMetier,idArtiste)
);

CREATE TABLE _role (
    idFilm INTEGER,
    idArtiste INTEGER,
    nomRole VARCHAR(15),
    CONSTRAINT role_films_fk FOREIGN KEY (idFilm) REFERENCES _films(idFilm),
    CONSTRAINT role_artiste_fk FOREIGN KEY (idArtiste) REFERENCES _artiste(idArtiste),
    CONSTRAINT role_pk PRIMARY KEY (idFilm,idArtiste)
);

CREATE TABLE _genre (
    idGenre SERIAL PRIMARY KEY,
    nomGenre VARCHAR
);

CREATE TABLE _possede_genre (
    idGenre INTEGER,
    idFilm INTEGER,
    CONSTRAINT films_fk FOREIGN KEY (idFilm) REFERENCES _films(idFilm),
    CONSTRAINT genre_fk FOREIGN KEY (idGenre) REFERENCES _genre(idGenre),
    CONSTRAINT possede_genre_pk PRIMARY KEY (idGenre,idFilm)
);
-- Fonctions

CREATE OR REPLACE FUNCTION split_genre_f() RETURNS TRIGGER AS 
$$
BEGIN
    INSERT INTO _possede_genre (i)
        SELECT i FROM SPLIT_PART(idGenre, ',', 1);
    RETURNS NULL;
END;
$$ language plpgsql

-- Peuplement

create table _temp(
    nomArtiste VARCHAR(75),
    metiers VARCHAR(100),
    titre VARCHAR(100),
    anneeSortie INTEGER,
    noteIMDb FLOAT,
    nbVotes INTEGER,
    genres VARCHAR(100),
    role varchar(20)
);

Wbimport -file=../datasetIMDb.csv
        -table=_temp
        -delimiter=';'
        -quoteChar='"'
        -mode=insert
        -filecolumns=$wb_skip$,titre,anneeSortie,$wb_skip$,genres,noteIMDb,nbVotes,role,nomArtiste,$wb_skip$,metiers;
        

-- Triggers

CREATE TRIGGER split_genre_t
    BEFORE INSERT ON _possede_genre
    FOR EACH ROW
    EXECUTE FUNCTION split_genre_f();

-- Views

select * from _temp where titre like '%Semicolon%';