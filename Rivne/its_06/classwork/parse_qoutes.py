import requests
from bs4 import BeautifulSoup
from datetime import datetime
from pprint import pprint


def get_response(url):
    response = requests.get(URL)
    text = BeautifulSoup(response.text, 'lxml')
    return text


URL = "https://quotes.toscrape.com/"
quotes_list = []
page = 1

while True:
    soup = get_response(f"{URL}/page/{page}/")
    quotes = soup.find_all('span', class_="text")
    if len(quotes) == 0: break
    page += 1
    authors = soup.find_all('small', class_="author")

    # tags = soup.find_all('div', class_="tags")

    for i in range(0, len(quotes)):
        quote = {"quote": quotes[i].text, "author": authors[i].text,
                 "author_info": URL + authors[i].find_next_sibling().get('href')[1:]}
        quotes_list.append(quote)


quotes_list = sorted(quotes_list, key=lambda quotes_list: quotes_list['author'])
# pprint(quotes_list)

authors_list = []

for i, item in enumerate(quotes_list):
    if i > 0 and quotes_list[i]["author"] == quotes_list[i-1]["author"]: continue
    soup = get_response(item["author_info"])
    author = {"name": soup.find('h3', class_="author-title").text,
              "born": soup.find('span', class_="author-born-date").text,
              "location": soup.find('span', class_="author-born-location").text,
              "description": soup.find('div', class_="author-description").text}
    authors_list.append(author)

pprint(authors_list[0])