import new_Common

command_options = new_Common.command_options()
command_list = new_Common.command_list()
footer = new_Common.footer()
content_variable = 'lol'
plus_footer = new_Common.add_footer(content_variable, footer)
test_verses_malformed_bracket = 'John 2:1 KJV'
test_verses_malformed_chapter = 'John :1 KJV'
test_verses_malformed_verse = 'John 1: KJV'
test_verses_proper = 'John 3:16 KJV'
selection = '[' + str.join('][', (test_verses_proper, 'asdfasd', test_verses_proper,'as[dfasd]', test_verses_proper)) + ']'

result = new_Common.verse_slice(selection)
neatify = new_Common.neatify_string_to_list(result[0])

create_iterator = new_Common.reference_iterator(selection)

single_verse = create_iterator[0]

transformation_test = new_Common.query_transformer(single_verse)
print(transformation_test)
'''
print(command_options)
print(command_list)
print(footer)
print(plus_footer)
new_Common.verse_slice(input_string)
new_Common.neatify_string_to_list(input_string)
new_Common.reference_iterator(input_string)
'''
'''

new_Common.versions_transformer(query_input, versions_dict_input)
new_Common.book_transformer(query_input, book_dict)
new_Common.verse_transformer(query_input)
new_Common.query_transformer(input_list)
new_Common.error_code_handler(json_input)

new_Common.config_loader(json_input)
new_Common.rest_text_to_json_list(json_input)
new_Common.comment_creator(json_input)

new_Common.no_swearing(input_string)
new_Common.section_too_long(processed_comment)

new_Common.insult_generator(input_string, api_key)
new_Common.repeat_after_me(input_string, api_key)
new_Common.command_processor(input_string, api_key_input)
new_Common.response_builder(query_input, api_key)
new_Common.return_verse_sections(input_list, api_key_input)
new_Common.full_response_creator(input_string, api_key)
'''