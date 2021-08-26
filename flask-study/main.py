from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/tut")
def tut_page():
    return "<h1>東京工科大学へようこそ!</h1>"
