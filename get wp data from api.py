from pprint import pprint
from httpx import get
base_url = 'https://www.cocooncityhostel.com/wp-json/wp/v2'

#page_api = f'{base_url}/pages?per_pages=10'
page_api = f'{base_url}/pages?page=3'
r = get(page_api)
api_data =r.json()

for page in api_data:
    try:
        print(page.get('link'))
    except:
        print('page not found')

