from flask import Flask
from flask import render_template
from jinja2 import Template
import random
app = Flask(__name__)

temp = 62
funnyMessagesList = ["copyright: me :3", 
                     "RIP: dark sky",
                     "google weather stole our idea, trust",
                     "the real weather app was the friends we made along the way",
                     "WARNING: must be a silly goose to inter :3",
                     '"it is not a skill issue, it is a skill solution"']

funnyMessage = random.choice(funnyMessagesList)


@app.route("/")

def hello_world():
    context = {'temprature' : temp,'funnyMessage' : funnyMessage}
    return render_template('hello.html', **context)

@app.route("/about")

def about():
    return render_template('about.html')

@app.route("/machineLearning")

def machineLearning():
    return render_template('machineLearning.html')