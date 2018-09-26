from Common import *
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
        list_of_saved = reddit_object.redditor('scripture_bot').saved()
        counter = 1
        for comments in list_of_saved:
            if str(i) == str(comments):
                return 'already responded to the redditor'
            counter +=1
        if "scripture_bot!" not in i.body:
            error_msg = str(i.author)+' made the malformed request '+str(i.body)+"\n \n ("+str(i)+")"+" at "+str(time())
            print(error_msg)
            i.mark_read()
            return error_msg
        if "scripture_bot!" in i.body:
            query = str(i.body)
            query_request_logger(i, query)
            requests_object = requests_object_caller_func(query)
            api_request_logger(i, requests_object, query)
            response = api_call_function(query, requests_object)
            comment_fullname = comment_fullname_function(i)
            unread_comment = reddit_object.comment(id=comment_fullname)
            if 'error' in response:
                compliant_log = query +\
                                ' was made at ' + time()\
                                + ' by ' + str(i.author) \
                                + '\n \n and the following error was raised ' \
                                + response
                print(compliant_log)
                i.mark_read()
            if 'error' not in response:
                unread_comment.reply(response)
                i.save()
                i.mark_read()
            query_response_logger(i, requests_object, query, response)


def inbox_mark_read_function(reddit_object):
    from praw.models import Message
    from praw.models import Comment
    unread_messages = []
    for item in reddit_object.inbox.unread(limit=None):
        print(type(item))
        if isinstance(item, Message):
            unread_messages.append(item.fullname)
        if isinstance(item, Comment):
            unread_messages.append(item.fullname)
        reddit_object.inbox.mark_read(unread_messages)


def the_actual_bot(authentication, unread_generator_func, fullname_creator_func, reply_function):
    reddit_object = authentication
    unread = unread_generator_func(reddit_object)
    reply_function(reddit_object, fullname_creator_func, unread, query_processor, requests_object_caller)

# Uncomment this if you want to run the bot locally and activate the script by executing scripture_bot.py


# while 1 == 1:
#     the_actual_bot(authenticate(), unread_generator, fullname_creator, reply_function_and_error_logging)


# pdb.runcall(the_actual_bot(authenticate(), unread_generator, fullname_creator, reply_function_and_error_logging))

