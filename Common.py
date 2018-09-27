import requests
import log
import API_keys
import time


def rate_limiter():
    whole_second = 1
    divisor = 40
    rate_limiting_time = whole_second / divisor
    initial_time = time.time()
    final_time = time.time()
    time_difference = final_time-initial_time
    while time_difference < rate_limiting_time:
        final_time = time.time()
        time_difference = final_time-initial_time


def biblia_api_key_storage():
    return API_keys.biblia()


def esv_api_key_storage():
    return API_keys.esv()


def error_handling(input_string):
    error_message = 'error: one or more things are missing from the query'
    if ':' not in input_string:
        return error_message
    return 'passed initial sanitization!'


def available_versions():
    correct_versions = dict([('ASV', 'ASV'),
                             ('ARB', 'ARVANDYKE'),
                             ('KJV', 'KJV'),
                             ('LSG', 'LSG'),
                             ('BYZ', 'BYZ'),
                             ('DRB', 'DARBY'),
                             ('ELZ', 'ELZEVIR'),
                             ('ITL', 'ITDIODATI1649'),
                             ('EMP', 'EMPHBBL'),
                             ('LEB', 'LEB'),
                             ('SCR', 'SCRMORPH'),
                             ('FIN', 'FI-RAAMATTU'),
                             ('RVR', 'RVR60'),
                             ('RVA', 'RVA'),
                             ('RUS', 'BB-SBB-RUSBT'),
                             ('ESP', 'EO-ZAMENBIB'),
                             ('SVV', 'SVV'),
                             ('STPH', 'STEPHENS'),
                             ('TKH', 'TANAKH'),
                             ('PBT', 'WBTC-PTBRNT'),
                             ('WHG', 'WH1881MR'),
                             ('YLT', 'YLT'),
                             ('ESV', 'ESV')])
    return correct_versions


def comment_parser(input_string, version_dict):
    # expects the format:
    # u/scripture_bot! john 3:16 kjv
    index_of_username_mention = 0
    username_test = 'scripture_bot'
    # exits early to avoid an exception
    if 'error' in input_string:
        return input_string
    # initial preprocessing and turns the query into a list
    query = input_string
    while "  " in query:
        query = query.replace('  ', ' ')
    query = query.split(" ")
    # looks for the version of the bible to use so that the query slice can be created.
    for i in query:
        if 'scripture_bot' in i:
            index_of_username_mention = query.index(i)
            username_test = i
            break
    available_bible_versions = version_dict
    search_indice = index_of_username_mention
    version_query = 1
    bible_version_found = 'no'
    bible_version = 'error: version not found'
    # searches for the end of the query
    while version_query == 1:
        if search_indice == len(query):
            break
        test = query[search_indice].upper()
        for i in available_bible_versions:
            if i in test:
                bible_version = i
                bible_version_found = 'yes'
                break
        search_indice = search_indice + 1
    if bible_version_found == 'no':
        return 'error: no bible version found'
    query_slice = query[index_of_username_mention:int(search_indice+1)]
    fixed_query_slice = list()
    for i in query_slice:
        if bible_version in i:
            fixed_query_slice.append(bible_version)
            break
        fixed_query_slice.append(i)
    query_slice = fixed_query_slice
    chapter_verse = 'error: chapter verse not found'
    username_mention = 'error: username not found'
    for i in query_slice:
        if i.upper() in available_bible_versions:
            bible_version = i
        if username_test in i:
            username_mention = i
        if ':' in i:
            chapter_verse = i
    query_slice.remove(bible_version)
    query_slice.remove(username_mention)
    if ':' not in chapter_verse:
        chapter_verse = query_slice[len(query_slice)-1]
    for i in (bible_version, chapter_verse, username_mention):
        if 'error' in i:
            return 'User has made a malformed query'
    query_slice.remove(chapter_verse)
    bible_version = bible_version.upper()
    chapter_verse = chapter_verse.replace(':', '.')
    actual_bible_version = available_bible_versions[bible_version]
    book = str(query_slice[0]).capitalize()
    if len(query_slice) > 1:
        book = str()
        for i in query_slice:
            i = str(i)
            book = book+i.capitalize()+'+'
        book = book.rstrip(' + ')
    final_query = [book, chapter_verse, actual_bible_version]
    # should now be ['john','3.16',"KJV"]
    return final_query


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
    removed_characters = removed_newlines.replace('\\u201d', '')\
        .replace('\\u201c', '')\
        .replace('\\u2019', '')\
        .replace('\\u2018', '')\
        .replace('\\u2014', '')\
        .replace(': [" ', '')\
        .replace(']}', '')\
        .replace('(ESV)"', '(ESV)')
    while '  ' in removed_characters:
        removed_characters = removed_characters.replace('  ', ' ')
    esv_response_body = removed_characters
    return esv_response_body


def text_creator(response_builder):
    return response_builder.text


def biblia_response_builder(query, api_key):
        rate_limiter()
        api_call = 'https://api.biblia.com/v1/bible/content/'+query[2]+'.txt.js?passage='+query[0]+query[1]
        api_call = api_call+'&callback=myCallbackFunction&key='+api_key
        api_call = api_call.replace('0A', '')
        api_call = api_call.replace('%', '')
        r = requests.get(api_call)
        return r


def final_biblia_response(input_string):
    biblia_response = input_string
    biblia_response_stripped_front = biblia_response.strip('myCallbackfunction({"text":"')
    biblia_response_stripped_front = biblia_response_stripped_front.replace('Function({"text":"', '')
    biblia_response_stripped_back = biblia_response_stripped_front.strip('"});').replace('\\r', '').replace('\\n', '')
    biblia_response_final = biblia_response_stripped_back
    biblia_response_body = biblia_response_final
    return biblia_response_body


def biblia_footer():
    couple_of_spaces = "\n\n***\n"
    tos_footer1 = "^(this) ^(bot) ^(uses) ^(the) [^(biblia)](https://biblia.com/)"
    tos_footer2 = " ^(web) ^(services) ^(from) [^(Faithlife) ^(Corporation)](https://faithlife.com/about/)"
    tos_footer = tos_footer1+tos_footer2
    github_footer = " ^(|) [^(source code)](https://github.com/matthewdaffern/redditbot])"
    msg_the_devs_footer = ' ^(|) [^(message the developers)](https://www.reddit.com/message/compose?to=/r/scripturebot)'
    footer = couple_of_spaces+tos_footer+github_footer+msg_the_devs_footer
    return footer


def esv_footer():
    couple_of_spaces = "\n\n***\n"
    tos_footer1 = '^(this) ^(bot) ^(uses) ^(the) [^(ESV) ^(API)](https://api.esv.org/docs/)'
    tos_footer2 = ' ^(from) [^(Crossway)](https://www.crossway.org/)'
    tos_footer = tos_footer1+tos_footer2
    github_footer = " ^(|) [^(source code)](https://github.com/matthewdaffern/redditbot])"
    msg_the_devs_footer = ' ^(|) [^(message the developers)](https://www.reddit.com/message/compose?to=/r/scripturebot)'
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
    reconverted_query = comment_parser(input_string, available_versions())
    final_query = str()
    for i in reconverted_query:
        final_query = final_query+i+' '
    final_query = final_query.replace('.', ':').replace('+', ' ')
    header = str(final_query+"\n \n")
    footer = footer_input
    final_comment = header+response_body+footer
    return final_comment


def biblia(input_string, requests_object):
    # higher level biblia function. Performs all biblia functionality and packages it neatly
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
    # higher level ESV function. Performs all biblia functionality and packages it neatly
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
    if 'error' in requests_object:
        return requests_object
    if "ESV" in input_string.upper():
        final_query = esv(input_string, requests_object)
    if "ESV" not in input_string.upper():
        final_query = biblia(input_string, requests_object)
    return final_query


def requests_object_caller(input_string):
    api_call = "ERROR: API call not processed\n\n"
    if "ESV" in input_string.upper():
        api_call = esv_response_builder(comment_parser(input_string, available_versions()), esv_api_key_storage())
    if "ESV" not in input_string.upper():
        api_call = biblia_response_builder(comment_parser(input_string, available_versions()), biblia_api_key_storage())
    return api_call
