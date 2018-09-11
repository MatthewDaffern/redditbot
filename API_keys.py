

def biblia():
    bibliakeyfile = open('config_file', 'r+')
    key = str()
    bibliakey = list(bibliakeyfile.readlines())
    for i in bibliakey:
        if 'biblia' in str(i):
            keytextline = str(i)
            keytextline = keytextline.split(": ")
            key = keytextline[1]
    return key


def esv():
    esvkeyfile = open('config_file', 'r+')
    esvkey = list(esvkeyfile.readlines())
    key = str()
    for i in esvkey:
        if 'esv' in str(i):
            keytextline = str(i)
            keytextline = keytextline.split(": ")
            key = keytextline[1]
    return key
