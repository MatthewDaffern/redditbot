import praw


def authenticate():
    reddit_instance = praw.Reddit(client_id='CLIENT_ID',
                                  client_secret='CLIENT_SECRET',
                                  password='PASSWORD',
                                  user_agent='USER_AGENT',
                                  username='USERNAME')
    return reddit_instance
