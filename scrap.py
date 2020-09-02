import bs4
import requests
import re
import time


print ('done')

url1 = "https://chem.libretexts.org/Bookshelves/Ancillary_Materials/Reference/Reference_Tables/Atomic_and_Molecular_Properties/A3%3A_Covalent_Radii"

response = requests.get(url1)

soup1 = bs4.BeautifulSoup(response.text, 'lxml')

url2 = 'https://chem.libretexts.org/Bookshelves/Ancillary_Materials/Reference/Reference_Tables/Atomic_and_Molecular_Properties/A2%3A_Electronegativity_Values'

'''
response = requests.get(url2)

soup2 = bs4.BeautifulSoup(response.text, 'lxml')

url3 = 'https://chem.libretexts.org/Bookshelves/Ancillary_Materials/Reference/Reference_Tables/Atomic_and_Molecular_Properties/A4%3A_Atomic_Weights_and_Isotope_Composition'

response = requests.get(url3)

soup3 = bs4.BeautifulSoup(response.text, 'lxml')

url4 = 'https://en.wikipedia.org/wiki/Ionic_radius'

response = requests.get(url4)

soup4 = bs4.BeautifulSoup(response.text, 'lxml')
'''

properties = {}

search = soup1.td

#print (search,'\n', str(search),'\n', re.compile('Atomic').search(search))
print (search.string)

print ([name.name for name in search.parents if name.name == 'tbody'])

def scrap_table (soup):
    if [name for name in soup.parents if name.name == 'tbody'] is None:
        soup = soup.next_element
        return scrap_libre(soup)
    else:




scrap_table(search)

print (properties)
