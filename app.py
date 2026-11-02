from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to FC Byte"


@app.route("/squad")
def squad():
    return "The FC Byte squad is coming soon"


@app.route("/club")
def club():
    return "The club is still being built. Updates coming soon!"


@app.route("/player/<name>")
def player(name):
    return f"Player profile: {escape(name)}"
    

