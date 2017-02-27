import requests
from bs4 import BeautifulSoup


def decode_web():
    base_url = "https://www.nytimes.com"
    r = requests.get(base_url)
    soup = BeautifulSoup(r.text)
    titles = open('titles.txt', 'w')
    titles.write("Here are the all article titles of nytimes:\n")

    for i in soup.find_all(class_="story-heading"):
        if i.a:
            titles.write(i.a.text.replace("\n", " ").strip())
            titles.write("\n")
        else:
            titles.write(i.contents[0].strip())
            titles.write("\n")
    titles.close()

decode_web()