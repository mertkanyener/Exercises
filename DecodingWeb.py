import requests
from bs4 import BeautifulSoup

#loading content from the desired URL
base_url = 'http://www.nytimes.com'
r = requests.get(base_url)

