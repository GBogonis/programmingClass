import requests
import json


'''
1668970400
1637434400
1605898400
1574276000
1574276000
1511204000
1479668000
1448045600
1416509600
1384973600
'''

apiCall = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=42.82642299955682&lon=-71.57923160207767&units=imperial&appid=15dfa1324b44123c1634401424dd71a1')
#apiCall = requests.get('https://api.openweathermap.org/data/3.0/onecall/timemachine?lat=42.82642299955682&lon=-71.57923160207767&dt=1668970400&appid=15dfa1324b44123c1634401424dd71a1')
print('code:', apiCall.status_code)
apiJson = apiCall.text
data = json.loads(apiJson)

print(data['name'])

print(data)
