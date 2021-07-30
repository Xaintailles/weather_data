# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 16:51:18 2021

@author: Gebruiker
"""


import requests
import json

with open("credentials.json") as json_file:
        json_credentials = json.load(json_file)



headers = {"Authorization": json_credentials['OpenData']}

r = requests.get('https://api.dataplatform.knmi.nl/open-data/v1/datasets/Tn1/versions/2/files'
                 , headers = headers)

test = r.json()