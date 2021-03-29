"""Data downloader"""
from __future__ import absolute_import

import requests


# Constant variables
URL = 'https://public.opendatasoft.com/explore/dataset/titanic-passengers/download/?format=csv' \
    '&timezone=Europe/Berlin&lang=fr&use_labels_for_header=true&csv_separator=%3B'

PATH = 'src/titanic.csv'

CHUNK_SIZE = 1000

# Function definition
def download_data(url: str=URL, path: str=PATH, chunksize: int=CHUNK_SIZE) -> None:
    """Download the titanic dataset from the OpendataSoft website

    Args:
        url (str, optional): The URL to download the data. Defaults to URL.
        path (str, optional): The path where to write the file. Defaults to PATH.
        chunksize (in, optional): The size of downloaded chunks. Defaults to CHUNK_SIZE.
    """
    print('# Downloading data ...', end='\t')
    response = requests.get(url, allow_redirects=True, stream=True)

    with open(path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=chunksize):
            if chunk:
                file.write(chunk)

    print('Done !')
