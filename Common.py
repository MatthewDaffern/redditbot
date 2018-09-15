import requests
import log
import api_keys
import time


def rate_limiter():
    whole_second = 1
    divisor = 32
    rate_limiting_time = whole_second / divisor
    initial_time = time.time()
    final_time = time.time()
    time_difference = final_time-initial_time
    while time_difference < rate_limiting_time:
        final_time = time.time()
        time_difference = final_time-initial_time


def biblia_api_key_storage():
    return api_keys.biblia()


def esv_api_key_storage():
    return api_keys.esv()


def error_handling(input_string):
    error_message = 'error: one or more things are missing from the query'
    array_test = input_string.split(' ')
    if not len(array_test) == 4:
        return error_message
    if ':' not in input_string:
        return error_message
    for i in array_test:
        if " " in i:
            return error_message
    return 'passed initial sanitization!'


def comment_parser(input_string):
    # expects the format:
    # /u/scripture_bot! john 3:16 kjv
    if 'error' in input_string:
        return input_string
    query = input_string.split(" ")
    query = query[1:4]
    verse_chapter = query[1]
    verse_chapter = str(verse_chapter[0]+"."+verse_chapter[1])
    query[1] = verse_chapter
    # should now be ['john','3.16',"kjv"]
    return query


def esv_response_builder(query, api_key):
    rate_limiter()
    mode = 'text'
    additional_parameters = '&include-passage-references=false&include-footnotes=false&include-headings=false'
    url = 'https://api.esv.org/v3/passage/'+mode+'/?q='+query[0]+'+'+query[1]+additional_parameters
    headers = {'authorization': str(api_key)}
    api_call = requests.get(url, headers=headers)
    return api_call


def final_esv_response(input_string):
    removed_data = input_string.split('"passages"')
    removed_data = removed_data[1]
    removed_newlines = removed_data.replace('\\n', '')
    removed_utf8_characters = removed_newlines.replace('\\u201d', '').replace('\\u201c', '')
    removed_utf8_characters = removed_utf8_characters.replace('\\u2019', '').replace('\\u2018', '')
    fixed_formatting = removed_utf8_characters.replace(': [" ', '').replace(']}', '').replace('(esv)"', '(esv)')
    esv_response_body = fixed_formatting
    return esv_response_body


def text_creator(response_builder):
    return response_builder.text


def biblia_response_builder(query, api_key):
        rate_limiter()
        api_call = 'https://api.biblia.com/v1/bible/content/'+query[2]+'.txt.js?passage='+query[0]+query[1]
        api_call = api_call+'&callback=myCallbackFunction&key='+api_key
        api_call = api_call.replace('%0A', '')
        r = requests.get(api_call)
        return r


def final_biblia_response(input_string):
    biblia_response = input_string
    biblia_response_stripped_front = biblia_response.strip('myCallbackfunction({"text":"')
    biblia_response_stripped_front = biblia_response_stripped_front.replace('Function({"text":"', '')
    biblia_response_stripped_back = biblia_response_stripped_front.strip('"});')
    biblia_response_final = biblia_response_stripped_back
    biblia_response_body = biblia_response_final
    return biblia_response_body


def biblia_footer():
    couple_of_spaces = "\n\n***  &nbsp;  \n"
    tos_footer1 = "^(this) ^(bot) ^(uses) ^(the) [^(biblia)](https://biblia.com/)"
    tos_footer2 = " ^(web) ^(services) ^(from) [^(Faithlife) ^(Corporation)](https://faithlife.com/about/)"
    tos_footer = tos_footer1+tos_footer2
    github_footer = "^(|)[^(source code)](https://github.com/matthewdaffern/redditbot])"
    msg_the_devs_footer = '^(|)[^(message the developers)](https://www.reddit.com/message/compose?to=/r/scripturebot)'
    footer = couple_of_spaces+tos_footer+github_footer+msg_the_devs_footer
    return footer


def esv_footer():
    couple_of_spaces = "\n\n***  &nbsp;  \n"
    tos_footer1 = '^(this) ^(bot) ^(uses) ^(the) [^(esv)](https://api.esv.org/docs/)'
    tos_footer2 = ' ^(web) ^(services) ^(from) [^(logos) ^(bible) ^(software)](https://www.logos.com/)'
    tos_footer = tos_footer1+tos_footer2
    github_footer = "^(|) [^(source code)](https://github.com/matthewdaffern/redditbot])"
    msg_the_devs_footer = '^(|) [^(message the developers)](https://www.reddit.com/message/compose?to=/r/scripturebot)'
    footer = couple_of_spaces+tos_footer+github_footer+msg_the_devs_footer
    return footer


'''error handling functions'''


def api_error_handler(response_builder):
    # expects a requests object as input
    if "200" not in str(response_builder):
        return "error: one or more queries could not be handled. Web Services cannot handle your request\n\n"
    if "200" in str(response_builder):
        return "success"


def length_checker(final_comment):
    if len(final_comment) > 8000:
        return "error:your request could not be fulfilled because it's over 8,000 characters.\n\n"
    else:
        return"success"


def full_comment_string(input_string, response_body, footer_input):
    # input string is the string initially used to make the api call.
    bot_username = "/u/scripture_bot!"
    reconverted_query = input_string.strip(bot_username)
    header = str(reconverted_query+"\n \n")
    footer = footer_input
    final_comment = header+response_body+footer
    return final_comment


def biblia(input_string, requests_object):
    api_call = requests_object
    log.api_response_logger(api_call)
    api_error_handling = api_error_handler(api_call)
    if 'error' in api_error_handling:
        return api_error_handling
    biblia_body = final_biblia_response(text_creator(api_call))
    response = full_comment_string(input_string, biblia_body, biblia_footer())
    length_test = length_checker(response)
    if 'error' in length_test:
        return length_test
    return response


def esv(input_string, requests_object):
    api_call = requests_object
    log.api_response_logger(api_call)
    api_error_handling = api_error_handler(api_call)
    if 'error' in api_error_handling:
        return api_error_handling
    esv_body = final_esv_response(text_creator(api_call))
    response = full_comment_string(input_string, esv_body, esv_footer())
    length_test = length_checker(response)
    if 'error' in length_test:
        return length_test
    return response


def query_processor(input_string, requests_object):
    final_query = "ERROR: Query not processed\n\n"
    if "esv" in input_string:
        final_query = esv(input_string, requests_object)
    if "esv" not in input_string:
        final_query = biblia(input_string, requests_object)
    return final_query


def requests_object_caller(input_string):
    api_has_not_been_called = str()
    api_call = api_has_not_been_called
    if "esv" in input_string:
        api_call = esv_response_builder(comment_parser(input_string), esv_api_key_storage())
    if "esv" not in input_string:
        api_call = biblia_response_builder(comment_parser(input_string), biblia_api_key_storage())
    return api_call
