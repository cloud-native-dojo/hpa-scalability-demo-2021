from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def top_page():
    return render_template('top.html')

@app.route("/result")
def result_page():
    return render_template('result.html')
