# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 20:11:49 2023

@author: Calixte
"""

import requests
from bs4 import BeautifulSoup

URL = 'https://www.buienradar.nl/weer/utrecht/nl/2745912'

page = requests.get(URL)

soup = BeautifulSoup(page.content)

results = soup.find_all(class_='rtable-cell hour-temperature-cell')

print(results)
