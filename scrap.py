import bs4
import requests
import re
import time


print ('done')

url = 'https://www.mobygames.com/browse/games/offset,0/so,0a/list-games/'

response = requests.get(url)
print (response.url, '\n', response)

soup = bs4.BeautifulSoup(response.text, 'lxml')

print (len(soup.tbody))


for href in soup.tbody:
    print (href)
