# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 16:51:18 2021

@author: Gebruiker
"""


import requests
import json
from datetime import datetime

with open("credentials.json") as json_file:
        json_credentials = json.load(json_file)

root = 'https://api.dataplatform.knmi.nl/open-data'
version_id = 2
dataset_name = 'Actuele10mindataKNMIstations'
extension = f'/v1/datasets/{dataset_name}/versions/{version_id}/files'

url = str(root) + str(extension)

headers = {"Authorization": json_credentials[dataset_name]}

max_keys = str(10)

timestamp = datetime.utcnow().date().strftime("%Y%m%d")
start_after_filename_prefix = f"KMDS__OPER_P___10M_OBS_L2_{timestamp}"

r = requests.get(url = url
                 ,headers = headers
                 ,params={"maxKeys": max_keys, "startAfterFilename": start_after_filename_prefix} 
                 )

test = r.json()
