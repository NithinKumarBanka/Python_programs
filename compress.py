s='aaabbcaa'

def compresstr(st):
    s=e=0
    count=0
    output=''
    while e<len(st):
     if st[s]==st[e]:
        count+=1
        e+=1

     else:
        output=output+st[s]+str(count)
        count=0
        s=e
    else:
     output=output+st[s]+str(count)
    return output
res=compresstr(s)
print(res)
