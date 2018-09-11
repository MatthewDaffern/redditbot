import praw
from Common import *

def authenticate():
	config=open('config_file','r+')
	config_list=list(config.readlines())
	for i in config_list:
		config_line=i.split(',')
		if config_line[0]=='username':
			USERNAME=config_line[1]
		if config_line[0]=='password':
			PASSWORD=config_line[1]
		if config_line[0]=='client_id':
			CLIENT_ID=config_line[1]
		if config_line[0]=='client_secret':
			CLIENT_SECRET=config_line[1]
		if config_line[0]=='user_agent':
			USER_AGENT=config_line[1]
    reddit = praw.Reddit(username=USERNAME,
                         password=PASSWORD,
                         client_id=CLIENT_ID,
                         client_secret=CLIENT_SECRET,
                         user_agent=CLIENT_AGENT)
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

