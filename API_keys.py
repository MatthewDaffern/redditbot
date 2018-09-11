def biblia():
#parse the key from a text file that's in the .gitignore
        bibliakeyfile=open('api_keys','r+')
        key=str()
        bibliakey=list(bibliakeyfile.readlines())
        for i in bibliakey:
                if  'biblia' in str(i):
                        keytextline=str(i)
                        keytextline=keytextline.split(",")
                        key=keytextline[1]
        return key
def esv():
#parse the key from a text file that's in the .gitignore
        esvkeyfile=open('api_keys','r+')
        esvkey=list(esvkeyfile.readlines())
        key=str()
        for i in esvkey:
                if  'esv' in str(i):
                        keytextline=str(i)
                        keytextline=keytextline.split(",")
                        key=keytextline[1]
        return key
