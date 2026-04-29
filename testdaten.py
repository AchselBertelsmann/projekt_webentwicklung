import sqlite3

conn = sqlite3.connect("analog.db")
cursor = conn.cursor()

hersteller = [
    {"name": "Canon", "land": "Japan", "wikidata_id": "Q192164"},
    {"name": "Leica", "land": "Deutschland", "wikidata_id": "Q152905"},
    {"name": "Kodak", "land": "USA", "wikidata_id": "Q133346"},
    {"name": "Fujifilm", "land": "Japan", "wikidata_id": "Q183287"},
    {"name": "Ilford", "land": "Vereinigtes Königreich", "wikidata_id": "Q992465"},
]

kameras = [
    {"name": "Canon AE-1", "hersteller_id": 1, "baujahr": 1976, "kameratyp": "Spiegelreflexkamera", "beschreibung": "Eine der meistverkauften analogen Kameras der Geschichte, bekannt für ihre Zuverlässigkeit und Bedienfreundlichkeit.", "bild_pfad": None, "wikidata_id": "Q220017", "dbpedia_uri": "http://dbpedia.org/resource/Canon_AE-1"},
    {"name": "Leica M6", "hersteller_id": 2, "baujahr": 1984, "kameratyp": "Messsucherkamera", "beschreibung": "Ikone der analogen Fotografie, geschätzt für ihre kompakte Bauweise und den leisen Verschluss.", "bild_pfad": None, "wikidata_id": "Q942285", "dbpedia_uri": "http://dbpedia.org/resource/Leica_M6"},
    {"name": "Canon F-1", "hersteller_id": 1, "baujahr": 1971, "kameratyp": "Spiegelreflexkamera", "beschreibung": "Canons professionelles Flaggschiff der 1970er Jahre, robust und modular erweiterbar.", "bild_pfad": None, "wikidata_id": "Q1034843", "dbpedia_uri": "http://dbpedia.org/resource/Canon_F-1"},
]

filme = [
    {"name": "Kodak Portra 400", "hersteller_id": 3, "iso": 400, "format": "35mm", "typ": "Farbnegativ", "beschreibung": "Professioneller Portraitfilm mit natürlichen Hauttönen und feiner Körnung, sehr beliebt in der Portraitfotografie.", "bild_pfad": None, "wikidata_id": "Q18218638", "dbpedia_uri": "http://dbpedia.org/resource/Kodak_Portra"},
    {"name": "Ilford HP5 Plus", "hersteller_id": 5, "iso": 400, "format": "35mm", "typ": "Schwarzweiß-Negativ", "beschreibung": "Klassischer Schwarzweißfilm mit großem Belichtungsspielraum, ideal für Push-Entwicklung.", "bild_pfad": None, "wikidata_id": "Q65076512", "dbpedia_uri": "http://dbpedia.org/resource/Ilford_HP5"},
    {"name": "Fujifilm Velvia 50", "hersteller_id": 4, "iso": 50, "format": "35mm", "typ": "Dia", "beschreibung": "Diafilm mit extrem kräftigen Farben und hoher Schärfe, besonders beliebt in der Landschaftsfotografie.", "bild_pfad": None, "wikidata_id": "Q2746778", "dbpedia_uri": "http://dbpedia.org/resource/Fujichrome_Velvia"},
]

objektive = [
    {"name": "Canon FD 50mm f/1.4", "hersteller_id": 1, "lichtstaerke_min": 1.4, "lichtstaerke_max": 16.0, "brennweite_min": 50, "brennweite_max": 50, "baujahr": 1971, "beschreibung": "Lichtstarkes Normalobjektiv aus der Canon FD-Reihe, bekannt für seine Schärfe und angenehmes Bokeh.", "bild_pfad": None, "wikidata_id": None, "dbpedia_uri": None},
    {"name": "Leica Summicron 35mm f/2", "hersteller_id": 2, "lichtstaerke_min": 2.0, "lichtstaerke_max": 16.0, "brennweite_min": 35, "brennweite_max": 35, "baujahr": 1958, "beschreibung": "Legendäres Weitwinkelobjektiv für das Leica M-System, geschätzt für seine außergewöhnliche Abbildungsleistung.", "bild_pfad": None, "wikidata_id": None, "dbpedia_uri": None},
    {"name": "Canon FD 35-70mm f/3.5-4.5", "hersteller_id": 1, "lichtstaerke_min": 3.5, "lichtstaerke_max": 22.0, "brennweite_min": 35, "brennweite_max": 70, "baujahr": 1982, "beschreibung": "Vielseitiges Zoomobjektiv für die Canon FD-Serie, kompakt und alltagstauglich für verschiedenste Motive.", "bild_pfad": None, "wikidata_id": None, "dbpedia_uri": None},
]


cursor.executemany("""
    INSERT INTO hersteller (name, land, wikidata_id)
    VALUES (:name, :land, :wikidata_id)
""", hersteller)

print("Herstellerdaten befüllt")

cursor.executemany("""
    INSERT INTO kamera (name, hersteller_id, baujahr, kameratyp, beschreibung, bild_pfad, wikidata_id, dbpedia_uri)
    VALUES (:name, :hersteller_id, :baujahr, :kameratyp, :beschreibung, :bild_pfad, :wikidata_id, :dbpedia_uri)
""", kameras)

print("Kameras befüllt")

cursor.executemany("""
    INSERT INTO film (name, hersteller_id, iso, format, typ, beschreibung, bild_pfad, wikidata_id, dbpedia_uri)
    VALUES (:name, :hersteller_id, :iso, :format, :typ, :beschreibung, :bild_pfad, :wikidata_id, :dbpedia_uri)
""", filme)

print("Filme befüllt")

cursor.executemany("""
    INSERT INTO objektiv (name, hersteller_id, lichtstaerke_min, lichtstaerke_max, brennweite_min, brennweite_max, baujahr, beschreibung, bild_pfad, wikidata_id, dbpedia_uri)
    VALUES (:name, :hersteller_id, :lichtstaerke_min, :lichtstaerke_max, :brennweite_min, :brennweite_max, :baujahr, :beschreibung, :bild_pfad, :wikidata_id, :dbpedia_uri)
""", objektive)

print("Objektive befüllt")


conn.commit()
print("Änderungen gespeichert")

conn.close()
print("fertig")