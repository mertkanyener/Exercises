import requests
from bs4 import BeautifulSoup


def decode_web():
    base_url = "www.nytimes.com"
    r = requests.get(base_url)
    soup = BeautifulSoup(r.text)
    titles = open('titles.txt', 'w')
    titles.write("Here are the all article titles of nytimes:")

    for i in soup.find_all(class_="story-heading"):
        if i.a:
            titles.write(i.a.text.replace("\n", " ").strip())
        else:
            titles.write(i.contents[0].strip())
    titles.close()

