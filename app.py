from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/squad")
def squad():
    return render_template("squad.html")


@app.route("/club")
def club():
    return render_template("club.html")


@app.route("/player/<name>")
def player(name):
    return f"Player profile: {escape(name)}"
    

