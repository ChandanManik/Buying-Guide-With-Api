# import requests
# api_find_url = "https://api.ipify.org?format=json"
# r = requests.get(api_find_url)
# if r.status_code == 200:
#     data = r.json()
#     ip = data.get('ip')

# ip_location_url = f"https://ipapi.co/{ip}/json/"
# re = requests.get(ip_location_url)
# if re.status_code == 200:
#     ip_details = re.json()
#     city = ip_details.get('city')
#     country = ip_details.get('country')

#     sentence = f"ip ({ip}) is located in {city} {region}, {country}."
#     print(sentence)

# # ip is located in Chittagong, Bangladesh.


# import requests
# api_find_url = "https://api.ipify.org?format=json"
# response = requests.get(api_find_url)

# if response.status_code == 200:
#     data = response.json()
#     ip = data.get('ip')

# ip_location_url = f"https://ipapi.co/{ip}/json/"
# re = requests.get(ip_location_url)
# if re.status_code ==200:
#     data = re.json()
#     city = data.get('city')
#     country = data.get ('country')
#     sentence= f"ip{ip} is located in {city} {region} , {country}"
#     print(sentence)

