import praw


def authenticate():
    reddit_instance = praw.Reddit(client_id='ID',
                                  client_secret='SECRET',
                                  password='PASSWORD',
                                  user_agent='agent',
                                  username='bot name')
    return reddit_instance
