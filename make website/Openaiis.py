#get data from api 93 video pixbay email: kaxawa1136@irebah.com pass: 123Google123
# import openai

# openai.api_key = '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'
# prompt = input('enter your command: ')

# response = openai.Completion.create(
#   model="text-davinci-003",
#   prompt= prompt,
#   temperature=0.7,
#   max_tokens=256,
#   top_p=1,
#   frequency_penalty=0,
#   presence_penalty=0
# )

# texts = response.get('choices')[0].get('text')
# print(texts)



#98 wordpress rest api end points by reference  
#https://developer.wordpress.org/rest-api/reference/
#sample page #https://cu.ac.bd/museum/ or #https://www.cocooncityhostel.com/wp-json

#getpost

# import requests
# from pprint import pprint
# url ='https://www.searchenginejournal.com/wp-json/wp/v2'
# post_api = f'{url}/posts'
# r = requests.get(post_api)
# pprint(r.json())

#getpage api

# from httpx import get
# from pprint import pprint

# url = 'https://www.searchenginejournal.com/wp-json/wp/v2'
# pages_apis = f'{url}/pages'
# r = get(pages_apis)
# api_data = r.json()
# for page in api_data: 
#     print(page.get('link'))
#pprint(r.json()) #pprint(data)


#99 getwordpress data from api-99
#perpage= #https://www.searchenginejournal.com/wp-json/wp/v2/pages?per_page=1

# from httpx import get
# from pprint import pprint

# url = 'https://www.searchenginejournal.com/wp-json/wp/v2'
# pages_apis = f'{url}/pages?per_page=5'
# r = get(pages_apis)
# api_data = r.json()
# for page in api_data: #jodi page na thake thokon try and except deya lagbe. 
#     try:
#         print(page.get('link'))
#     except:
#         print('page not here')

#100 write to text file r= read, w= write, a= append(new line), \n= space
#homework remove \ to read file ?

# text = 'who are you 3?'
# file = open('love.text', 'a')
# file.writelines(text + '\n')
# file.close()

# import httpx
# ur_list = [
#     'https://www.searchenginejournal.com/what-is-chatgpt/473664/',
#     'https://www.searchenginejournal.com/target-multiple-cities-seo/469609/',
#     'https://www.searchenginejournal.com/competitors-seo-strategies/473258/'
# ]

# for url in ur_list:
#     r = httpx.get(url)
#     text = f'{url}------------{r.status_code}'
#     file = open('link.text', 'a+')
#     file.writelines(text + '\n')
#     file.close()

#     #read will be try 


#101: PIXBABY API (Images url to text file)

# from requests import get
# from pprint import pprint
# ap_key = '32393458-849f7ba227160d99660b4355b'
# query = 'yellow+flowers'
# api_url = f'https://pixabay.com/api/?key={ap_key}&q={query}'

# r = get(api_url) #print(r.status_code)
# api_data = r.json().get('hits') #pprint(api_data)

# for datas in api_data:
#     imag_url = datas.get('webformatURL') #print(imag_url)
#     file = open('ima.text','a+')
#     file.writelines(imag_url +'\n')
#     file.close()

#104 Download Image

