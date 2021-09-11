import re
import requests
from functools import partial
import json
import books_dict
import versions_dict


def command_processor(input_string, api_key_input):
    return verse_sections(input_string, api_key_input)


# ======================================================================================================================


def de_fancypantsify(input_string):
    return input_string.replace('\','')

def verse_slice(input_string):
    print(input_string)
    """This is the regex pattern that I hit on during testing for grabbing verse sections. Note that finditer is used
       I have no idea why it works best, but it's the only solution."""
    pattern = '\[.{0,15}:.{0,10}\]'
    match = re.finditer(pattern, input_string)
    print(match)
    return list(map(lambda x: x.group(0), list(match)))


def neatify_string_to_list(input_string):
    """Gets me my actual list of items to query"""
    clean_brackets = input_string.replace('[', '')\
                                 .replace(']', '')
    print(clean_brackets)
    return clean_brackets.split(' ')
# ======================================================================================================================
# curry the above to create a series of lists for processing


def reference_iterator(input_string):
    """creates the iterator that's needed for your API calls."""
    return list(verse_slice(de_fancypantsify(input_string)))


"[Luke 24:1-5 KJV]"

'''
curl --request GET \
--url https://api.scripture.api.bible/v1/books \
--header '***'
'''
# ======================================================================================================================
# error catching functions


def versions_transformer(query_input, versions_dict_input):
    """Grabs the version and casts it to a list"""
    processed_query = query_input.upper()
    for i in list(versions_dict_input.keys()):
        result = re.search(str(i), processed_query)
        if result is not None:
            version = versions_dict_input[result.group(0)]
            reduced_query = processed_query.replace(result.group(0), '')
            return [version, reduced_query]
    failover_reduced_query = processed_query.split(' ')
    failover_reduced_query = failover_reduced_query.pop(len(failover_reduced_query) - 1)
    return [versions_dict_input['KJV'], str.join('', failover_reduced_query)]


def book_transformer(query_input, book_dict_input):
    """grabs the book and casts it to a list"""
    sample_version = versions_dict.versions_dict()
    query_input[1] = query_input[1].replace('[', '').replace(']', '').lstrip().rstrip().upper()
    for i in list(book_dict_input.keys()):
        result = re.search(i, query_input[1])
        if result is not None:
            book = book_dict_input[result.group(0)]
            reduced_query = query_input[1].replace(result.group(0), '')
            return [query_input[0], book, reduced_query]
    return [sample_version['KJV'], 'error book not found']


def verse_transformer(query_input):
    """creates the compliant verse reference"""
    if query_input[1] == 'error book not found':
        query_input[1] = query_input[1].replace(' ', ".")
        return query_input
    verse = query_input[2]
    verse = verse.replace('[', '').replace(']', '').lstrip().rstrip()
    book = query_input[1]
    verse = verse.split(':')
    if '-' in verse[1]:
        verse_section_list = verse[1].split('-')
        return [query_input[0],
                str.join('', (book, '.', verse[0], '.', verse_section_list[0], '-',
                              book, '.', verse[0], '.', verse_section_list[1]))]
    else:
        return [query_input[0], str.join("", (book, '.', verse[0], '.', verse[1]))]


def query_transformer(input_string):
    """QUERY CURRY"""
    versions = versions_dict.versions_dict()
    books = books_dict.books_dict()
    versions_transformer_partial = partial(versions_transformer, versions_dict_input=versions)
    book_transformer_partial = partial(book_transformer, book_dict_input=books)
    return verse_transformer(book_transformer_partial(query_input=versions_transformer_partial(query_input=input_string)
                                                      ))


# ======================================================================================================================

# ======================================================================================================================


def response_builder(query_input, api_key_input):
    """Makes the actual request"""
    url = ["https://api.scripture.api.bible/v1/bibles/", query_input[0], "/passages/", query_input[1]]
    querystring = {"content-type": "text",
                   "include-notes": "false",
                   "include-titles": "false",
                   "include-chapter-numbers": "false",
                   "include-verse-numbers": "true",
                   "include-verse-spans": "false",
                   "use-org-id": "false"}
    headers = {'api-key':  str(api_key_input)}
    api_call = requests.get(str.join('', url), headers=headers, params=querystring)
    print(api_call)
    return api_call


def error_code_handler(json_input_object):
    """I pass everything as a response now, so I technically produce only valid responses.
       This will work later down the way so when the response is compiled, it's a formatted error message."""
    json_input = json.loads(json_input_object.text)
    if 'statusCode' in json_input.keys():
        if not json_input['statusCode'] == '200':
            json_input['copyright'] = 'Malformed Request'
            json_input['reference'] = "***\nif you are seeing this, You have made a malformed request. \n\n " \
                                      "Please ensure that you have picked a book and version that is accessible, " \
                                      "as well as formed the request correctly. \n\n , simply mention this bot\'s " \
                                      "username, and state look up somewhere in your comment. \n\n Then you can " \
                                      "specify as many verse selections under the 8000 character limit\n\n like " \
                                      "this: [John 3:16 KJV]"
            json_input['content'] = str.join('', (json_input['error'], ':', '\n\n',   json_input['message']))
            fake_data_holder = dict()
            fake_data_holder['data'] = json_input
            return json_input
    else:
        return json_input['data']


def footer():
    """feets"""
    footer_list = '^^^(this) ^^^(bot) ^^^(uses) ^^^(the) [^^^(scripture.api.bible)](https://scripture.api.bible/) ' \
                  '^^^(web) ^^^(services) ^^^(from) [^^^(American) ^^^(Bible) ^^^(Society)]' \
                  '(https://www.americanbible.org/) ^^^(|) [^^^source ^^^code]' \
                  '(https://github.com/matthewdaffern/redditbot) ^^^(|) [^^^message ' \
                  '^^^the ^^^developers](https://www.reddit.com/message/compose?to=/r/scripturebot)'
    return str.join('', footer_list)


def config_loader(json_input):
    """generic json parsers"""
    json_file = open(json_input, 'r+')
    return json.load(json_file)


def full_response_creator(input_string, api_key_input):
    """creates the response by currying everything"""
    configured_response = partial(response_builder, api_key_input=api_key_input)
    return comment_creator(error_code_handler(configured_response(query_input=query_transformer(input_string))))


def rest_text_to_json_list(response_json_input):
    """removes that pesky 'data' object label"""
    json_object = json.loads(response_json_input.text)
    return json_object['data']


def make_the_copyright_tinier(string_input):
    return string_input.replace(' ', ' ^^^')


def comment_creator(json_input):
    """ references the required elements from the dictionary object that's always passed around.
        Note I just need to create the respective keys, and it'll work well."""
    return str.join('', ('**',
                         json_input['reference'],
                         '**'
                         '\n***\n',
                         json_input['content'],
                         '\n***\n',
                         make_the_copyright_tinier(str("^^^" + json_input['copyright']))))


def add_footer(content, dev_footer):
    return str.join('', (content,  dev_footer))
# ======================================================================================================================
# this is where you map your API calls over your valid list of queries.


def section_too_long(processed_comment):
    if len(processed_comment) > 8000:
        return str.join('', ('Your query exceeds 8000 characters', '\n***\n', footer()))
    else:
        return processed_comment


def remove_quad_spaces(processed_comment):
    return processed_comment.replace('    ', '')


def verse_sections(input_string, api_key_input):
    verse_list = reference_iterator(input_string)
    comment_creator_partial = partial(full_response_creator, api_key_input=api_key_input)
    comment_results = list(map(lambda x: comment_creator_partial(input_string=x), verse_list))
    return section_too_long(remove_quad_spaces(str.join('\n\n', (comment_results + [footer()]))))

# Rest API format is:
# "https://api.scripture.api.bible/v1/bibles/#bibleID/verses/Luk.24.2"
# I should create a dict with the bibles I intend to support. The verse code is fairly easy,
# I just need to use another dict.

# url = "https://api.scripture.api.bible/v1/bibles/bible_id/passages/Luk.12.12-Luk.12.14" workable format.

# ======================================================================================================================
