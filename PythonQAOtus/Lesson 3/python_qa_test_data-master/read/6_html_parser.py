import requests

from html.parser import HTMLParser

r = requests.get("https://www.habr.com")

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print("Start tag:", tag)
        for attr in attrs:
            print("     attr:", attr)

    def handle_endtag(self, tag):
        print("End tag :", tag)

    def handle_data(self, data):
        print(data)

parser = MyHTMLParser()

parser.feed(r.text)
