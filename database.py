import sqlite3

# Verbindung zu Datenbank herstellen
con = sqlite3.connect("analog.db")

# Schema.sql einlesen und Datenbank erstellen
with open("schema.sql") as f:
    con.executescript(f.read())

con.close()
print("Datenbank erstellt!")