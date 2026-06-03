n=int(input('Number:'))
a=0
b=1
print(a,b,end=' ')
i=1
while i<=n-2:
    c=a+b
    print(c,end=' ')
    i=i+1

    a=b
    b=c
