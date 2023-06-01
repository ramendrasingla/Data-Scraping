import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen, HTTPError

url = "https://sgmagazine.com/category/dining/"
hdr = {'User-Agent': 'Mozilla/5.0'}
req = Request(url,headers=hdr)
soup = BeautifulSoup(urlopen(req))

# title = soup.title
# print(title)
# print(title.text)

# print(soup.find('div', class_="elementor-widget-container"))
print(soup.find_all('div', class_="elementor-widget-container"))