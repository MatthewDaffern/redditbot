from Common import *
from log import *


def fullname_creator(comment_object):
    initial_fullname = str(comment_object.fullname)
    initial_fullname_array = initial_fullname.split('_')
    final_fullname = str(initial_fullname_array[1])
    return final_fullname


def reply_function_and_error_logging(reddit_object,
                                     comment_fullname_function,
                                     api_call_function,
                                     requests_object_caller_func):
    for i in reddit_object.inbox.unread(limit=None):
        list_of_saved = reddit_object.redditor('scripture_bot').saved()
        for comments in list_of_saved:
            if str(i) == str(comments):
                return 'already responded to the redditor'
        if "scripture_bot!" not in i.body:
            i.mark_read()
            return malformed_request(i.author, i.body, i)
        if "scripture_bot!" in i.body:
            query = str(i.body)
            query_request_logger(i, query)
            requests_object = requests_object_caller_func(query)
            api_request_logger(i, requests_object, query)
            response = api_call_function(query, requests_object)
            comment_fullname = comment_fullname_function(i)
            unread_comment = reddit_object.comment(id=comment_fullname)
            if ": [" in response:
                response = esv_error_catcher(response)
            if ":[" in response:
                response = esv_error_catcher(response)
            if "{" in response:
                response = esv_error_catcher(response)
            if 'error' in response:
                unread_comment.reply(response)
                i.mark_read()
                return complaint_log(i.author, response)
            if 'error' not in response:
                unread_comment.reply(response)
                i.save()
                i.mark_read()
            query_response_logger(i, requests_object, query, response)


def the_actual_bot(authentication, fullname_creator_func, reply_function):
    reddit_object = authentication
    reply_function(reddit_object, fullname_creator_func, query_processor, requests_object_caller)

# Uncomment this if you want to run the bot locally and activate the script by executing scripture_bot.py

# from authenticator import authenticate
# while 1 == 1:
#    the_actual_bot(authenticate(), fullname_creator, reply_function_and_error_logging)


# pdb.runcall(the_actual_bot(authenticate(), unread_generator, fullname_creator, reply_function_and_error_logging))

