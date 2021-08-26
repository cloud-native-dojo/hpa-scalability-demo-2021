from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def top_page():
    return render_template('top.html')

@app.route("/result", methods=["POST"])
def result_page():
    username = request.form['username']
    return render_template('result.html', name=username)
