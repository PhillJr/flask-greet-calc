
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!- I'm changing<p><br><p>Change detected<p>"

@app.route("/welcome")
def welcome():
    return "<h1>welcome<h1>"
@app.route("/welcome/home")
def home():
    return "<h1>welcome home<h1>"
@app.route("/welcome/back")
def back():
    return "<h2 style='color:blue'>Welcome Back<h2>"
