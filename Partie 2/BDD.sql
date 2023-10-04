DROP SCHEMA IF EXISTS flamberge CASCADE;
CREATE SCHEMA flamberge;
SET SCHEMA 'flamberge';

CREATE TABLE _films (
    idFilm SERIAL PRIMARY KEY,
    titre VARCHAR(100) NOT NULL,
    anneeSortie INTEGER,
    noteIMDb FLOAT,
    nbNote INTEGER
);

CREATE TABLE _artiste (
    idArtiste SERIAL PRIMARY KEY,
    nomArtiste VARCHAR(50)
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
    SELECT SPLIT_PART(idGenre, ',', 1) INTO monrec FROM _genre;
    IF NOT FOUND THEN
        RAISE EXCEPTION 'genre not found';
    END IF; 
END;
$$ language plpgsql

-- Triggers

CREATE TRIGGER split_genre_t
    BEFORE INSERT ON _genre
    FOR EACH ROW
    EXECUTE FUNCTION split_genre_f();



-- Peuplement

WbImport ...


-- Views

