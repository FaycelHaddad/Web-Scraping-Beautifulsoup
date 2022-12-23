# Imports
from IPython.core.display import display, HTML
import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
%matplotlib inline
# MUBAWAB's homepage
mubawab_url = 'https://www.mubawab.tn/fr/st/la-marsa/appartements-a-vendre:tw:75763'
# Use requests to retrieve data from a given URL
mubawab_response = requests.get(mubawab_url)
# Parse the whole HTML page using BeautifulSoup
mubawab_soup = BeautifulSoup(mubawab_response.text, 'html.parser')
price_list = []

price = mubawab_soup.find('span',{'class':'priceTag hardShadow float-right floatL yellowBg'})
price_list.append(price.text.replace(u'\xa0',' ').replace(u'TND','').strip().split('|'))

for price in mubawab_soup.findAll('span',{'class':'priceTag hardShadow float-right floatL'}):
    price_list.append(price.text.replace(u'\xa0',' ').replace(u'TND','').strip().split('|'))
print(price_list)

surface_list = []
for surface in mubawab_soup.findAll('div',{'class':'inBlock w100'}):
    surface_list.append(surface.text.replace(u'\xa0',' ').replace(u'TND','').strip().split('|'))
print(surface_list)

annonce_list = pd.DataFrame({'price' : [price_list],'surface' : [surface_list] })
annonce_list

annonce_list.to_csv('annonce_list.csv', index=False)
annonce_list.to_excel('annonce_list.xlsx', index=False)
