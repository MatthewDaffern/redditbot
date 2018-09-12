
import requests
import log
import api_keys


def biblia_api_key_storage():
    return api_keys.biblia()


def esv_api_key_storage():
    return api_keys.esv()


def comment_parser(input_string):
    # expects the format:
    # /u/scripture_bot! john 3:16 kjv
    query = input_string.split(" ")
    query = query[1:3]
    verse_chapter = query[1]
    verse_chapter = verse_chapter.split(":")
    verse_chapter = str(verse_chapter[0]+"."+verse_chapter[1])
    query[1] = verse_chapter
    # should now be ['john','3.16',"kjv"]
    return query


def esv_response_builder(query, api_key):
    mode = 'text'
    additional_parameters = '&include-passage-references=false&include-footnotes=false&include-headings=false'
    url = 'https://api.esv.org/v3/passage/'+mode+'/?q='+query[0]+'+'+query[1]+additional_parameters
    headers = {'authorization': str(' '+api_key)}
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
    # example api call
    # https://api.biblia.com/v1/bible/content/{bible}.{outputformat}?passage={biblereference}&key={api key}
    # expects the query to be in the following format kjv,john,3:16
        api_call = 'https://api.biblia.com/v1/bible/content/'+str(query[0])+'.js'+'?passage='
        api_call = api_call+query[1]+query[2]+'&key='+api_key
        biblia_api_return = requests.get(api_call)
        return biblia_api_return


def final_biblia_response(input_string):
    biblia_response = input_string
    biblia_response_stripped_front = biblia_response.strip('"mycallbackfunction({"text":"')
    biblia_response_stripped_back = biblia_response_stripped_front.strip('"});')
    biblia_response_final = biblia_response_stripped_back
    biblia_response_body = biblia_response_final
    return biblia_response_body


def biblia_footer():
    couple_of_spaces = "\n \n"
    tos_footer1 = "^(this) ^(bot) ^(uses) ^(the) [^(biblia)](https://biblia.com/)"
    tos_footer2 = " ^(web) ^(services) ^(from) [^(esv)](https://www.logos.com/))"
    tos_footer = tos_footer1+tos_footer2
    github_footer = "^(|) [^(source code)](https://github.com/matthewdaffern/redditbot])"
    msg_the_devs_footer = '^(|) [^(message the developers)](https://www.reddit.com/message/compose?to=/r/scripturebot)'
    footer = couple_of_spaces+tos_footer+github_footer+msg_the_devs_footer
    return footer


def esv_footer():
    esv_title = "*esv*"
    couple_of_spaces = "\n \n"
    tos_footer1 = '^(this) ^(bot) ^(uses) ^(the) [^(esv)](https://api.esv.org/docs/)'
    tos_footer2 = ' ^(web) ^(services) ^(from) [^(logos bible software)](https://www.logos.com/))'
    tos_footer = tos_footer1+tos_footer2
    github_footer = "^(|) [^(source code)](https://github.com/matthewdaffern/redditbot])"
    msg_the_devs_footer = '^(|) [^(message the developers)](https://www.reddit.com/message/compose?to=/r/scripturebot)'
    footer = esv_title+couple_of_spaces+tos_footer+github_footer+msg_the_devs_footer
    return footer


'''error handling functions'''


def api_error_handler(response_builder):
    # expects a requests object as input
    if "200" not in str(response_builder):
        return "error: one or more queries could not be handled. biblia or esv cannot fulfill your request at this time"
    if "200" in str(response_builder):
        return "success"


def length_checker(final_comment):
    if len(final_comment) > 8000:
        return "error:your request could not be fulfilled because it's over 8,000 characters."
    else:
        return"success"


def full_comment_string(input_string, response_body, footer_input):
    # input string is the string initially used to make the api call.
    bot_username = "/u/scripture_bot!"
    reconverted_query = input_string.strip(bot_username)
    header = str("*"+reconverted_query+"*"+"\n \n")
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
    final_query = "ERROR: Query not processed"
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
