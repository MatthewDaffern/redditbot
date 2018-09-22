import requests
import log
import API_keys
import time

def rate_limiter():
    whole_second = 1
    divisor = 50
    rate_limiting_time = whole_second / divisor
    initial_time = time.time()
    final_time = time.time()
    time_difference = final_time-initial_time
    while time_difference < rate_limiting_time:
        final_time = time.time()
        time_difference = final_time-initial_time
        
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
    if 'error' in input_string:
        return input_string
    query = input_string.replace(':', '.')
    while "  " in query:
        query = query.replace('  ', ' ')
    query = query.split(" ")
    for i in query:
        if 'scripture_bot' in i:
            index_of_username_mention = query.index(i)
            username_test = i
            break
    versions = version_dict
    search_indice = index_of_username_mention
    version_query = 1
    while version_query == 1:
        if query[search_indice] in versions:
            break
        search_indice = search_indice + 1
    query_slice = query[index_of_username_mention:int(search_indice+1)]
    bible_version = 'error: version not found'
    chapter_verse = 'error: chapter verse not found'
    username_mention = 'error: username not found'
    for i in query_slice:
        username_test = i
        if i in versions:
            bible_version = i
        if 'u/scripture_bot' in username_test:
            username_mention = i
        if '.' in i:
            chapter_verse = i
    query_slice.remove(bible_version)
    query_slice.remove(username_mention)
    print(query_slice)
    if '.' not in chapter_verse:
        chapter_verse = query_slice[len(query_slice)-1]
    query_slice.remove(chapter_verse)
    bible_version = bible_version.upper()
    book = str(query_slice[0]).capitalize()
    if len(query_slice) > 1:
        book = str()
        for i in query_slice:
            i = str(i)
            book = book+i.capitalize()+'+'
        book = book.rstrip(' + ')
    final_query = [book, chapter_verse, bible_version]
    print(final_query)
    # should now be ['john','3.16',"KJV"]
    return final_query


test1 = comment_parser('u/scripture_bot! 3:1 song of solomon KJV ', available_versions())
test2 = comment_parser('/u/scripture_bot! 1 Corinthians 1: ESV ', available_versions())


def biblia_api_key_storage():
    return API_keys.biblia()


def esv_api_key_storage():
    return API_keys.esv()


def text_creator(response_builder):
    return response_builder.text


def esv_response_builder(query, api_key):
    rate_limiter()
    mode = 'text'
    additional_parameters = str('&include-passage-references=false&' +
                                'include-footnotes=false&' +
                                'include-headings=false' +
                                '&include-line-breaks=false')
    url = 'https://api.esv.org/v3/passage/'+mode+'/?q='+query[0]+'+'+query[1]+additional_parameters
    headers = {'authorization': str(api_key)}
    print('the API call is:  '+url)
    api_call = requests.get(url, headers=headers)
    return api_call


def biblia_response_builder(query, api_key):
        rate_limiter()
        api_call = 'https://api.biblia.com/v1/bible/content/'+query[2]+'.txt.js?passage='+query[0]+query[1]
        api_call = api_call+'&callback=myCallbackFunction&key='+api_key
        api_call = api_call.replace('0A', '')
        api_call = api_call.replace('%', '')
        print(api_call)
        r = requests.get(api_call)
        return r

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
        .replace('(esv)"', '(esv)')
    while '  ' in removed_characters:
        removed_characters = removed_characters.replace('  ',' ')
    esv_response_body = removed_characters 
    return esv_response_body

    

raw_response_biblia = str(text_creator(biblia_response_builder(test1,biblia_api_key_storage())))
raw_response_esv = str(final_esv_response(text_creator(esv_response_builder(test2,esv_api_key_storage()))))

print(biblia_response_builder(test1,biblia_api_key_storage()))
print(esv_response_builder(test1,esv_api_key_storage()))
print(raw_response_biblia)
print(raw_response_esv)
