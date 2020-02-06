import requests
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
from Article import Article

science_daily_AI_url = 'https://www.sciencedaily.com/news/computers_math/artificial_intelligence'
science_daily = 'https://www.sciencedaily.com'


def get_page_html(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    page_soup = soup(webpage, 'html.parser')
    return page_soup


def scrape_for_top_title():
    page_soup = get_page_html(
        'https://www.sciencedaily.com/news/computers_math/artificial_intelligence')

    title_html_element = page_soup.find('div', {'id': 'featured_tab_1'})
    title = title_html_element.find('h3', 'latest-head').text

    return title


def scrape_for_top_sum():
    page_soup = get_page_html(
        'https://www.sciencedaily.com/news/computers_math/artificial_intelligence')

    title_html_element = page_soup.find('div', {'id': 'featured_tab_1'})

    summary_html_element = title_html_element.find(
        'div', 'latest-summary').find('span', 'more').find('a')
    summary_link = summary_html_element['href']
    more_url = science_daily + summary_link

    page_soup2 = get_page_html(more_url)

    summary = page_soup2.find('div', {'id': 'story_text'}).find(
        'p', {'id': 'first'}).text

    return summary


def scrape_for_top_link():
    page_soup = get_page_html(
        'https://www.sciencedaily.com/news/computers_math/artificial_intelligence')

    title_html_element = page_soup.find('div', {'id': 'featured_tab_1'})

    summary_html_element = title_html_element.find(
        'div', 'latest-summary').find('span', 'more').find('a')
    summary_link = summary_html_element['href']
    more_url = science_daily + summary_link

    page_soup2 = get_page_html(more_url)
    link_ref = page_soup2.find('div', {'id': 'story_source'}).find('a')
    link = link_ref['href']

    return link


def scrape_for_search(*args):

    more_URLs = []
    headlines = []
    summaries = []
    sources = []
    articles = []
    final_articles = []

    page_soup = get_page_html(
        'https://www.sciencedaily.com/news/computers_math/artificial_intelligence')

    latest_summs_div = page_soup.find(
        'div', {'id': 'summaries'}).find_all('div', 'latest-summary')

    latest_heads = page_soup.find(
        'div', {'id': 'summaries'}).find_all('h3', 'latest-head')

    for sums in latest_summs_div:
        more_URLs.append(
            science_daily + sums.find('span', 'more').find('a')['href'])

    for more in more_URLs:
        page_soup_2 = get_page_html(more)

        headline = page_soup_2.find('h1', 'headline').text
        headlines.append(headline.lower())

        summary = page_soup_2.find('dd', {'id': 'abstract'}).text
        summaries.append(summary)

        source = page_soup_2.find(
            'div', {'id': 'story_source'}).find('a')['href']
        sources.append(source)

    for h, s, l in zip(headlines, summaries, sources):
        articles.append(Article(h, s, l))

    for a in articles:
        if all(word in a.title for word in args):
            final_articles.append(Article(a.title.title(), a.summary, a.link))

    return final_articles


scrape_for_search('robot')  # for testing only
