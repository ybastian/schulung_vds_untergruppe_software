from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = (request.form.get("name") or "").strip()
    return render_template("result.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)
