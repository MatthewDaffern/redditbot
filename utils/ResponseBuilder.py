
import requests
import API_Keys
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
def Biblia_API_Key_Storage():
    return API_Keys.Biblia()
def Biblia_Response_Builder(query,APIkey):
    #example API call
    #https://api.biblia.com/v1/bible/content/{bible}.{outputFormat}?passage={bibleReference}&key={API key}
    #expects the query to be in the following format KJV,John,3:16
        api_call='https://api.biblia.com/v1/bible/content/'+str(query[0])+'.js'+'?passage='+query[1]+query[2]+'&key='+APIkey
        api_return=requests.get(api_call)
        api_return=api_return.text
        return api_return
def Final_Biblia_Response(input):
    Biblia_Response=input
    Biblia_Response_Stripped_Front=Biblia_Response.strip('"myCallbackFunction({"text":"')
    Biblia_Response_Stripped_Back=Biblia_Response_Stripped_Front.strip('"});')
    Biblia_Response_Final=Biblia_Response_Stripped_Back
    Biblia_Response_Body=Biblia_Response_Final
    #conform properly to Reddit Markdown requirements to make it look nice
    #add neccesary edits to comply with the API TOS
    return Biblia_Response_Body
def full_comment_string(input_string, Response_Body):
    #query should be the list returned from the comment parser
    bot_username="/u/scripturebot!"
    converted_query=input_string.strip(bot_username)

    header=str("*"reconverted_query+"*"+"/n /n")
    final_comment=header+Response_Body

# Single Line of Biblia Backend  full_comment_string(input_string,Final_Biblia_Response(Biblia_Response_Builder(comment_parser(input_string),Biblia_API_Key_Storage())))
# Less insane, easier to understand backend.
# comment=comment_parser(input_string)
# Biblia_Response=Biblia_Response_Builder(comment,Biblia_API_Key_Storage())
# Final_Biblia_Response_String=Final_Biblia_Response(Biblia_Response)
# returned_comment=full_comment_string(input_string,Final_Biblia_Response_String)
def Bible_API_Key_Storage():
    return API_Keys.BibleAPI()
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


'''
class ResponseBuilder:
    def __init__(self):
        self.__standards = {
            WLC(),
            WSC(),
            HC(),
            BCF(),
            WCF(),
            LBCF89(),
            ARTICLES(),
            CDA(),
            CDR()
        }
        self.__text = ''
        self.__citation = ''
        self.__malformed = False
        self.__footer = ('\n\n***\n[^Code](https://github.com/Nokeo08/standardsbot) ^|'
                         ' [^Contact ^Dev](/message/compose/?to=nokeo08) ^|'
                         ' [^Usage](https://github.com/Nokeo08/standardsbot/blob/master/README.md#usage) ^|'
                         ' [^Changelog](https://github.com/Nokeo08/standardsbot/blob/master/CHANGELOG.md) ^|'
                         ' [^Find ^a ^problem? ^Submit ^an ^issue.](https://github.com/Nokeo08/standardsbot/issues)')

    def __reset(self):
        self.__append('', '', False, True)

    def __append(self, text, citation='', malformed=False, overwrite=False):
        if overwrite:
            self.__text = text
            self.__citation = citation
            self.__malformed = malformed
        else:
            self.__text += text
            self.__citation += citation
            self.__malformed |= malformed

    def __append_response(self, response):
        if len(response) != 3:
            raise NotImplementedError
        self.__append(response[0], response[1], response[2])

    def fetch(self, citations):
        self.__reset()
        if citations:
            for standard in self.__standards:
                self.__append_response(standard.fetch(citations))

            if self.__malformed:
                self.__append("\n\n**Your request contained one or more malformed requests that I could not fulfill.**")

            if len(self.__text) > 0:
                if len(self.__text) > 9500:
                    self.__append(
                        "Citation contains more than the maximum number characters allowed in a comment.",
                        "Comment overflow",
                        False,
                        True
                    )
                self.__append(self.__footer)
            return self.__text, self.__citation, self.__malformed
'''