# import requests
# api_url ='https://api.ipify.org?format=json'
# response = requests.get(api_url)
#print(response.status_code)
#print(response.json())

#if response.status_code == 200:
  #  data = response.json()
    #print(data)
    #print(response.json())


import requests
api_url ="https://api.ipify.org?format=json"
r = requests.get(api_url)
# print(r.status_code)
# print(r.json())

#fancy:
#if r.status_code == 200:
    #print(r.json())
#MOST FANCY:
# if r.status_code == 200:
    # data = r.json()
    # print(data)
#over fancy
if r.status_code == 200:
    data = r.json()
    ip = data.get('ip')
    print('My Ip address is: ', ip)



