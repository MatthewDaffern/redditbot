
import praw
import authenticator
from authenticator import authenticate
'''
def authenticate():
    reddit_instance = praw.Reddit(client_id='FUlMD-cKILpnUA',
                                  client_secret='bkZH3og2C2x8_IpqDD-mFCTOseA',
                                  password='1%YjQ%*xP5lrJcpF5lD^',
                                  user_agent='scripture_bot',
                                  username='scripture_bot')
    return reddit_instance
'''

scripture_bot_object = authenticate()


print(scripture_bot_object.user.me())

print('the reddit bot object is '+str(scripture_bot_object))
'''
unread_messages = scripture_bot.unread_generator(scripture_bot_object)

print('the unread message object is '+str(unread_messages))
'''
unread = scripture_bot_object.inbox.unread(limit=None)
for i in unread:
    print(i.body)
for i in scripture_bot_object.inbox.unread(limit=None):
    print(i.body)
    print(i.author)
    print(i.fullname)


'''
for i in unread_messages:
    print(unread_messages)

'''
