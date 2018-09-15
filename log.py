from time import asctime,  gmtime
from time import time as epochtime


def time():
    current_time = str(asctime(gmtime(epochtime())))
    return current_time


def api_response_logger(requests_object):
    response_code = str(requests_object)
    response_url = str(requests_object.url)
    log_time = time()
    api_response_log_entry = ('\n \n' + response_url + " returned a status code of " +
                              response_code + " at: " + log_time + '\n \n')
    print(api_response_log_entry)
    return api_response_log_entry


def api_request_logger(reddit_comment_object, requests_object, query):
    response_url = str(requests_object.url)
    log_time = time()
    query_owner = str(reddit_comment_object.author)
    query = str(query)
    api_request_log_entry = ("scripture_bot has made the query: " + query + " to \n \n" + response_url +
                             " \n on behalf of " + query_owner + "\n \nat: " + log_time + "\n\n")
    print(api_request_log_entry)
    return api_request_log_entry


def query_request_logger(reddit_comment_object, query):
    log_time = time()
    query_owner = str(reddit_comment_object.author)
    query = str(query)
    query_request_log_entry = ("scripture_bot has received the query: " + query + "\n \n from " +
                               query_owner + " at: " + log_time + "\n\n")
    print(query_request_log_entry)
    return query_request_log_entry


def query_response_logger(reddit_comment_object, requests_object, query, final_response):
    log_time = time()
    query_owner = str(reddit_comment_object.author)
    query = str(query)
    response_url = str(requests_object.url)
    response_code = str(requests_object)
    query_response_log_entry = ("scripture_bot responded to " + query_owner + " at: " + log_time +
                                "\n \n" + "it used their query: " + query +
                                "\n \n" + "to make a request to: \n \n" + response_url +
                                "\n \n" + 'which responded with ' + response_code +
                                "\n \n \n" + "the final comment string returned was: " +
                                '\n \n \n' + str(final_response) + " \n \n \n ")
    print(str(query_response_log_entry))
    return str(query_response_log_entry)
