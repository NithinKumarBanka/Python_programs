str=input("Enter a string: ")
def palindrome(str):
    s=0
    e=len(str)-1

    while s<e:
        if str[s]!=str[e]:
         return False
        s=s+1
        e=e-1
    else:
       
        return True
        
res=palindrome(str)
print(res)
