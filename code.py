import os
import sys
import requests
from bs4 import BeautifulSoup


class Quotes(object):
    def __init__(self):
        pass

    def get_data(self, p=1):
        data = {"status_code": "ok", "data": {}}
        res = requests.get(url="http://quotes.toscrape.com/page/{0}/".format(str(p)))
        data["status"] = res.status_code
        soup = BeautifulSoup(res.content)
        for link_idx, link in enumerate(soup.find_all("div", attrs={"class": "quote"})):
            quote_text = link.find("span", attrs={"class": "text", "itemprop": "text"})
            quote_author = link.find("small", attrs={"class": "author", "itemprop": "author"})
            quote_tags = link.find_all("a", attrs={"class": "tag"})
            data["data"][link_idx] = {"qoute_text": quote_text.text, "quote_author": quote_author, "quote_tags": [_qt_.text for _qt_ in quote_tags]}
        return data

if __name__ == "__main__":
    _Quotes = Quotes()
    print(_Quotes.get_data())