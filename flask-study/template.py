from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('hello.html')

@app.route("/tut")
def hello_tut():
    return render_template('tut.html')
