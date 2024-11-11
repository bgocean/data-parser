import requests
from bs4 import BeautifulSoup as bs4

headers = {
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
}

url = "https://itproger.com/"
session = requests.Session()
req = session.get(url, headers=headers)
if req.status_code == 200:
    print("Ok")

# 15.30 video