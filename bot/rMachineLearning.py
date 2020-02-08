import praw

file1 = open('config.txt', 'r+')
lines = file1.readlines()

reddit = praw.Reddit(client_id='shhh',
                     client_secret='sshhhhhhhhhh', password='sh',
                     user_agent='AINewsScraper', username='AlfaXBotUser')


rML = reddit.subreddit('MachineLearning')

for submission in rML.new(limit=100):
    title = submission.title
    if title.startswith('[R]'):
        print(title)
