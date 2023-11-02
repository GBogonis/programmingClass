from flask import Flask, render_template, request
from jinja2 import Template
#from textblob import TextBlob
import random
import requests
import json
app = Flask(__name__)


funnyMessagesList = ["copyright: me :3", 
                     "RIP: dark sky",
                     "google weather stole our idea, trust",
                     "the real weather app was the friends we made along the way",
                     "WARNING: must be a silly goose to enter :3",
                     '"it is not a skill issue, it is a skill solution"',
                     "It's joever",
                     '"from the desk of Dr.Copenheimer"',
                     "the temperature has fallen, Billions must freeze"]

funnyMessage = random.choice(funnyMessagesList)


@app.route("/")

def userInput():
    context = {'funnyMessage' : funnyMessage}
    return render_template('userInput.html', **context)

@app.route("/weatherApp/", methods = ['POST', 'GET'])
def weatherApp():   
    
    if request.method == 'GET':
        return render_template('error.html')
    if request.method == 'POST':
        form_data = request.form
        lat = form_data["latitude"]
        lon = form_data["longitude"]
        #Lat and long
        #42.82642299955682, -71.57923160207767
        #api call
        apiCall = requests.get('https://api.openweathermap.org/data/2.5/weather?lat='+lat+'&lon='+lon+'&units=imperial&appid=15dfa1324b44123c1634401424dd71a1')
        apiText = apiCall.text
        apiData = json.loads(apiText)

        #data
        name = apiData['name']
        temp = apiData['main']['temp']
        temp = round(temp)
        description = apiData['weather'][0]['description']
        feelsLike = apiData['main']['feels_like']
        feelsLike = round(feelsLike)
        humidity = apiData['main']['humidity']
        windSpeed = apiData['wind']['speed']
        #context
        context = {'temperature' : temp, 
               'description' : description,
               'funnyMessage' : funnyMessage,
               'feelsLike' : feelsLike,
               'humidity' : humidity,
               'windSpeed' : windSpeed,
               'cityName' : name}
        
    return render_template('home.html', **context)

@app.route("/about")

def about():
    context = {'funnyMessage' : funnyMessage}
    return render_template('about.html', **context)

@app.route("/machineLearning")

def machineLearning():
    context = {'funnyMessage' : funnyMessage}
    return render_template('machineLearning.html', **context)