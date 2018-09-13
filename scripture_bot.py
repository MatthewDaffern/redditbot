from common import *
from log import *
from authenticator import authenticate


def unread_generator(reddit_object):
    inbox = reddit_object.inbox.unread(limit=None)
    return inbox


def fullname_creator(comment_object):
    initial_fullname = str(comment_object.fullname)
    initial_fullname_array = initial_fullname.split('_')
    final_fullname = str(initial_fullname_array[1])
    return final_fullname


def reply_function_and_error_logging(reddit_object,
                                     comment_fullname_function,
                                     unread_message,
                                     api_call_function,
                                     requests_object_caller_func):
    comment_log = list()  
    for i in reddit_object.inbox.unread(limit=None):
        if "scripture_bot!" not in i.body:
            print("malformed request made by "+str(i.author)+" at "+str(time()))
            return 'error'
        query = str(i.body)
        query_request_logger(i, query)
        requests_object = requests_object_caller_func(query)
        api_request_logger(reddit_object, requests_object, query)
        response = api_call_function(query, requests_object)
        comment_fullname = comment_fullname_function(i)
        unread_comment = reddit_object.comment(id=comment_fullname)
        if 'error' in response:
            compliant_log1 = query + ' was made at ' + time()
            compliant_log2 = 'by ' + str(reddit_object.author) + ' and the following error was raised' + response
            compliant_log = compliant_log1 + compliant_log2
            print(compliant_log)
            reply1 = 'malformed request: your request cannot be fulfilled for one or more reasons.'
            reply2 = ' the developers have been notified'
            reply = reply1 + reply2
            unread_comment.reply(reply)
        if 'error' not in response:
            unread_comment.reply(response)
            comment_log.append(str(response))
        query_response_logger(reddit_object, requests_object, query, response)
    return comment_log



def the_actual_bot(authentication, unread_generator_func, fullname_creator_func, reply_function):
    reddit_object = authentication()
    unread = unread_generator_func(reddit_object)
    reply_function(reddit_object, fullname_creator_func, unread, query_processor)
'''


def the_actual_bot(authentication, unread_generator_func, fullname_creator_func, reply_function):
    reddit_object = authentication
    while 1 == 1:
        x=int()
        unread = unread_generator_func(reddit_object)
        reply_function(reddit_object, fullname_creator_func, unread, query_processor,requests_object_caller)
        x=x+1
        if x>7:
            break

the_actual_bot(authenticate(), unread_generator, fullname_creator, reply_function_and_error_logging)
'''
