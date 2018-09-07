
import requests
import API_Keys

#Separate flow control from the lower order functions.
#Use higher order functions for the flow control decision
#So this means the following:
#   Abstract away each API service functions into a single function for each API.
#   This will make it easier to perform my unit testing
#   Eventually operate it off a single function.
'''API Key Storage Functions'''
def Biblia_API_Key_Storage():
    return API_Keys.Biblia()

 def ESV_API_Key_Storage():
    return API_Keys.ESV()   

'''Reddit Parsing Functions'''
def comment_parser(input_string): 
    #expects the format:
    # /u/biblebot! John 3:16 KJV
    query=input_string.split(" ")
    query=query[1:3]
    Verse_Chapter=query[1]
    Verse_Chapter=Verse_Chapter.split(":")
    Verse_Chapter=str(Verse_Chapter[0]+"."+Verse_Chapter[1])
    query[1]=Verse_Chapter
    #Should now be ['John','3.16',"KJV"]
    return query
'''Bible Functions'''
def ESV_Response_Builder(query,APIkey):
    mode='text'
    url='https://api.esv.org/v3/passage/'+mode+'/?q'+query[0]+'+'+query[1]
    headers={'authentication':str(' '+APIkey)}
    esv_api_call=requests.get(url, headers=headers)
    return esv_api_call

    #where you last left off
def Final_ESV_Response(input_string):
    print()
    return ESV_Response_Body
    #fill this with more stuff
    
def Text_Creator(Response_Builder):
    return Response_Builder.text
def Biblia_Response_Builder(query,APIkey):
    #example API call
    #https://api.biblia.com/v1/bible/content/{bible}.{outputFormat}?passage={bibleReference}&key={API key}
    #expects the query to be in the following format KJV,John,3:16
        esv_api_call='https://api.biblia.com/v1/bible/content/'+str(query[0])+'.js'+'?passage='+query[1]+query[2]+'&key='+APIkey
        biblia_api_return=requests.get(api_call)
        return biblia_api_return
def Final_Biblia_Response(input_string):
    Biblia_Response=input_string
    Biblia_Response_Stripped_Front=Biblia_Response.strip('"myCallbackFunction({"text":"')
    Biblia_Response_Stripped_Back=Biblia_Response_Stripped_Front.strip('"});')
    Biblia_Response_Final=Biblia_Response_Stripped_Back
    Biblia_Response_Body=Biblia_Response_Final+
    return Biblia_Response_Body
def Biblia_Footer():
    Couple_of_Spaces="\n \n"
    TOS_footer="^(This) ^(Bot) ^(uses) ^(the) [^(Biblia)](https://biblia.com/) ^(web) ^(services) ^(from) [^(ESV)](https://www.logos.com/))"
    Github_Footer="^(|) [^(Source Code)](https://github.com/MatthewDaffern/redditbot])"
    Message_The_Developers_Footer+'^(|) [^(Message the developers)](https://www.reddit.com/message/compose?to=/r/scripturebot)'
    footer=Couple_of_Spaces+TOS_footer+Github_Footer+Message_The_Developers_Footer
    return footer 
def ESV_footer():
    ESV="*ESV*"
    Couple_of_Spaces="\n \n"
    TOS_footer="^(This) ^(Bot) ^(uses) ^(the) [^(ESV)](https://api.esv.org/docs/) ^(web) ^(services) ^(from) [^(Logos Bible Software)](https://www.logos.com/))"
    Github_Footer="^(|) [^(Source Code)](https://github.com/MatthewDaffern/redditbot])"
    Message_The_Developers_Footer+'^(|) [^(Message the developers)](https://www.reddit.com/message/compose?to=/r/scripturebot)'
    footer=ESV+Couple_of_Spaces+TOS_footer+Github_Footer+Message_The_Developers_Footer
    return footer 
'''Error Handling Functions'''
def API_Error_Handler(Response_Builder):
    #expects a requests object as input
    if "200" not in str(Response_Builder):
        return "Error: One or more queries could not be handled.(API HANDLING HAS MALFUNCTIONED)"
    if "200" in str(Response_Builder):
        return "Success" 
def input_sanitization(Response_Builder):
    forbidden_words_and_symbols_list=['(',")",";","def","return","class","exec","eval","import"]
    for i in forbidden_words_and_symbols_list:
        if i in str(Response_Builder):
            return(Error: Malformed Input)
    return("Success")
def length_checker(final_comment):
    if len(final_comment)>8000:
        return "Error:your request could not be fulfilled to to the size constraint on reddit comments. It might be best to paste from your favorite website."
    else:
        return("Success")
'''Comment Building Functions '''
def full_comment_string(input_string, Response_Body,footer_input):
    #input string is the string initially used to make the API call.
    bot_username="/u/scripturebot!"
    converted_query=input_string.strip(bot_username)
    header=str("*"reconverted_query+"*"+"\n \n")
    footer=footer_input
    final_comment=header+Response_Body_Final+footer
    return final_comment

'''Higher order Functions '''
def Biblia(input_string):
    api_call=Biblia_Response_Builder(input_string,Biblia_API_Key_Storage())
    API_Error_Handling=API_Error_Handler(api_call)
    if 'Error' in API_Error_Handling:
        return "API_Error_Handling"
    Biblia_body=Final_Biblia_Response(Text_Creator(api_call))
    response=full_comment_string(input_string, Biblia_body, Biblia_Footer())
    lengthtest=length_checker(response)
    if 'Error' in lengthtest:
        return lengthtest
    return response
def ESV(input_string):
    api_call=ESV_Response_Builder(input_string,ESV_API_Key_Storage())
    API_Error_Handling=API_Error_Handler(api_call)
    if 'Error' in API_Error_Handling:
        return "API_Error_Handling"
    Biblia_body=Final_ESV_Response(Text_Creator(api_call))
    response=full_comment_string(input_string, Biblia_body, ESV_Footer())
    lengthtest=length_checker(response)
    if 'Error' in lengthtest:
        return lengthtest
    return response
def query_wrapper(input_string):
    if "ESV" in input_string:
        final_query=ESV(input_string)
    if "ESV" not in input_string
        final_query=Biblia(input_string)
    return final_query
