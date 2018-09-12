from common import (biblia_api_key_storage,
                    esv_api_key_storage,
                    comment_parser,
                    esv_response_builder,
                    final_esv_response,
                    text_creator,
                    biblia_response_builder,
                    final_biblia_response,
                    biblia_footer,
                    esv_footer,
                    api_error_handler,
                    length_checker,
                    full_comment_string,
                    biblia,
                    esv,
                    query_processor,
                    requests_object_caller)
biblia_key = biblia_api_key_storage()
esv_key = esv_api_key_storage()

print('the biblia key is: '+biblia_key)
print('the esv key is: '+esv_key)




raw_biblia_comment = '/u/scripture_bot! john 3:16 KJV'
raw_esv_comment = '/u/scripture_bot! john 3:16 ESV'
parsed_biblia_comment = comment_parser(raw_biblia_comment)
parsed_esv_comment = comment_parser(raw_esv_comment)

print('the parsed biblia comment is '+str(parsed_biblia_comment))
print('the parsed esv comment is '+str(parsed_esv_comment))


correct_biblia_requests_object = biblia_response_builder(parsed_biblia_comment, biblia_key)
print('the api response code from biblia is: '+str(correct_biblia_requests_object))
biblia_http_code = api_error_handler(correct_biblia_requests_object)
print('the error result from the api error handler for biblia is: '+biblia_http_code)
biblia_raw_text = text_creator(correct_biblia_requests_object)
print('the biblia raw text is :'+str(biblia_raw_text))


#ESV is correct so far!

for i in range(50):
    correct_biblia_requests_object = biblia_response_builder(parsed_biblia_comment, biblia_key)
    print(correct_biblia_requests_object)


'''
correct_esv_requests_object = esv_response_builder(parsed_esv_comment, esv_key)
print('the api response code from esv is: '+str(correct_esv_requests_object))
esv_http_code = api_error_handler(correct_esv_requests_object)
print('the error result from the api error handler for esv is: '+esv_http_code)
esv_raw_text = text_creator(correct_esv_requests_object)
print('the esv raw text is :'+str(esv_raw_text))


biblia_processed_text = final_biblia_response(biblia_raw_text)
esv_processed_text = final_esv_response(esv_raw_text)

print('the processed text for biblia is '+biblia_processed_text)
print('the processed text for esv is '+esv_processed_text)

print(biblia_footer())
print(esv_footer())

esv_full_comment_string = full_comment_string(raw_esv_comment, esv_processed_text, esv_footer())
biblia_full_comment_string = full_comment_string(raw_biblia_comment, biblia_processed_text, biblia_footer())

print(esv_full_comment_string)
print(biblia_full_comment_string)

print('length checker result is: '+length_checker(esv_full_comment_string))

esv_comment = esv(raw_esv_comment, correct_esv_requests_object)
print(esv_comment)

biblia_comment = biblia(raw_biblia_comment, correct_biblia_requests_object)
print(biblia_comment)


esv_query_processor = query_processor(raw_esv_comment, requests_object_caller(raw_esv_comment))
print(esv_query_processor)

biblia_query_processor = query_processor(raw_biblia_comment, requests_object_caller(raw_biblia_comment))
print(biblia_query_processor)
'''
