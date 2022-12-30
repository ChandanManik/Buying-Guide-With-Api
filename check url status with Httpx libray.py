# import httpx
# from pprint import pprint
# key = 'a4ee02062bdefde65da7ff388bffc9d5'
# city= 'Dhaka'
# api_url = f'https://api.openweathermap.org/data/2.5/weather?q={city},&appid={key}&units=metric'

# r = httpx.get(api_url)
# pprint(r.json())

#url: use for loop
import httpx
url_list = [
    'https://www.dogfoodadvisor.com/best-dog-foods/best-dry-dog-foods/',
    'https://www.dogfoodadvisor.com/best-dog-foods/',
    'https://www.nbcnews.com/select/shopping/best-dog-food-ncna1189551',
    'https://nypost.com/article/best-dog-food-brands-per-veterinarians/',
    'https://www.thesprucepets.com/best-dog-food-brands-4843452'
]
for url in url_list:
    res = httpx.get(url)
    print(url, res.status_code, sep ="........")