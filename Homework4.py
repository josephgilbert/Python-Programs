

def twoCount(thelist, tar):
    cntr = 0
    for i in range(0,len(thelist)):
        if thelist[i] == tar:
            cntr = cntr + 1
    return cntr        

def twoIn(thelist, tar):
    for i in range(0, len(thelist)):
        if thelist[i] == tar:
            return True
        
def twoReverse(thelist):
    plagiarism = [ ]
    for i in range(0, len(thelist)):
        plagiarism.append(thelist.pop())
    return plagiarism

def twoIndex(thelist, item):
    c = 0
    alist = thelist[:]
    
    for i in range(len(thelist)):
        
        a = thelist[i]
        if a == item:
            c = c + 1
            print (i)
        elif i == len(thelist)-1 and c < 1:
            return (-1)

def twoInsert(thelist, idx, item):
    d = thelist[0:idx]
    n = thelist[idx-1:]
    d.append(item)
    b = d + n
    return b


name = ['joe', 'tom', 'barb', 'sue', 'sally']
scores = [10, 23, 13, 18, 12]

def makeDictionary(name, scores):
    scoreDict = {}
    for k in range(len(name)):
        a = name[k]
        b = scores[k]
        scoreDict[a] = b
    print (scoreDict)    
            
           
        










    
        
        
            
            
            
        
        
        
                
        
            
        
        
