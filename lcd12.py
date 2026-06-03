n1=int(input('Enter number:'))
n2=int(input('Enter number:'))
if n1>n2:
    small=n2
else:
    small=n1

d=1
while d<=small:
    if n1%d==0 and n2%d==0:
        print(d)
    d=d+1
    


