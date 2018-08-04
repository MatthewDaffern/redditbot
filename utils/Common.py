
import requests
import API_Keys



'''API Key Storage Functions'''
def Biblia_API_Key_Storage():
    return API_Keys.Biblia()

 def Bible_API_Key_Storage():
    return API_Keys.BibleAPI()   

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

'''Biblia Functions'''
def Biblia_Text_Creator(Response_Builder):
    return Response_Builder.text
def Biblia_Response_Builder(query,APIkey):
    #example API call
    #https://api.biblia.com/v1/bible/content/{bible}.{outputFormat}?passage={bibleReference}&key={API key}
    #expects the query to be in the following format KJV,John,3:16
        api_call='https://api.biblia.com/v1/bible/content/'+str(query[0])+'.js'+'?passage='+query[1]+query[2]+'&key='+APIkey
        api_return=requests.get(api_call)
        return api_return
def Final_Biblia_Response(input):
    Biblia_Response=input
    Biblia_Response_Stripped_Front=Biblia_Response.strip('"myCallbackFunction({"text":"')
    Biblia_Response_Stripped_Back=Biblia_Response_Stripped_Front.strip('"});')
    Biblia_Response_Final=Biblia_Response_Stripped_Back
    Biblia_Response_Body=Biblia_Response_Final+"!!!!Biblia"
    return Biblia_Response_Body
def Biblia_Footer():
    Couple_of_Spaces="\n \n"
    TOS_footer="^(This) ^(Bot) ^(uses) ^(the) [^(Biblia)](https://biblia.com/) ^(web) ^(services) ^(from) [^(Logos Bible Software)](https://www.logos.com/))"
    Github_Footer="^(|) [^(Source Code)](https://github.com/MatthewDaffern/redditbot])"
    Message_The_Developers_Footer+'^(|) [^(Message the developers)](https://www.reddit.com/message/compose?to=/r/scripturebot)'
    footer=Couple_of_Spaces+TOS_footer+Github_Footer+Message_The_Developers_Footer
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
def Format_enforcer:
    #To do. This will all depend on how the BIBLE API operates.
'''Comment Building Functions '''
def full_comment_string(input_string, Response_Body):
    #input string is the string initially used to make the API call.
    bot_username="/u/scripturebot!"
    converted_query=input_string.strip(bot_username)
    Response_Body=Response_Body.split("!!!!")
    header=str("*"reconverted_query+"*"+"\n \n")
    if Response_Body[1]=="Biblia":
        footer=Biblia_Footer()
    if Response_Body[1]=="BibleAPI":
        footer=BibleAPI_Footer()
    final_comment=header+Response_Body_Final+footer
    return final_comment

'''Bible API Functions '''
def BibleAPI_Response_Builder(query,APIKey):
    #place an example API call
    # do error handling and shape the query to work with the API
    api_call='placeholder'#concatenate a string for making the call
    api_return=requests.get(api_call)
        return api_return.json
    else:
        return "error response"#return an error response that can be handled by the actual bot
def Final_BibleAPI_Response(JSON_input):
    #parse the JSON
    #turn it into a string
    #conform properly to Reddit Markdown requirements to make it look nice
    #add neccesary edits to comply with the API TOS
    Final_JSON_input=str(Final_JSON_input)
    return Final_JSON_input







