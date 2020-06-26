import math

def fib(n):
    l = 1
    r = 2
    for i in range(3,n):
        f = l + r
        print(f)
        l = r
        r = f
    return(f)        
            
def lee(terms):
    acc = 0
    num = 4
    den = 1

    for aterm in range(terms):
        nextterm = num/den * (-1)**aterm

        acc = acc + nextterm

        den = den + 2

    return acc

def ark(numsides):
    inneranB = 360.0/numsides
    halfanA = inneranB/2
    onehalfsideS = math.sin(math.radians(halfanA))
    sideS = onehalfsideS * 2
    polygonCirc = numsides * sideS
    pi = polygonCirc/2

    return pi

def wallis(pairs):
    acc = 1
    nom = 2
    for apair in range(pairs):
        leftterm = nom/(nom - 1)
        rightterm = nom/(nom + 1)
        acc = acc * leftterm * rightterm
        nom = nom + 2
    pi = acc * 2
    return pi
        
