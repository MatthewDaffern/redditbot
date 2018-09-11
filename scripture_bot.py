#!/usr/bin/python
# -*- coding: utf-8 -*-

import praw
import Common



def authenticate():
    reddit = praw.Reddit(username=USERNAME,
                         password=PASSWORD,
                         client_id=CLIENT_ID,
                         client_secret=CLIENT_SECRET,
                         user_agent="Scripturebot v1.2 for reddit. /u/i_need_to_argue")
    return reddit
def unread_generator(reddit_object):
    inbox=reddit_object.inbox.unread()
    return inbox
def fullname_creator(comment_object):
    initial_fullname=str(comment_object.fullname()):
    initial_fullname_array=initial_fullname.split('_')
    final_fullname=str(initial_fullname[1])
    return final_fullname
def reply_function_and_error_logging(reddit_object,comment_fullname_function,unread_message,API_call_function):
    comment_log=list()
    for i in unread_message:
        query=str(i)
        response=API_call_function(query)
        comment_fullname=comment_fullname_function(i)
        unread_comment=reddit_object.comment(id=comment_fullname)
        if 'ERROR' in response:
        	reddit_object.message()
        	reddit.subreddit('scripturebot').message('ERROR', response+'\n \n \n'+"query processed was: "+query)
        	unread_comment.reply('Malformed request: Your request cannot be fulfilled for one or more reasons. The developers have been notified')
        if 'ERROR' not in response:
	        unread_comment.reply(response)
	        comment_log.append(str(response))
    return comment_log
def the_actual_bot(authenticate,unread_generator,fullname_creator,reply_function):
    reddit=authenticate()
    unread=unread_generator(reddit)
    reply_function(reddit,fullname_creator,unread,query_wrapper)




the_actual_bot()


'''

@failable
def process_subreddit(sub, reddit, rb):
    for comment in reddit.subreddit(sub).comments(limit=None):
        if not replied_to(comment.id) and comment.archived is False:
            text, citation, malformed = rb.fetch(comment.body)
            if len(text) > 0:
                comment.reply(text)
                insert(comment.id, sub, comment.author.name, citation)
                log("Responded to " + comment.author.name + " on " + sub + " with " + citation)
                if malformed:
                    log(comment.author.name + "submitted a malformed request. Some of all of their "
                                              "request was not fulfilled")
from Config import USERNAME, PASSWORD, CLIENT_ID, CLIENT_SECRET, SUBREDDITS
from utils import ResponseBuilder
from utils.Database import create_table, replied_to, insert
from utils.Failable import failable
from utils.Util import log
def main():
    prepare_database()
    reddit = authenticate()
    rb = ResponseBuilder()
    for sub in SUBREDDITS:
        process_subreddit(sub, reddit, rb)
if __name__ == '__main__':
    main()
def prepare_database():
    create_table()
    log("Database Ready")
'''