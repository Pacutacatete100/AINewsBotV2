import requests
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup

science_daily_url = 'https://www.sciencedaily.com/news/computers_math/artificial_intelligence/'

req = Request(science_daily_url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
page_soup = soup(webpage, "html.parser")


def scrape_for_title():
    titles = page_soup.findAll("div", {"id": "featured_tab_1"})
    for title in titles:
        latest_head = page_soup.find("h3", "latest-head")
        print(latest_head.text)


scrape_for_title()

# TODO: finish scraping site for elements, use github of old bot as reference
