def isprime(n):
    for i in range(2,(n//2)+1):
        if n%i==0:
            return False
    else:
        return True

def rangeofprime(s,e):
    output=[]
    for num in range(s,e+1):
        if isprime(num)==True:
            output.append(num)
            

    return output
res=rangeofprime(2,100)
print(res)
