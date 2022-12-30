#short
from requests import get
from pprint import pprint
#import requests
#sundor kore code explain korar jonno
#import pprint
key = 'a4ee02062bdefde65da7ff388bffc9d5'
city= 'Dhaka'
api_url = f'https://api.openweathermap.org/data/2.5/weather?q={city},&appid={key}&units=metric'

# print(api_url)

#response = requests.get(api_url)
response = get(api_url)

#print(response.status_code)
#print(response.json())

api_data = response.json()
country_name = api_data.get('sys').get('country')
weather_data =api_data.get('main')
feels_like = weather_data.get('feels_like')
temp = weather_data.get('temp')
print(country_name, temp, feels_like)
#print(country_name)
#pprint.pprint(api_data)
#pprint(api_data)
#pprint(weather_data)



