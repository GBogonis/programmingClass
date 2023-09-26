from flask import Flask
from flask import render_template
from jinja2 import Template

app = Flask(__name__)

temp = 62


@app.route("/")

def hello_world():
    context = {'temprature' : temp}
    return render_template('hello.html', **context)