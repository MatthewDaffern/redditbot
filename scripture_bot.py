import praw
from Common import *
from log import *
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
	reddit=praw.Reddit(username=USERNAME,password=PASSWORD,client_id=CLIENT_ID,client_secret=CLIENT_SECRET,user_agent=CLIENT_AGENT)
	return reddit
def unread_generator(reddit_object):
    inbox=reddit_object.inbox.unread()
    return inbox
def fullname_creator(comment_object):
    initial_fullname=str(comment_object.fullname()):
    initial_fullname_array=initial_fullname.split('_')
    final_fullname=str(initial_fullname[1])
    return final_fullname
def reply_function_and_error_logging(reddit_object,comment_fullname_function,unread_message,API_call_function,requests_object_caller):
    comment_log=list()
    for i in unread_message:
        query=str(i)
        Query_Request_Logger(reddit_object,query)
        requests_object=requests_object_caller(query)
        API_Request_Logger(reddit_object,requests_object,query)
        response=API_call_function(query,requests_object)
        comment_fullname=comment_fullname_function(i)
        unread_comment=reddit_object.comment(id=comment_fullname)
        if 'ERROR' in response:
        	print(query+' was made at '+time()+'by '+str(reddit_object.author)+' and the following error was raised'+response)
        	unread_comment.reply('Malformed request: Your request cannot be fulfilled for one or more reasons. The developers have been notified')
        if 'ERROR' not in response:
	        unread_comment.reply(response)
	        comment_log.append(str(response))
        Query_Response_Logger(reddit_object,requests_object,response)
    return comment_log
def the_actual_bot(authenticate,unread_generator,fullname_creator,reply_function):
    reddit=authenticate()
    unread=unread_generator(reddit)
    reply_function(reddit,fullname_creator,unread,query_processor)





