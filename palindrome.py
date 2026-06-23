def ispalindrome(str):
    if str == str[::-1]:
        return True
    else:
        return False
s=input('Enter a String')
res=ispalindrome(s)
print(res)
