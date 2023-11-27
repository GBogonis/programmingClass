import requests
import json




#apiCall = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=42.82642299955682&lon=-71.57923160207767&units=imperial&appid=15dfa1324b44123c1634401424dd71a1')
#apiCall = requests.get('https://api.openweathermap.org/data/3.0/onecall/timemachine?lat=42.82642299955682&lon=-71.57923160207767&dt=1668970400&appid=15dfa1324b44123c1634401424dd71a1')
year = 2022
tempList = []
while year >= 2000: 
    print('start')
    yearStr = str(year)
    apiCall = requests.get('https://archive-api.open-meteo.com/v1/archive?latitude=42.826287240545135&longitude=-71.5792990891693&start_date=' + yearStr +'-11-27&end_date=' + yearStr +'-11-27&daily=temperature_2m_mean&temperature_unit=fahrenheit&wind_speed_unit=ms&precipitation_unit=inch')
    apiJson = apiCall.text
    data = json.loads(apiJson)
    tempList.append(data['daily']['temperature_2m_mean'])
    year -= 1
    print('end')

print(tempList)

