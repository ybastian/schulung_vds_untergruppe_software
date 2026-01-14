# app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def startseite():
    return "Hallo, Flask läuft!"

if __name__ == "__main__":
    app.run(debug=True)
