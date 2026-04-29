from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/kameras")
def index():
    return render_template("kameras.html")


@app.route("/filme")
def index():
    return render_template("filme.html")

@app.route("/objektive")
def index():
    return render_template("objektive.html")

# App nicht nur über localhost sondern auch Netzwerk verfügbar machen (0.0.0.0)
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
