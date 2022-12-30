from bs4 import BeautifulSoup
import requests
url = 'https://www.discovermagazine.com/sitemap/article/environment/1.xml'
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data, 'html.parser')
# headings = soup.find('h1')
# print(headings.text)
# links = soup.find('a')#single link
# print(links.text)
locs = soup.findAll('loc')
for lou in locs:
    #print(locs)
    print(lou.text)
# for link in multiple:
#     print(link.text)
#     #print('https://quotes.toscrape.com' + link.get('href')) 