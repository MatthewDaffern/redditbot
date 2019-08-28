from Common import *
from log import *
import new_Common
import time
from authenticator import authenticate
import functools
import re


def timer(int_input):
    initial_time = time.time()
    while time.time() - initial_time < int_input:
        True
    return None


def api():
    api_file = open('api.key', 'r+')
    key = api_file.readlines()[0]
    return key


def fullname_creator(comment_object):
    initial_fullname = str(comment_object.fullname)
    initial_fullname_array = initial_fullname.split('_')
    final_fullname = str(initial_fullname_array[1])
    return final_fullname


def reply_function(comment_id_input, api_input, reddit_object_input):
    for i in new_Common.command_list():
        if re.match(i, comment_id_input.body) is not None:
            i.mark_read()
            comment_fullname = fullname_creator(i)
            unread_comment = reddit_object_input.comment(id=comment_fullname)
            result = new_Common.command_processor(i.body, api_input)
            unread_comment.reply(result)
            i.save()
            return None
    return 'No command found'


def list_creator(reddit_object_input):
    unread = list(reddit_object_input.inbox.unread(limit=None))
    saved = list(reddit_object_input.redditor('scripture_bot').saved(limit=10))

    def saved_test(comment_input):
        if comment_input in saved:
            return True
        else:
            return False
    return list(filter(saved_test, unread))


def main():
    reddit_object = authenticate()
    configured_processor = functools.partial(reply_function, api_input=api(), reddit_object_input=reddit_object)
    list(map(lambda x: configured_processor(comment_id_input=x), list_creator(reddit_object)))


# Uncomment this if you want to run the bot locally and activate the script by executing scripture_bot.py


if __name__ == '__main__':
    while True:
        timer(300)
        main()


