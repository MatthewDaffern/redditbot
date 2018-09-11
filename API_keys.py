def Biblia():
#parse the key from a text file that's in the .gitignore
        BibliaKeyFile=open('API_Keys','r+')
        key=str()
        BibliaKey=list(BibliaKeyFile.readlines())
        for i in BibliaKey:
                if  'Biblia' in str(i):
                        KeyTextLine=str(i)
                        KeyTextLine=KeyTextLine.split(",")
                        key=KeyTextLine[1]
        return key
def ESV():
#parse the key from a text file that's in the .gitignore
        ESVKeyFile=open('API_Keys','r+')
        ESVKey=list(ESVKeyFile.readlines())
        key=str()
        for i in ESVKey:
                if  'ESV' in str(i):
                        KeyTextLine=str(i)
                        KeyTextLine=KeyTextLine.split(",")
                        key=KeyTextLine[1]
        return key
