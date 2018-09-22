def query_processor(input_string, requests_object):
    final_query = "ERROR: Query not processed"
    if "esv" in input_string:
        final_query = esv(input_string, requests_object)
    if "esv" not in input_string:
        final_query = get_bible(input_string, requests_object)
    return final_query
 def requests_object_caller(input_string):
    api_has_not_been_called = str()
    api_call = api_has_not_been_called
    if "esv" in input_string:
        api_call = esv_response_builder(comment_parser(input_string), esv_api_key_storage())
    if "esv" not in input_string:
        api_call = get_bible_response_builder(comment_parser(input_string))
    return api_call
 def get_bible(input_string, requests_object):
    api_call = requests_object
    log.api_response_logger(api_call)
    api_error_handling = api_error_handler(api_call)
    if 'error' in api_error_handling:
        return api_error_handling
    get_bible_body = final_get_bible_response(text_creator(api_call))
    response = full_comment_string(input_string, get_bible_body, get_bible_footer())
    length_test = length_checker(response)
    if 'error' in length_test:
        return length_test
    return response
 def get_bible_footer():
    couple_of_spaces = "\n \n"
    tos_footer1 = "^(this) ^(bot) ^(uses) ^(the) [^(get_bible)](http://getbible.net/about)"
    tos_footer2 = " ^(web) ^(services) ^(from) [^(Llewellyn van der Merwe)](https://stackoverflow.com/cv/llewellyn/))"
    tos_footer = tos_footer1+tos_footer2
    github_footer = "^(|) [^(source code)](https://github.com/matthewdaffern/redditbot])"
    msg_the_devs_footer = '^(|) [^(message the developers)](https://www.reddit.com/message/compose?to=/r/scripturebot)'
    footer = couple_of_spaces+tos_footer+github_footer+msg_the_devs_footer
    return footer
 def get_bible_response_builder(query):
    # http://getbible.net/json?passage=John%2015:25-28,%2010,%2015&version=web
    mode = 'json'
    version = query[2]
    chapter_verse = query[1].replace('.', ':')
    book = query[0]
    url = 'http://getbible.net/'+mode+'?passage='+book+'%20'+chapter_verse+',%2010,%2015&version='+version
    api_call = requests.get(url)
    return api_call
 def final_get_bible_response(input_string):
    list_to_iterate = input_string.split('"verse":"')
    list_without_beginning_statistics_to_iterate=list()
    for i in list_to_iterate:
        if 'book' not in i:
            list_without_beginning_statistics_to_iterate.append(i)
    get_bible_response_body = str()
    for i in list_without_beginning_statistics_to_iterate:
        temp_list = i.split('\r\n')
        verse_to_add = temp_list
        get_bible_response_body=get_bible_response_body+verse_to_add[0]
    return get_bible_response_body
