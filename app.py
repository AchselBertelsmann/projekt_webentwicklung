from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Test"

# App nicht nur über localhost sondern auch Netzwerk verfügbar machen (0.0.0.0)
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
