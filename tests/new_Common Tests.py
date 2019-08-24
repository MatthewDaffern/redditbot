import new_Common
import books_dict
import versions_dict
'''
# testing to make sure I can call the commands
command_options = new_Common.command_options()
command_list = new_Common.command_list()
footer = new_Common.footer()
content_variable = 'lol'
# Tested the footer
plus_footer = new_Common.add_footer(content_variable, footer)

# Test variable list.

test_verses_malformed_bracket = 'John 2:1 KJV'
test_verses_malformed_chapter = 'John :1 KJV'
test_verses_malformed_verse = 'John 1: KJV'
test_verses_proper = 'John 3:16-18 KJV'
selection = '[' + str.join('][', (test_verses_proper,
                                  'asdfasd',
                                  test_verses_proper,
                                  'as[dfasd]',
                                  test_verses_proper)) + ']'
# initialize the versions and books for later tests.
versions = versions_dict.versions_dict()
books = books_dict.books_dict()
result = new_Common.verse_slice(selection)
print(result)
neatify = new_Common.neatify_string_to_list(result[0])

malformed_neatify = neatify
malformed_neatify[0] = 'lol'
'''

def api():
    api_file = open('api.key', 'r+')
    key = api_file.readlines()[0]
    return key


key = api()

input_test = 'ckiks'


'''
print(str.encode(key))

test = new_Common.response_builder(transformed_query, key)


text = new_Common.rest_text_to_json_list(test.text)

print(text)

comment = new_Common.comment_creator(text)

print(comment)
'''

print(new_Common.command_processor(input_test, key))

'''
print(new_Common.error_code_handler(new_Common.response_builder(malformed_neatify, key)))
'''
'''
print(command_options)
print(command_list)
print(footer)
print(plus_footer)
new_Common.verse_slice(input_string)
new_Common.neatify_string_to_list(input_string)
new_Common.reference_iterator(input_string)
new_Common.versions_transformer(query_input, versions_dict_input)
new_Common.book_transformer(query_input, book_dict)
new_Common.verse_transformer(query_input)
new_Common.query_transformer(input_list)
new_Common.response_builder(query_input, api_key)
new_Common.rest_text_to_json_list(test.text)
new_Common.return_verse_sections(input_list, api_key_input)
new_Common.full_response_creator(input_string, api_key)
new_Common.no_swearing(input_string)
new_Common.repeat_after_me(input_string, api_key)
new_Common.insult_generator(input_string, api_key)
new_Common.section_too_long(processed_comment)
new_Common.error_code_handler(json_input)
new_Common.config_loader(json_input)



'''