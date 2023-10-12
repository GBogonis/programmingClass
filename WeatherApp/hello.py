from flask import Flask
from flask import render_template
from jinja2 import Template
import random
import requests
app = Flask(__name__)

#Lat and long
#42.82642299955682, -71.57923160207767
data = requests.get("https://api.openweathermap.org/data/2.5/weather?lat={42.82642299955682}&lon={-71.57923160207767}&appid={15dfa1324b44123c1634401424dd71a1}")
print(data.status_code)


temp = 52
feelsLike = 52
humidity = 80
chanceOfRain = 0
windSpeed = 2
funnyMessagesList = ["copyright: me :3", 
                     "RIP: dark sky",
                     "google weather stole our idea, trust",
                     "the real weather app was the friends we made along the way",
                     "WARNING: must be a silly goose to inter :3",
                     '"it is not a skill issue, it is a skill solution"',
                     "It's joever",
                     '"from the desk of Dr.Copenheimer"']

funnyMessage = random.choice(funnyMessagesList)


@app.route("/")

def hello_world():
    context = {'temprature' : temp, 
               'funnyMessage' : funnyMessage,
               'feelsLike' : feelsLike,
               'humidity' : humidity,
               'chanceOfRain' : chanceOfRain,
               'windSpeed' : windSpeed}
    return render_template('hello.html', **context)

@app.route("/about")

def about():
    context = {'funnyMessage' : funnyMessage}
    return render_template('about.html', **context)

@app.route("/machineLearning")

def machineLearning():
    context = {'funnyMessage' : funnyMessage}
    return render_template('machineLearning.html', **context)