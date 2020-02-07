import requests
from bs4 import BeautifulSoup
from Article import Article

science_daily_AI_url = 'https://www.sciencedaily.com/news/computers_math/artificial_intelligence'
science_daily = 'https://www.sciencedaily.com'


def get_page_html(url):

    result = requests.get(url, headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    }).text
    page_soup = BeautifulSoup(result, 'html.parser')
    return page_soup


def scrape_for_top_title():
    page_soup = get_page_html(
        'https://www.sciencedaily.com/news/computers_math/artificial_intelligence')

    title_html_element = page_soup.find(id='featured_tab_1')

    return title_html_element.h3.a.text


def scrape_for_top_sum():
    page_soup = get_page_html(
        'https://www.sciencedaily.com/news/computers_math/artificial_intelligence')

    title_html_element = page_soup.find(id='featured_tab_1')

    # print(title_html_element)

    more_link = title_html_element.find(
        class_='latest-summary').find(class_='more').a['href']

    more = science_daily + more_link

    soup_2 = get_page_html(more)

    return soup_2.find(id='abstract').text


def scrape_for_top_link():
    page_soup = get_page_html(
        'https://www.sciencedaily.com/news/computers_math/artificial_intelligence')

    title_html_element = page_soup.find(id='featured_tab_1')

    summary_html_element = title_html_element.find(
        'div', class_='latest-summary').find('span', class_='more').a

    summary_link = summary_html_element['href']
    more_url = science_daily + summary_link

    page_soup2 = get_page_html(more_url)
    link_ref = page_soup2.find(id='story_source').a['href']

    return link_ref


def scrape_for_search(*args):
    # git branch test

    more_URLs = []
    headlines = []
    summaries = []
    sources = []
    articles = []
    final_articles = []

    page_soup = get_page_html(
        'https://www.sciencedaily.com/news/computers_math/artificial_intelligence')

    latest_summs_div = page_soup.find(id='summaries').find_all(
        'div', class_='latest-summary')

    featured_summs = page_soup.find(id='featured_shorts').find_all('li')

    latest_heads = page_soup.find(id='summaries').find_all(
        'h3', class_='latest-head')

    for sums in latest_summs_div:
        URL = science_daily + sums.find('span', class_='more').a['href']

        more_URLs.append(URL)

    for sums in featured_summs:
        URL = science_daily + sums.find('a')['href']
        more_URLs.append(URL)

    for more in more_URLs:
        page_soup_2 = get_page_html(more)

        headline = page_soup_2.find(
            'h1', class_='headline')
        headlines.append(headline.text)

        summary = page_soup_2.find(id='abstract')
        summaries.append(summary.text)

        source = page_soup_2.find(
            'div', id='story_source').find('a')['href']
        sources.append(source)

    for h, s, l in zip(headlines, summaries, sources):
        articles.append(Article(h, s, l))

    for a in articles:
        if all(word in a.title for word in args):
            final_articles.append(Article(a.title.title(), a.summary, a.link))

    return final_articles


# scrape_for_search('thermoplastic')  # for testing only
# scrape_for_top_title()
# scrape_for_top_sum()
# scrape_for_top_link()
