from Common import *
from log import *
import new_Common
from authenticator import authenticate
import functools
import re
import datetime
from time import sleep


def timer(int_input):
    return sleep(int_input)


def api():
    api_file = open('api.key', 'r+')
    key = api_file.readlines()[0]
    api_file.close()
    return key


def log_to_cloud_watch_input(comment_input):
    return print(str.join('', (comment_input, '\n', 
                               comment_input.body, '\n', 
                               str(datetime.date.today()))))


def log_to_cloud_watch_output(comment_input, reply_input):
    return print(str.join('', (str(comment_input), '\n', reply_input)))


def fullname_creator(comment_object):
    initial_fullname = str(comment_object.fullname)
    initial_fullname_array = initial_fullname.split('_')
    final_fullname = str(initial_fullname_array[1])
    return final_fullname


def reply_function(comment_id_input, api_input, reddit_object_input):
    print()
    for i in new_Common.command_list():
        if re.match(i, comment_id_input.body) is not None:
            log_to_cloud_watch_input(comment_id_input)
            i.mark_read()
            comment_fullname = fullname_creator(i)
            comment_id_string = fullname_creator(comment_id_input)
            unread_comment = reddit_object_input.comment(id=comment_id_string)
            result = new_Common.command_processor(i.body, api_input)
            unread_comment.reply(result)
            log_to_cloud_watch_output(comment_id_input, result)
            i.save()
            return None
    return 'No command found'


def list_creator(reddit_object_input):
    unread = set(reddit_object_input.inbox.unread(limit=None))
    saved = set(reddit_object_input.redditor('scripture_bot').saved(limit=10))
    return [x for x in unread if x not in saved]


def main():
    reddit_object = authenticate()
    configured_processor = functools.partial(reply_function, api_input=api(), reddit_object_input=reddit_object)
    list(map(lambda x: configured_processor(comment_id_input=x), list_creator(reddit_object)))


# Uncomment this if you want to run the bot locally and activate the script by executing scripture_bot.py


if __name__ == '__main__':
    while True:
        timer(300)
        main()


