def Biblia():
	#parse the key from a text file that's in the .gitignore
	BibliaKeyFile=open('API_Keys','r+')
	key=str()
	for i in BibliaKeyFile:
		if  'Biblia' in str(i):
			KeyTextLine=str(i)
			KeyTextLine=KeyTextLine.split(",")
			key=KeyTextLine[1]
	return key
def BibleAPI():
	#parse the key from a text file that's in the .gitignore
    BibleAPIKeyFile=open('API_Keys','r+')
	key=str()
	for i in BibleAPIFile:
		if  'BibleAPI' in str(i):
			KeyTextLine=str(i)
			KeyTextLine=KeyTextLine.split(",")
			key=KeyTextLine[1]
	return key