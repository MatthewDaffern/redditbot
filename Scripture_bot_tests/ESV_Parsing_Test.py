import requests
#API_KEY=Put api Key here
headers={'Authorization': API_KEY}
totalurl='https://api.esv.org/v3/passage/text/?q=John+1&include-passage-references=false&include-footnotes=false&include-headings=false'
r=requests.get(totalurl, headers=headers)
test=r.text
def Final_ESV_Response(input_string):
        removed_data=input_string.split('"passages"')
        removed_data=removed_data[1]
        removed_newlines=removed_data.replace('\\n','')
        removed_utf8_characters=removed_newlines.replace('\\u201d','').replace('\\u201c','').replace('\\u2019','').replace('\\u2018','')
        fixed_formatting=removed_utf8_characters..replace(': [" ','').replace(']}','').replace('(ESV)"','(ESV)')
        print(input_string)
        return input_string
Final_ESV_Response(test)
