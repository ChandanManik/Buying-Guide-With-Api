# from bs4 import BeautifulSoup
# import requests
# url = 'https://quotes.toscrape.com/' 
# r = requests.get(url) #variable set na thakle arguement ei '' bebohar korte hobe
# data = r.text
# soup = BeautifulSoup(data, 'html.parser') #print(soup) #must be add html.parser
# heading1 = soup.find('h1')
# print(heading1.text)  #want to see tag, add text in print area with variable

# link = soup.find('a') #link format understand with 'a'
# print(link.text) #want to like text format

# import requests    #multiple link tag wise scrap
# from bs4 import BeautifulSoup 
# url = 'https://quotes.toscrape.com/' #request url
# r = requests.get(url)
# data = r.text
# #soup =BeautifulSoup(r.text, 'html.parser') #directway
# soup = BeautifulSoup(data, 'html.parser') #variableway
# #print(soup.title.text) #titlecrack
# links = soup.findAll('a')
# for link in links:
#     #print(link.get('href'))
#     print('https://quotes.toscrape.com' + link.get('href'))


# from bs4 import BeautifulSoup
# import requests
# url = 'https://quotes.toscrape.com'
# r = requests.get(url)
# data = r.text
# #soup = (r.text, 'html.parser')
# soup = BeautifulSoup(data, "html.parser") #print(soup.text)
# links = soup.findAll('a')  #[for list we will for loop] print(links) check
# for link in links:
#     #print(link) #show data with a
#     #print(link.text) #show data text popup
#     #print(link.get('href')) #show data with tag
#     #print('https://quotes.toscrape.com' + link.get('href'))


#scrap sitemap https://www.discovermagazine.com/ use = sitemap.xml
from bs4 import BeautifulSoup as b
import requests
url = 'https://www.discovermagazine.com/sitemap/article/environment/1.xml'   #'https://www.discovermagazine.com/sitemap.xml'
r = requests.get(url)
soup = b(r.text, 'html.parser')
locs = soup.findAll('loc')
for lou in locs:
    #print(locs)
    print(lou.text)


