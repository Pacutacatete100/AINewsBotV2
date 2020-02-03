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


def scrape_for_top_title():
    page_soup = get_page_html(
        'https://www.sciencedaily.com/news/computers_math/artificial_intelligence')

    title_html_element = page_soup.find("div", {"id": "featured_tab_1"})
    title = title_html_element.find("h3", "latest-head").text

    return title


def scrape_for_top_sum():
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


def scrape_for_top_link():
    page_soup = get_page_html(
        'https://www.sciencedaily.com/news/computers_math/artificial_intelligence')

    title_html_element = page_soup.find("div", {"id": "featured_tab_1"})

    summary_html_element = title_html_element.find(
        "div", "latest-summary").find("span", "more").find("a")
    summary_link = summary_html_element["href"]
    more_url = science_daily + summary_link

    page_soup2 = get_page_html(more_url)
    link_ref = page_soup2.find("div", {"id": "story_source"}).find("a")
    link = link_ref["href"]

    return link


def scrape_for_search(*args):

    titles = []
    summaries = []
    final_titles = []
    final_summaries = []
    html_summaries_links = None

    page_soup = get_page_html(
        'https://www.sciencedaily.com/news/computers_math/artificial_intelligence')

    html_titles = page_soup.find_all("h3", "latest-head")
    for element in html_titles:
        titles.append(element.text)

    for word in args:
        for title in titles:
            if word in title:
                final_titles.append(title)

    return final_titles


# TODO: finish scraping site for elements, use github of old bot as reference
scrape_for_search("Quantum")  # for testing only

# html_summaries = page_soup.find_all("div", "latest-summary")

# for summ in html_summaries:
#     html_summaries_links = science_daily + \
#         summ.find("span", "more").find("a")["href"]
#     summaries.append(html_summaries_links)

# for summary in summaries:
#     page_soup_2 = get_page_html(summary)
#     final_summaries.append(page_soup_2.find("div", {"id": "story_text"}).find(
#         "p", {"id": "first"}).text)
