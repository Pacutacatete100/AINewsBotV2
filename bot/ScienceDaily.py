import requests
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
x = 0

science_daily_AI_url = 'https://www.sciencedaily.com/news/computers_math/artificial_intelligence'
science_daily = "https://www.sciencedaily.com"


def get_page_html(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    page_soup = soup(webpage, "html.parser")
    return page_soup


def scrape_for_title():
    page_soup = get_page_html(
        'https://www.sciencedaily.com/news/computers_math/artificial_intelligence')

    title_html_element = page_soup.find("div", {"id": "featured_tab_1"})
    title = title_html_element.find("h3", "latest-head").text

    return title


def scrape_for_sum():
    page_soup = get_page_html(
        'https://www.sciencedaily.com/news/computers_math/artificial_intelligence')

    title_html_element = page_soup.find("div", {"id": "featured_tab_1"})

    summary_html_element = title_html_element.find(
        "div", "latest-summary").find("span", "more").find("a")
    summary_link = summary_html_element["href"]
    more_url = science_daily + summary_link

    page_soup2 = get_page_html(more_url)

    summary = page_soup2.find("div", {"id": "story_text"}).find(
        "p", {"id": "first"}).text

    return summary

# TODO: finish scraping site for elements, use github of old bot as reference
