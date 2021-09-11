import praw


def authenticate():
    reddit_instance = praw.Reddit(client_id='FUlMD-cKILpnUA',
                                  client_secret='bkZH3og2C2x8_IpqDD-mFCTOseA',
                                  password='1%YjQ%*xP5lrJcpF5lD^',
                                  user_agent='scripture_bot',
                                  username='scripture_bot')
    return reddit_instance
