from Common import *

test1 = comment_parser('u/scripture_bot! 3:1 song of solomon KJV ', available_versions())
test2 = comment_parser('/u/scripture_bot! 1 Corinthians 1: ESV ', available_versions())

raw_response_biblia = str(text_creator(biblia_response_builder(test1,biblia_api_key_storage())))
raw_response_esv = str(final_esv_response(text_creator(esv_response_builder(test2,esv_api_key_storage()))))

print(biblia_response_builder(test1,biblia_api_key_storage()))
print(esv_response_builder(test1,esv_api_key_storage()))
print(raw_response_biblia)
print(raw_response_esv)

