import requests
import log
import API_keys
import time


# =====================================================================================================================
# API key loading functions
def biblia_api_key_storage():
    return API_keys.biblia()


def esv_api_key_storage():
    return API_keys.esv()


# =====================================================================================================================
# Nonversion specific functions


def available_versions():
    correct_versions = dict([('ASV', 'ASV'),
                             ('ARB', 'ARVANDYKE'),
                             ('KJV', 'KJV'),
                             ('APOC', 'KJVAPOC'),
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
# Versions I allow. Currently not distinguished by API type.


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


# Hastily written rate_limiter since Biblia restricts the amount of API calls I can make.
# I currently have it on a 1/32 delay whenever rate_limiter is invoked

def text_creator(response_builder):
    return response_builder.text
# Just grabs the text from the response object


def comment_parser(input_string, version_dict):
    def space_remover_and_list_creator(input_string_object):
        query = input_string_object
        while "  " in query:
            query = query.replace('  ', ' ')
        query = query.split(" ")
        for i in query:
            print(str(i))
        return query
# Creates the initial list object

    def newline_character_remover(list_input):
        cleaned_list = list()
        for i in list_input:
            place_holder = i
            if '\n' in place_holder:
                place_holder = place_holder.split('\n')
                place_holder = place_holder[0]
                cleaned_list.append(place_holder)
            if '\n' not in place_holder:
                cleaned_list.append(place_holder)
        return cleaned_list
# Removes the \n characters that were messing me up.

    def index_of_username_mention_finder(list_input):
        print(list_input)
        index_of_username_mention = 0
        for i in list_input:
            if 'scripture_bot' in i:
                index_of_username_mention = list_input.index(i)
                break
        return index_of_username_mention
# Finds the index of the username_mention

    def slice_creator(query, version_dict_object):
        available_bible_versions = version_dict_object
        index_of_username_mention = index_of_username_mention_finder(query)
        search_indice = index_of_username_mention
        version_query_loop = 'on'
        # searches for the end of the query
        success = 'no'
        while version_query_loop == 'on':
            if success == 'yes':
                break
            if search_indice == len(query):
                return log.incorrect_bible_version()
            test = query[search_indice].upper()
            for i in list(available_bible_versions):
                if test in i:
                    success = 'yes'
                    break
            search_indice = search_indice + 1
        query_slice = query[index_of_username_mention:int(search_indice + 1)]
        return query_slice
# Creates the slice based on where the valid bible version is.

    def final_list_creator(query, version_dict_object):
        username_mention = 'scripture_bot'
        query_slice = query
        available_bible_versions = version_dict_object
        # [/u/scripture_bot!,1st,John,3:2,KJV]
        for i in query_slice:
            if username_mention in i:
                username_mention_index = query_slice.index(i)
            if i.upper() in list(available_bible_versions):
                bible_version_index = query_slice.index(i)
                bible_version = available_bible_versions[i.upper()]
        var_check = list(locals())
        for i in ('bible_version_index', 'username_mention_index'):
            if i not in var_check:
                print(str(i)+' not assigned')
                bible_version = 'error: no bible book'
                bible_book = 'error: no chapter verse'
                bible_chapter_verse = 'error: no chapter verse'
                final_query_slice = [bible_book, bible_chapter_verse, bible_version]
                return final_query_slice
        book_chapter_verse_slice = query_slice[int(username_mention_index+1) : int(bible_version_index)]
        for i in book_chapter_verse_slice:
            if '.' in i:
                bible_chapter_verse = i
                bible_chapter_verse_index = book_chapter_verse_slice.index(i)
            if ':' in i:
                bible_chapter_verse = i
                bible_chapter_verse_index = book_chapter_verse_slice.index(i)
        var_check = list(locals())
        if 'bible_chapter_verse_index' not in var_check:
            bible_version = 'error: no bible book'
            bible_book = 'error: no chapter verse'
            bible_chapter_verse = 'error: no chapter verse'
            final_query_slice = [bible_book, bible_chapter_verse, bible_version]
            return final_query_slice
        bible_book_slice = book_chapter_verse_slice[:(bible_chapter_verse_index)]
        bible_book = str()
        for i in bible_book_slice:
            bible_book = bible_book + str(i) + '+'
        bible_book = bible_book.rstrip('+')
        var_check = list(locals())
        if 'bible_book' not in var_check:
            bible_book = 'error: no bible book'
        if 'bible_chapter_verse' not in var_check:
            bible_chapter_verse = 'error: no chapter verse'
        if 'bible_version' not in var_check:
            bible_version = 'error: no version recognized'
        final_query_slice = [bible_book, bible_chapter_verse, bible_version]
        return final_query_slice
    final_query = final_list_creator(slice_creator(newline_character_remover(
                    space_remover_and_list_creator(input_string)), version_dict), version_dict)

    # does the monstrous parsing and sorting job
    return final_query
# this is where most of the work is done to make the comment usable in an API call.
# Most of my errors and problems have been here.


# =====================================================================================================================
# ESV Functions


def esv_response_builder(query, api_key):
    rate_limiter()
    mode = 'text'
    additional_parameters = '&include-passage-references=false&include-footnotes=false&include-headings=false'
    url = 'https://api.esv.org/v3/passage/'+mode+'/?q='+query[0]+'+'+query[1]+additional_parameters
    headers = {'authorization': str(api_key)}
    api_call = requests.get(url, headers=headers)
    return api_call
# ESV specific request maker


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
# this accepts the input string and filters out all the irritating extra unicode characters with a .replace() call.
# it also removes all the statistics I get in the beginning normally.


def esv_footer():
    couple_of_spaces = "\n\n***\n"
    tos_footer1 = '^(this) ^(bot) ^(uses) ^(the) [^(ESV) ^(API)](https://api.esv.org/docs/)'
    tos_footer2 = ' ^(from) [^(Crossway)](https://www.crossway.org/)'
    tos_footer = tos_footer1+tos_footer2
    github_footer = " ^(|) [^(source code)](https://github.com/matthewdaffern/redditbot])"
    msg_the_devs_footer = ' ^(|) [^(message the developers)](https://www.reddit.com/message/compose?to=/r/scripturebot)'
    footer = couple_of_spaces+tos_footer+github_footer+msg_the_devs_footer
    return footer
# fairly self explanatory. This is where I maintain compliance with my API agreement.

# =====================================================================================================================
# Biblia Functions


def biblia_response_builder(query, api_key):
        rate_limiter()
        api_call = 'https://api.biblia.com/v1/bible/content/'+query[2]+'.txt.js?passage='+query[0]+query[1]
        api_call = api_call+'&callback=myCallbackFunction&key='+api_key
        api_call = api_call.replace('0A', '')
        api_call = api_call.replace('%', '')
        r = requests.get(api_call)
        return r
# biblia specific request maker


def final_biblia_response(input_string):
    biblia_response = input_string
    biblia_response_stripped_front = biblia_response.strip('myCallbackfunction({"text":"')
    biblia_response_stripped_front = biblia_response_stripped_front.replace('Function({"text":"', '')
    biblia_response_stripped_back = biblia_response_stripped_front.strip('"});').replace('\\r', '').replace('\\n', '')
    biblia_response_final = biblia_response_stripped_back
    biblia_response_body = biblia_response_final
    return biblia_response_body
# this accepts the input string and filters out all the irritating extra unicode characters with a .replace() call.
# it also removes all the statistics I get in the beginning normally.


def biblia_footer():
    couple_of_spaces = "\n\n***\n"
    tos_footer1 = "^(this) ^(bot) ^(uses) ^(the) [^(biblia)](https://biblia.com/)"
    tos_footer2 = " ^(web) ^(services) ^(from) [^(Faithlife) ^(Corporation)](https://faithlife.com/about/)"
    tos_footer = tos_footer1+tos_footer2
    github_footer = " ^(|) [^(source code)](https://github.com/matthewdaffern/redditbot])"
    msg_the_devs_footer = ' ^(|) [^(message the developers)](https://www.reddit.com/message/compose?to=/r/scripturebot)'
    footer = couple_of_spaces+tos_footer+github_footer+msg_the_devs_footer
    return footer
# fairly self explanatory. This is where I maintain compliance with my API agreement.


# =====================================================================================================================
# Just designed to reject requests that don't return a 200 call.

def api_error_handler(response_builder):
    # expects a requests object as input
    if "200" not in str(response_builder):
        log.http_non_200(response_builder)
        return 'error. Please notify /u/i_need_to_argue or the moderators of scripturebot'
    if "200" in str(response_builder):
        return "success"

# =====================================================================================================================
# This function is designed to take the final text, a footer, and the original query and turn it into an actual comment
# It's designed not be dependent on knowing what API to use, as the relevant strings are passed to it instead.


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

# =====================================================================================================================
# The below functions are combining all my loose functions from above so that they can be easily used.
# I tried to break up the functions into single tasks for each function
# This made is easier to write than having a long imperative mess of spaghetti


def biblia(input_string, requests_object):
    # higher level biblia function. Performs all biblia functionality and packages it neatly
    api_call = requests_object
    log.api_response_logger(api_call)
    api_error_handling = api_error_handler(api_call)
    if 'error' in api_error_handling:
        return api_error_handling
    biblia_body = final_biblia_response(text_creator(api_call))
    response = full_comment_string(input_string, biblia_body, biblia_footer())
    length_test = log.length_checker(response)
    if 'error' in length_test:
        return length_test
    return response


def esv(input_string, requests_object):
    # higher level ESV function. Performs all ESV functionality and packages it neatly
    api_call = requests_object
    log.api_response_logger(api_call)
    api_error_handling = api_error_handler(api_call)
    if 'error' in api_error_handling:
        return api_error_handling
    esv_body = final_esv_response(text_creator(api_call))
    response = full_comment_string(input_string, esv_body, esv_footer())
    length_test = log.length_checker(response)
    if 'error' in length_test:
        return length_test
    return response

# =====================================================================================================================
# the requests_object_caller creates the requests object that gets worked on further.
# the comment and I can use the requests object for error checking since it also stores HTTP response codes
# The query_processor takes the original input string just for some decision making on how to format comment responses
# I probably can make it clearer by wrapping the two into a single function that just requires an input string. TODO


def requests_object_caller(input_string):
    if 'error' in input_string:
        return 'one or more things are missing from the query. Check the documentation or contact /u/i_need_to_argue'
    api_call = "ERROR: API call not processed\n\n"
    if "ESV" in input_string.upper():
        api_call = esv_response_builder(comment_parser(input_string, available_versions()), esv_api_key_storage())
    if "ESV" not in input_string.upper():
        api_call = biblia_response_builder(comment_parser(input_string, available_versions()), biblia_api_key_storage())
    if 'ERROR' in api_call:
        return log.log_wrapper(api_call)
    return api_call


def query_processor(input_string, requests_object):
    if 'error' in input_string:
        return 'one or more things are missing from the query. Check the documentation or contact /u/i_need_to_argue'
    final_query = "ERROR: Query not processed\n\n"
    if 'error' in requests_object:
        return requests_object
    if "ESV" in input_string.upper():
        final_query = esv(input_string, requests_object)
    if "ESV" not in input_string.upper():
        final_query = biblia(input_string, requests_object)
    return final_query


