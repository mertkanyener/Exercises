import requests
from bs4 import BeautifulSoup

#loading content from the desired URL
base_url = 'http://www.nytimes.com'
r = requests.get(base_url)

#Decoding webpage
soup = BeautifulSoup(r.text)

#find and loop through all elements on the page with the
#class name "story-heading"
for i in soup.find_all(class_="story-heading"):
    if i.a:
        print(i.a.text.replace("\n", " ").strip())
    else:
        print(i.contents[0].strip())






