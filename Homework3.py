def prblmUno():
    name = "Roy G Biv"
    s = "s"
    p = "p"

    print("mi" + s*2 + "i" + s*2 + "i" + p*2 + "i")

    for i in range(len(name)+1):
        print(name[0:i])

#this function replaces iss with ox in mississippi
def prblmDos():
    astring = "mississippi"
    d = astring.replace("iss", "ox")
    return d

#this is how you center and capitalize python
def prettySnake():
    cstring = "python"
    a = cstring.upper()
    b = a.center(20)
    return b

def scramble2Decrypt(cipherText):
    halfLength = len(cipherText) // 2
    oddChars = cipherText[:halfLength]
    evenChars = cipherText[halfLength:]
    plainText = ""

    for i in range(halfLength):
        plainText = plainText + evenChars[i]
        plainText = plainText + oddChars[i]

    if len(oddChars) < len(evenChars):
        plainText = plainText + evenChars[-1]

    return plainText


def stripSpaces(myString):
    g = myString.replace(" ", "")
    return g


def removeChar(daString,idx):
    pa = ""
    pb = ""
    for i in range(idx):
        pa = pa + daString[i]
    for j in range(idx + 1, len(daString)):
        pb = pb + daString[j]

    pf = pa + pb    
    return pf

#Caesar ENCRYPTION function
def caesarEn(hString,numRot):
    alphabet = 'abcdefghijklmnopqrstuvwxyz '
    q = len(hString)
    newStr = ''
    for i in range(0, q):
        a = (alphabet.index(hString[i]) + numRot)
        
        if a > 27:
            a = a - 27
        midStr = alphabet[a]
        newStr = newStr + midStr
        print(newStr) 
    return newStr    
        
#Caesar DECRYPTION function        
def caesarDe(hString,numRot):
    alphabet = 'abcdefghijklmnopqrstuvwxyz '
    q = len(hString)
    newStr = ''
    for i in range(0, q):
        a = (alphabet.index(hString[i]) - numRot)
        
        if a < 0:
            a = a + 27
        midStr = alphabet[a]
        newStr = newStr + midStr
        print(newStr) 
    return newStr 
















