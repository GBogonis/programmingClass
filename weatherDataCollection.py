import requests
import json

output = open("weatherData2.txt","w")


#apiCall = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=42.82642299955682&lon=-71.57923160207767&units=imperial&appid=15dfa1324b44123c1634401424dd71a1')
#apiCall = requests.get('https://api.openweathermap.org/data/3.0/onecall/timemachine?lat=42.82642299955682&lon=-71.57923160207767&dt=1668970400&appid=15dfa1324b44123c1634401424dd71a1')
year = 1982

startYear = 1982
endYear= 2022
day = 20
month = 12
tempList = []
while year <= endYear: 
    print(year)
    
    #print('start')
    apiCall = requests.get('https://archive-api.open-meteo.com/v1/archive?latitude=42.826287240545135&longitude=-71.5792990891693&start_date=' + str(year) +'-'+str(month)+'-'+str(day)+'&end_date=' + str(year) +'-'+str(month)+'-'+str(day)+'&daily=temperature_2m_mean&temperature_unit=fahrenheit&wind_speed_unit=ms&precipitation_unit=inch')
    apiJson = apiCall.text
    data = json.loads(apiJson)
    tempList.append(data['daily']['temperature_2m_mean'][0])
    outputStr = (str(year) + "," + str(data['daily']['temperature_2m_mean'][0]) +"\n")
    print(outputStr)
    output.write(outputStr)
    
    year += 1
    #print('end')

