import requests
import json

output = open("weatherData3.txt","w")


#apiCall = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=42.82642299955682&lon=-71.57923160207767&units=imperial&appid=15dfa1324b44123c1634401424dd71a1')
#apiCall = requests.get('https://api.openweathermap.org/data/3.0/onecall/timemachine?lat=42.82642299955682&lon=-71.57923160207767&dt=1668970400&appid=15dfa1324b44123c1634401424dd71a1')
year = 1982

#startYear = 1982
endYear= 2023
day = '01'
month = '01'
#dataList = []

#apiCall = requests.get('https://archive-api.open-meteo.com/v1/archive?latitude=42.826287240545135&longitude=-71.5792990891693&start_date=' + str(year) +'-'+str(month)+'-'+str(day)+'&end_date=' + str(year) +'-'+str(month)+'-'+str(day)+'&daily=temperature_2m_mean&temperature_unit=fahrenheit&wind_speed_unit=ms&precipitation_unit=inch')
'''
apiCall = requests.get("https://archive-api.open-meteo.com/v1/archive?latitude=42.82642299955682&longitude=-71.57923160207767&start_date=2023-01-02&end_date=2023-01-02&daily=temperature_2m_mean,sunshine_duration,precipitation_sum,wind_speed_10m_max,shortwave_radiation_sum&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch&timezone=auto")
apiJson = apiCall.text
data = json.loads(apiJson)
print(data)
'''
#print(data['daily']['temperature_2m_mean'],data['daily']['sunshine_duration'],data['daily']['precipitation_sum'],data['daily']['wind_speed_10m_max'],data['daily']['shortwave_radiation_sum'])
startLine = "month,"+"temp,"+"sunshine,"+"precipitation,"+"windspeed,"+"radiation"+"\n"
#output.write(startLine)

while year <= endYear: 
    print(year)
    
    #print('start')
    apiCall = requests.get('https://archive-api.open-meteo.com/v1/archive?latitude=42.82642299955682&longitude=-71.57923160207767&start_date=' + str(year) + '-' + month + '-' + day + '&end_date=' + str(year) + '-' + month + '-' + day + '&daily=temperature_2m_mean,sunshine_duration,precipitation_sum,wind_speed_10m_max,shortwave_radiation_sum&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch&timezone=auto')
    apiJson = apiCall.text
    data = json.loads(apiJson)
    #dataList.append(data['daily']['temperature_2m_mean'][0],data['daily']['sunshine_duration'][0],data['daily']['precipitation_sum'][0],data['daily']['wind_speed_10m_max'][0],data['daily']['shortwave_radiation_sum'][0])
    outputStr = (month + ',' + str(data['daily']['temperature_2m_mean'][0]) + ',' + str(data['daily']['sunshine_duration'][0]) + ',' + str(data['daily']['precipitation_sum'][0]) + ',' + str(data['daily']['wind_speed_10m_max'][0]) + ',' + str(data['daily']['shortwave_radiation_sum'][0]) +"\n")
    print(outputStr)
    output.write(outputStr)
    
    year += 1
    #print('end')
