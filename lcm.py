n1=int(input("Enter first number"))
n2=int(input("Enter second number"))
if n1<n2:
    small=n1
else :
    small=n2
hcf=1

if small%n1==0 and small%n2==0:
    hcf=small

else:
    for i in range(2,small+1):
        if n1%i==0 and n2%i==0:
            hcf=i

    print(hcf)
