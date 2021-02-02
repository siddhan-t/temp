def isprime(n):
    if n==2:
        return 1

    for i in range(2,n):
        if n%i==0:
            return 0
    return 1
            
def primegenerator(num,v):
    l=[]
    for i in range(2,num):
        if isprime(i)==1:
            l.append(i)
    if v==0:
        return l[::2]
    else:
        return l[1::2]
    
print(primegenerator(21,0))

        