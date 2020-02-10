import praw
import json
from Article import Article
import sys

with open('myconfig.json', 'r') as myfile:
    data = myfile.read()
obj = json.loads(data)

reddit = praw.Reddit(client_id=str(obj["client_id"]),
                     client_secret=str(obj["client_secret"]), password=str(obj["password"]),
                     user_agent='AINewsScraper', username='AlfaXBotUser')
rML = reddit.subreddit('MachineLearning')


def remove_dup(arr):
    final_list = []
    for num in arr:
        if num not in final_list:
            final_list.append(num)
    return final_list


def get_r_research_titles():

    articles = []
    summaries = []
    titles = []

    for submission in rML.new(limit=100):
        title = submission.title
        if title.startswith('[R]'):
            titles.append(title.strip('[R]'))
            summaries.append(submission.selftext)

        if title.startswith('[Research]'):
            titles.append(title.strip('[Research]'))
            summaries.append(submission.selftext)

    for t, s in zip(titles, summaries):
        articles.append(Article(t, s))

    return articles  # returns list of articles with only title and summary


def get_r_news_titles():

    articles = []
    summaries = []
    titles = []

    for submission in rML.new(limit=100):

        if submission.title.startswith('[N]'):
            titles.append(submission.title.strip('[N]'))
            summaries.append(submission.selftext)

        if submission.title.startswith('[News]'):
            titles.append(submission.title.strip('[News]'))
            summaries.append(submission.selftext)

    for t, s in zip(titles, summaries):
        articles.append(Article(t, s))

    return articles  # returns list of articles with only title and summary


def search_r_titles(*args):

    research = get_r_research_titles()
    news = get_r_news_titles()

    articles = research + news
    final_articles = []

    for a in articles:
        if all(word in a.title.lower() for word in args):
            final_articles.append(a)

    return final_articles


search_r_titles('unlearning')
