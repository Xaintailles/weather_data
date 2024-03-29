# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 16:51:18 2021

@author: Gebruiker

https://developer.dataplatform.knmi.nl/get-started
"""

import logging
import sys
from datetime import datetime
from pathlib import Path

import requests
import os
import json

with open(r'C:\Users\Calixte\Desktop\Secrets\secrets.json') as f:
    d_secrets = json.load(f)['KMI_API']

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel("INFO")

api_url = "https://api.dataplatform.knmi.nl/open-data"
api_version = "v1"

#https://api.dataplatform.knmi.nl/open-data/v1/datasets/Actuele10mindataKNMIstations/versions/2/files
#https://api.dataplatform.knmi.nl/open-data/v1/datasets/Tx1/versions/2/files


# Parameters
#api_key = d_secrets['KEY']
api_key = 'eyJvcmciOiI1ZTU1NGUxOTI3NGE5NjAwMDEyYTNlYjEiLCJpZCI6IjI4ZWZlOTZkNDk2ZjQ3ZmE5YjMzNWY5NDU3NWQyMzViIiwiaCI6Im11cm11cjEyOCJ9'
dataset_name = "Tx1"
dataset_version = "2"
max_keys = "10"

# Use list files request to request first 10 files of the day.
timestamp = datetime.utcnow().date().strftime("%Y%m%d")
start_after_filename_prefix = f"KMDS__OPER_P___10M_OBS_L2_{timestamp}"
list_files_response = requests.get(
    f"{api_url}/{api_version}/datasets/{dataset_name}/versions/{dataset_version}/files",
    headers={"Authorization": api_key},
    params={"maxKeys": max_keys, "startAfterFilename": start_after_filename_prefix},
)
list_files = list_files_response.json()

logger.info(f"List files response:\n{list_files}")
dataset_files = list_files.get("files")

# Retrieve first file in the list files response
filename = dataset_files[0].get("filename")
logger.info(f"Retrieve file with name: {filename}")
endpoint = f"{api_url}/{api_version}/datasets/{dataset_name}/versions/{dataset_version}/files/{filename}/url"
get_file_response = requests.get(endpoint, headers={"Authorization": api_key})
if get_file_response.status_code != 200:
    logger.error("Unable to retrieve download url for file")
    logger.error(get_file_response.text)
    sys.exit(1)

download_url = get_file_response.json().get("temporaryDownloadUrl")
dataset_file_response = requests.get(download_url)
if dataset_file_response.status_code != 200:
    logger.error("Unable to download file using download URL")
    logger.error(dataset_file_response.text)
    sys.exit(1)

# Write dataset file to disk
p = Path(filename)
p.write_bytes(dataset_file_response.content)
logger.info(f"Successfully downloaded dataset file to {p}")


