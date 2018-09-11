from time import asctime,gmtime
from time import time as epochtime
def API_Response_Logger(requests_object):
	response_code=str(requests_object)
	response_url=str(requests_object.url)
	log_time=time()
	API_response_log_entry=response_url+" returned a status code of "+response_code+" at: "+log_time
	print(API_response_log_entry)
	return API_response_log_entry
def API_Request_Logger(reddit_comment_object,requests_object,query):
	response_url=str(requests_object.url)
	log_time=time()
	query_owner=str(reddit_comment_object.author)
	query=str(query)
	API_request_log_entry="scripture_bot has made the query: "+query+" to "+response_url+" \n on behalf of "+query_owner+"at: "+log_time
	print(API_request_log_entry)
	return API_response_log_entry
def Query_Request_Logger(reddit_comment_object,query):
	log_time=time()
	query_owner=str(reddit_comment_object.author)
	query=str(query)
	query_request_log_entry="scripture_bot has recieved the query: "+query+" from "+query_owner+" at: "+log_time
	print(query_request_log_entry)
	return query_request_log_entry
def Query_Response_Logger(reddit_comment_object,requests_object,query,final_response):
	log_time=time()
	query_owner=str(reddit_comment_object.author)
	query=str(query)
	response_url=str(requests_object.url)
	response_code=str(requests_object)
	query_response_log_entry="scripture_bot responded to "+query_owner+" at: "+log_time+"\n"
	query_response_log_entry=query_response_log_entry+"it used their query: "+query+"\n"+"to make a request to "+response_url+"\n"+'which responded with '+response_code+"\n"
	query_response_log_entry="the final comment string returned was: "+'\n'+str(final_response)
	print(str(query_response_log_entry))
	return str(query_response_log_entry)
def time():
	time=str(asctime(gmtime(epochtime())))
	return time 
#exception handling will be done by Lambda itself with cloudwatch
