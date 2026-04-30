from flask import Flask, render_template
import sqlite3
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/kameras")
def kameras():
    conn = sqlite3.connect("analog.db") # Verbindung zu db herstellen
    conn.row_factory = sqlite3.Row  # Ausgabe formatiert --> dictionary-mäßig
    cursor = conn.cursor() 
    
    cursor.execute("SELECT * FROM kamera") # Alle Daten aus kamera-db abrufen
    kameras = cursor.fetchall()
    
    conn.close()
    return render_template("kameras.html", kameras=kameras)


@app.route("/filme")
def filme():
    conn = sqlite3.connect("analog.db") # Verbindung zu db herstellen
    conn.row_factory = sqlite3.Row  # Ausgabe formatiert --> dictionary-mäßig
    cursor = conn.cursor() 
    
    cursor.execute("SELECT * FROM film") # Alle Daten aus kamera-db abrufen
    filme = cursor.fetchall()
    
    conn.close()
    return render_template("filme.html", filme=filme)

@app.route("/farbfilme")
def farbfilme():
    conn = sqlite3.connect("analog.db") # Verbindung zu db herstellen
    conn.row_factory = sqlite3.Row  # Ausgabe formatiert --> dictionary-mäßig
    cursor = conn.cursor() 
    
    cursor.execute("SELECT * FROM film WHERE typ = 'Farbnegativ'") # Alle Daten aus kamera-db abrufen die Farbnegative sind
    farbfilme = cursor.fetchall()
    
    conn.close()
    return render_template("farbfilme.html", farbfilme=farbfilme)

@app.route("/objektive")
def objektive():
    conn = sqlite3.connect("analog.db") # Verbindung zu db herstellen
    conn.row_factory = sqlite3.Row  # Ausgabe formatiert --> dictionary-mäßig
    cursor = conn.cursor() 
    
    cursor.execute("SELECT * FROM objektiv") # Alle Daten aus objektiv-db abrufen die Objektive sind
    objektive = cursor.fetchall()
    
    conn.close()
    return render_template("objektive.html", objektive=objektive)

# App nicht nur über localhost sondern auch Netzwerk verfügbar machen (0.0.0.0)
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
