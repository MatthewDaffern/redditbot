#!/usr/bin/python
# -*- coding: utf-8 -*-

from standards import *
import requests

def ResponseBuilder(query,APIkey):
    #example API call
    #https://api.biblia.com/v1/bible/content/{bible}.{outputFormat}?passage={bibleReference}&key={API key}
    #expects the query to be in the following format KJV,John 3:16
    if "," in query:
        query.split(",")
        #changes the verse selection to fit the requirements of the API
        verse_query=str()
        placeholder_verse_query=str(query[1])
        for i in placeholder_verse_query:
            if i==":":
                verse_query=verse_query+"."
            else:
                verse_query=verse_query+i
        verse_query=str.replace(" ","")
        query[1]=verse_query

        api_call='https://api.biblia.com/v1/bible/content/'+str(query[0])+'.js'+'?passage='+query[1]+'&key='+APIkey
        api_return=requests.get(api_call)
        return api_return.json
    else:
        return "malformed request. comma must go between the bible verse and book"


    



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