# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 20:11:49 2023

@author: Calixte
"""
#%% Packages
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import datetime
import locale
import helpers as h

#%% Creating the soup
#url of the page we want to scrape
url = 'https://www.buienradar.nl/weer/utrecht/nl/2745912/5daagse'

# initiating the webdriver. Parameter includes the path of the webdriver.
driver = webdriver.Chrome('./chromedriver') 
driver.get(url) 
  
# this is just to ensure that the page is loaded
time.sleep(5) 
  
html = driver.page_source

soup = BeautifulSoup(html, "html.parser")

#%% 

all_tables = soup.find_all('div', {'class': 'expanded-box'})

all_results = []

for table in all_tables:
    day = table.find('span', {'class': 'header-text'}).text
    for table_row in table.find_all('div', {'class': 'rtable-row rtable-row-hour'}):
        print(type(table_row))
        time = table_row.find('div', {'class': 'rtable-cell hour-time-cell'}).text
        temp = table_row.find('span', {'class': 'temperature'}).text
        all_results.append([datetime.datetime.now(),day,time,temp])

results = pd.DataFrame(all_results, columns = ['Scrapped_time_stamp','Day', 'Time', 'Temp'])

new_date = []

#To do, fix the function that is supposed to clean the date, see the helper file
for dutch_day in results['Day']:
    print(dutch_day.find('Maandag'))


    
