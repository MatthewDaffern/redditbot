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


def incorrect_bible_version():
    log_statement = 'incompatible bible request was made at: ' + str(time())
    print(log_statement)
    return log_statement


def http_non_200(http_response_input):
    error = "error: one or more queries could not be handled. Web Services cannot handle your request\n\n"
    resulting_error = error+str(http_response_input)
    return resulting_error


def length_checker(final_comment):
    if len(final_comment) > 8000:
        return "error:your request could not be fulfilled because it's over 8,000 characters.\n\n"
    else:
        return "success"


def log_wrapper(input_string):
    return str(input_string+' '+str(time()))


def malformed_request(author_object, body_object, comment_object):
    error_msg = str(author_object) + ' made the malformed request ' \
                + str(body_object) + "\n \n (" + str(comment_object) + ")" \
                + " at " + str(time())
    print(error_msg)
    return error_msg


def complaint_log(author_object, response):
    complaint_error = query +\
                ' was made at ' + time()\
                + ' by ' + str(author_object) \
                + '\n \n and the following error was raised ' \
                + response
    print(complaint_error)
    return complaint_error