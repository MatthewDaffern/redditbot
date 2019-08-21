from Common import *
from log import *
import new_Common

def fullname_creator(comment_object):
    initial_fullname = str(comment_object.fullname)
    initial_fullname_array = initial_fullname.split('_')
    final_fullname = str(initial_fullname_array[1])
    return final_fullname


def reply_function(reddit_object, comment_fullname_function, api_call_function):
    for i in reddit_object.inbox.unread(limit=None)
        list_of_saved = reddit_object.redditor('scripture_bot').saved()
        for comments in list_of_saved:
            if str(i) == str(comments):
                return 'already responded to the redditor'
        if "scripture_bot!" not in i.body:
            i.mark_read()
            return malformed_request(i.author, i.body, i)
            i.save()
        if "scripture_bot!" in i.body:
            i.mark_read()
            comment_fullname = comment_fullname_function(i)
            unread_comment = reddit_object.comment(id=comment_fullname)
            result = new_Common.command_processor(i.body, api_call_function())
            unread_comment.reply(result)
            i.save()


def the_actual_bot(authentication, fullname_creator_func, reply_function):
    reddit_object = authentication
    reply_function(reddit_object, fullname_creator_func, query_processor, requests_object_caller)

# Uncomment this if you want to run the bot locally and activate the script by executing scripture_bot.py

# from authenticator import authenticate
# while 1 == 1:
#    the_actual_bot(authenticate(), fullname_creator, reply_function)


# pdb.runcall(the_actual_bot(authenticate(), unread_generator, fullname_creator, reply_function_and_error_logging))

