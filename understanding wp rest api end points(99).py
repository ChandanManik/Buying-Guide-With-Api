#import httpx
from pprint import pprint
from httpx import get
base_url = 'https://www.cocooncityhostel.com/wp-json/wp/v2'


#get post

# post_api = f'{base_url}/posts'
# r = httpx.get(post_api)

#page

page_api = f'{base_url}/pages'
r = get(page_api)

#print(r.status_code)
#pprint(r.json())
#link:
api_data = r.json()
for page in api_data:
    print(page.get('link'))