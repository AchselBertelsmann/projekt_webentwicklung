CREATE TABLE hersteller (
    id  INTEGER PRIMARY KEY AUTOINCREMENT ,
    name    TEXT NOT NULL , 
    land    TEXT ,
    wikidata_id TEXT UNIQUE

);

CREATE TABLE kamera (
    id  INTEGER PRIMARY KEY AUTOINCREMENT ,
    name    TEXT NOT NULL ,
    hersteller_id   INTEGER REFERENCES hersteller(id) ,
    baujahr INTEGER ,
    kameratyp   TEXT ,
    beschreibung    TEXT ,
    bild_pfad   TEXT , 
    wikidata_id TEXT UNIQUE ,
    dbpedia_uri TEXT
);

CREATE TABLE film (
    id  INTEGER PRIMARY KEY AUTOINCREMENT ,
    name    TEXT NOT NULL , 
    hersteller_id   INTEGER REFERENCES hersteller(id) , 
    iso         INTEGER ,
    format  TEXT , 
    typ     TEXT , 
    beschreibung    TEXT , 
    bild_pfad   TEXT , 
    wikidata_id     TEXT UNIQUE ,
    dbpedia_uri     TEXT
);

CREATE TABLE objektiv (
    id  INTEGER PRIMARY KEY AUTOINCREMENT ,
    name    TEXT NOT NULL , 
    hersteller_id   INTEGER REFERENCES hersteller(id) , 
    lichtstaerke_min    REAL ,
    lichtstaerke_max         REAL ,
    brennweite_min  INTEGER ,
    brennweite_max  INTEGER , 
    baujahr     TEXT , 
    beschreibung    TEXT , 
    bild_pfad   TEXT , 
    wikidata_id     TEXT UNIQUE ,
    dbpedia_uri     TEXT
);

CREATE TABLE tag (
    id  INTEGER PRIMARY KEY AUTOINCREMENT , 
    name    TEXT NOT NULL UNIQUE 
);

CREATE TABLE kamera_tag (
    kamera_id   INTEGER REFERENCES kamera(id) , 
    tag_id  INTEGER REFERENCES tag(id) ,
    PRIMARY KEY     (kamera_id, tag_id) 
);

CREATE TABLE film_tag (
    film_id     INTEGER REFERENCES film(id) ,
    tag_id  INTEGER REFERENCES tag(id) , 
    PRIMARY KEY     (film_id, tag_id)
);