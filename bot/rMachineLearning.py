import praw
import json
from Article import Article

with open('myconfig.json', 'r') as myfile:
    data = myfile.read()
obj = json.loads(data)

reddit = praw.Reddit(client_id=str(obj["client_id"]),
                     client_secret=str(obj["client_secret"]), password=str(obj["password"]),
                     user_agent='AINewsScraper', username='AlfaXBotUser')
rML = reddit.subreddit('MachineLearning')

titles = []


def remove_dup(arr):
    final_list = []
    for num in arr:
        if num not in final_list:
            final_list.append(num)
    return final_list


def get_r_research_titles():
    for submission in rML.new(limit=500):
        title = submission.title
        if title.startswith('[R]'):
            titles.append(title.strip('[R]'))

        if title.startswith('[Research]'):
            titles.append(title.strip('[Research]'))

    return titles


def get_r_news_titles():
    for submission in rML.new(limit=500):
        title = submission.title
        if title.startswith('[N]'):
            titles.append(title.strip('[N]'))

        if title.startswith('[News]'):
            titles.append(title.strip('[News]'))

    return titles


def search_r_titles(*args):
    research_titles = map(lambda t: t.lower(),
                          get_r_research_titles() + get_r_news_titles())

    searched_titles = []
    articles = []

    for title in research_titles:
        if all(word in title for word in args):
            searched_titles.append(title.title())

    final_titles = remove_dup(searched_titles)

    for t in final_titles:
        articles.append(Article(t))

    return articles


search_r_titles('intel', 'habana')
