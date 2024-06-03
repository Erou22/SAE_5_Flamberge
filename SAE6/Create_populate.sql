DROP schema if exists olympicgames CASCADE;

create schema olympicgames;

set schema 'olympicgames';

-- TABLES
-- ___________________________

create table olympicgames._state(
		state varchar(50) not null, constraint _state_PK primary key (state));

create table _year (
		year integer not null, constraint _year_PK primary key (year));

create table _athlete (
		athlete_id serial not null,
		athlete_url varchar(80) not null,
		athlete_full_name varchar(50) not null,
		games_participations integer not null,
		athlete_year_birth integer,
		athlete_state varchar(50),
		age integer,
     constraint _athlete_PK primary key (athlete_id));
     
create table _game (
		game_id varchar(30) not null,
		game_end_date date not null,
		game_start_date date not null,
		game_season varchar(6) not null,
		game_location varchar(50),
		game_year integer,
     constraint _game_PK primary key (game_id));
     
create table _discipline(
	discipline_id serial not null,
	discipline_title varchar(30) not null,
	event_title varchar(140) not null,
		constraint _disicpline_PK primary key (discipline_id));

     
create table _results (
		athlete_id integer not null,
		game_id varchar(30) not null,
		discipline_id integer not null,
		rank_position varchar(3) not null,
			constraint _result_PK primary key (athlete_id, game_id, discipline_id));

-- Constraints Section
-- ___________________ 

alter table olympicgames._athlete add constraint athlete_FK1
     foreign key (athlete_year_birth)
     references olympicgames._year;		

alter table olympicgames._athlete add constraint athlete_FK2
     foreign key (athlete_state)
     references olympicgames._state;	

alter table olympicgames._game add constraint game_FK1
     foreign key (game_location)
     references olympicgames._state;		
     
alter table olympicgames._game add constraint game_FK2
     foreign key (game_year)
     references olympicgames._year;		
     
alter table olympicgames._results add constraint results_FK_1
     foreign key (athlete_id)
     references olympicgames._athlete;
     
alter table olympicgames._results add constraint results_FK_2
     foreign key (game_id)
     references olympicgames._game;

alter table olympicgames._results add constraint results_FK_3
     foreign key (discipline_id)
     references olympicgames._discipline;

-- View Win
-- _______________________
			
Create or replace function attributeMedal(rank_position varchar(3)) RETURNS varchar(6) AS $$
DECLARE
     medal varchar(6);
BEGIN
     medal := NULL;
     IF (rank_position='1') THEN
          medal := 'GOLD';
     END IF;
     IF (rank_position='2') THEN
          medal := 'SILVER';
     END IF;
     IF (rank_position='3') THEN
          medal := 'BRONZE';
     END IF;
     RETURN medal;
END;
$$ language plpgsql;
	
create or replace view win(athlete_id, game_id, discipline_id, medal) AS
SELECT athlete_id, game_id, discipline_id, attributeMedal(rank_position) FROM _results WHERE rank_position='1' OR rank_position='2' OR rank_position='3'; 


-- Triggers
-- _________________________

CREATE OR REPLACE FUNCTION trigger_function_age() RETURNS TRIGGER AS $$
BEGIN
     IF NEW.age < 10 OR NEW.age > 72 THEN
          NEW.age := NULL;
     END IF;
     RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_age
     BEFORE INSERT OR UPDATE ON olympicgames._athlete
     FOR EACH ROW
     EXECUTE FUNCTION trigger_function_age();


-- Populate
-- _________________________		

create table _athlete_tmp (
		athlete_id serial not null,
		athlete_url varchar(80) not null,
		athlete_full_name varchar(50) not null,
		games_participations integer not null,
		athlete_year_birth integer,
     constraint _athlete_tmp_PK primary key (athlete_id));

WbImport -file=./olympicsGames/olympic_athletes.csv
         -header=true
         -table=olympicgames._athlete_tmp
         -delimiter=','
         -fileColumns=athlete_url,athlete_full_name,games_participations,$wb_skip$,athlete_year_birth,$wb_skip$,$wb_skip$
         -importColumns=$wb_skip$,athlete_url,athlete_full_name,games_participations,$wb_skip$,athlete_year_birth,$wb_skip$
         -ENCODING='UTF8';

-- CREATE OR REPLACE FUNCTION randomize_full_names()
-- RETURNS VOID AS $$
-- BEGIN
--     -- Ajouter une colonne temporaire pour stocker les noms mélangés
--     ALTER TABLE olympicgames._athlete_tmp ADD COLUMN full_name_temp VARCHAR(50);
    
--     -- Utiliser une sous-requête pour mélanger les noms aléatoirement
--     WITH noms_melanges AS (
--         SELECT athlete_id, athlete_full_name,
--                ROW_NUMBER() OVER (ORDER BY athlete_id) AS original_id,
--                ROW_NUMBER() OVER (ORDER BY random()) AS random_id
--         FROM olympicgames._athlete_tmp
--     )
--     UPDATE olympicgames._athlete_tmp a
--     SET full_name_temp = (
--         SELECT nm2.athlete_full_name
--         FROM noms_melanges nm1
--         JOIN noms_melanges nm2 ON nm1.random_id = nm2.original_id
--         WHERE nm1.athlete_id = a.athlete_id
--     );

--     -- Mettre à jour la colonne athlete_full_name avec les noms mélangés
--     UPDATE olympicgames._athlete_tmp
--     SET athlete_full_name = full_name_temp;
    
--     -- Supprimer la colonne temporaire
--     ALTER TABLE olympicgames._athlete_tmp DROP COLUMN full_name_temp;
-- END;
-- $$ LANGUAGE plpgsql;

-- SELECT randomize_full_names();

DROP TABLE IF EXISTS olympicgames.tmp_game;
create table olympicgames.tmp_game (
        game_id varchar(30) not null,
        game_end_date date not null,
        game_start_date date not null,
        game_season varchar(6) not null,
        game_location varchar(50),
        game_year integer not null,
     constraint tmp_game_PK primary key (game_id));

WbImport -file=./olympicsGames/olympic_hosts.csv
         -header=true
         -table=olympicgames.tmp_game
         -delimiter=','
         -fileColumns=game_id,game_end_date,game_start_date,game_location,$wb_skip$,game_season,game_year
         -importColumns=game_id,game_end_date,game_start_date,game_season,game_location,game_year
         -ENCODING='UTF8';


DROP TABLE IF EXISTS olympicgames._tmp;
CREATE TABLE _tmp(
     id serial not null,
     discipline_title varchar(30) not null,
     event_title varchar(140) not null,
     slug_game varchar(30) not null,
     rank_position varchar(3),
     country_name varchar(50),
     country_3_letter_code char(3),
     athlete_url varchar(80),
     athlete_full_name varchar(50) not null,
     constraint _tmp_PK primary key (id));

WbImport -file=./olympicsGames/olympic_results.csv
         -header=true
         -table=olympicgames._tmp
         -delimiter=','
         -fileColumns=discipline_title,event_title,slug_game,$wb_skip$,$wb_skip$,$wb_skip$,rank_position,country_name,$wb_skip$,country_3_letter_code,athlete_url,athlete_full_name,$wb_skip$,$wb_skip$
         -ENCODING='UTF8';

CREATE OR REPLACE FUNCTION change_game_id() RETURNS VOID AS $$
BEGIN
     ALTER TABLE olympicgames.tmp_game
          ADD COLUMN country_code char(3),
          ADD COLUMN game_id_tmp varchar(30); 
     
     CREATE SEQUENCE IF NOT EXISTS edition_number_seq;
     UPDATE olympicgames.tmp_game SET country_code = t.country_3_letter_code FROM olympicgames._tmp t WHERE tmp_game.game_id = t.slug_game AND tmp_game.game_location LIKE t.country_name;
     
     UPDATE tmp_game
        SET country_code = 'CHN'
        WHERE game_id = 'beijing-2022';
     UPDATE tmp_game
        SET country_code = 'CHN'
        WHERE game_id = 'beijing-2008';
     UPDATE tmp_game
        SET country_code = 'USA'
        WHERE game_id = 'salt-lake-city-2002';
     UPDATE tmp_game
        SET country_code = 'USA'
        WHERE game_id = 'atlanta-1996';
     UPDATE tmp_game
        SET country_code = 'USA'
        WHERE game_id = 'los-angeles-1984';
     UPDATE tmp_game
        SET country_code = 'RUS'
        WHERE game_id = 'moscow-1980';
     UPDATE tmp_game
        SET country_code = 'USA'
        WHERE game_id = 'lake-placid-1980';
     UPDATE tmp_game
        SET country_code = 'USA'
        WHERE game_id = 'squaw-valley-1960';
     UPDATE tmp_game
        SET country_code = 'AUS'
        WHERE game_id = 'melbourne-1956';
     UPDATE tmp_game
        SET country_code = 'USA'
        WHERE game_id = 'los-angeles-1932';
     UPDATE tmp_game
        SET country_code = 'USA'
        WHERE game_id = 'lake-placid-1932';
     UPDATE tmp_game
        SET country_code = 'USA'
        WHERE game_id = 'st-louis-1904';


     UPDATE olympicgames.tmp_game SET game_id_tmp = country_code || '-' || nextval('edition_number_seq') WHERE game_id_tmp IS NULL;
     UPDATE olympicgames._tmp SET slug_game = tmp_game.game_id_tmp FROM olympicgames.tmp_game WHERE _tmp.slug_game = tmp_game.game_id;
     UPDATE olympicgames.tmp_game SET game_id = game_id_tmp;

    ALTER TABLE olympicgames.tmp_game
        DROP COLUMN country_code,
        DROP COLUMN game_id_tmp;
END;
$$ LANGUAGE plpgsql;

SELECT change_game_id();

select * from _game;

-- We populate the year with both the birth years of the athletes and the years of the games.          
INSERT INTO olympicgames._year
SELECT DISTINCT athlete_year_birth FROM olympicgames._athlete_tmp a  WHERE athlete_year_birth IS NOT NULL;

INSERT INTO olympicgames._year
SELECT DISTINCT game_year FROM olympicgames.tmp_game g WHERE g.game_year IS NOT NULL AND g.game_year NOT IN (SELECT * FROM olympicgames._year) ;

-- We populate the state with both the state of the athletes and the state of the host games. 
INSERT INTO olympicgames._state 
SELECT DISTINCT country_name FROM olympicgames._tmp t WHERE country_name IS NOT NULL;

INSERT INTO olympicgames._state 
SELECT DISTINCT g.game_location FROM olympicgames.tmp_game g WHERE  g.game_location IS NOT NULL AND g.game_location NOT IN (SELECT * FROM _state) ;

INSERT INTO olympicgames._game 
SELECT * FROM tmp_game;


-- INSERT INTO athlete thanks to tmp_athlete and tmp
INSERT INTO olympicgames._athlete (athlete_url,athlete_full_name,games_participations,athlete_year_birth,athlete_state,age) 
     SELECT DISTINCT a.athlete_url, a.athlete_full_name, a.games_participations, a.athlete_year_birth, t.country_name, (g.game_year - a.athlete_year_birth)
     FROM olympicgames._tmp t
     INNER JOIN olympicgames._athlete_tmp a 
     ON a.athlete_url=t.athlete_url AND a.athlete_full_name=t.athlete_full_name
     INNER JOIN olympicgames.tmp_game g ON g.game_id=t.slug_game;


INSERT INTO olympicgames._discipline (discipline_title,event_title) 
SELECT DISTINCT discipline_title,event_title FROM olympicgames._tmp;

INSERT INTO olympicgames._results(athlete_id,game_id,discipline_id,rank_position)
SELECT DISTINCT a.athlete_id, tmp.slug_game, d.discipline_id, tmp.rank_position FROM olympicgames._tmp tmp 
     INNER JOIN olympicgames._discipline d ON tmp.discipline_title=d.discipline_title AND tmp.event_title = d.event_title
     INNER JOIN olympicgames._athlete a ON a.athlete_full_name=tmp.athlete_full_name AND a.athlete_url=tmp.athlete_url AND a.athlete_state=tmp.country_name
     WHERE rank_position IS NOT NULL;



DROP TABLE IF EXISTS olympicgames._athlete_tmp;
DROP TABLE IF EXISTS olympicgames._tmp;
DROP TABLE IF EXISTS olympicgames.tmp_game;


-------------------------------------------------
-- VUES
-------------------------------------------------

CREATE OR REPLACE VIEW athlete AS
    SELECT athlete_id, athlete_state, age
    FROM olympicgames._athlete;
     

CREATE OR REPLACE VIEW discipline AS
    SELECT discipline_id, discipline_title
    FROM olympicgames._discipline;


SELECT * FROM athlete;

SELECT * FROM discipline;
