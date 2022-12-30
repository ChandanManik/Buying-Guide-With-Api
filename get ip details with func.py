import requests
def response_data(url):
    r= requests.get(url)
    if r.status_code ==200:
        data = r.json()
    return data

api_find_url = "https://api.ipify.org?format=json"
datas = response_data(api_find_url)
ip = datas.get('ip')

ip_locaion_url = f"https://ipapi.co/{ip}/json/"
database = response_data(ip_locaion_url)
city = database.get('city')
region = database.get('region')
country = database.get('country')

sentence = f"ip ({ip}) is located in {city} {region}, {country}."
print(sentence)
    


    
