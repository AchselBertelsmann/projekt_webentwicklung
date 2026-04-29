import sqlite3

# Verbinde dich mit der Datenbank (Datei wird automatisch erstellt, wenn sie nicht existiert)
con = sqlite3.connect("analog.db")

# Lies das Schema und führe alle CREATE TABLE Befehle aus
with open("schema.sql") as f:
    con.executescript(f.read())

con.close()
print("Datenbank erstellt!")