from Common import *
from log import *
from new_Common import *
import time
from authenticator import authenticate
import functools
import new_scripture_bot
import functools


api_key = new_scripture_bot.api()

print(api_key)


reddit_object = authenticate()
print(reddit_object)

comment_list = new_scripture_bot.list_creator(reddit_object)

print(comment_list)
