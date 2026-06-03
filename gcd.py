n1=int(input('Enter n1: '))
n2=int(input('Enter n2: '))

if n1<n2:
    small=n1
else:
    small=n2

i=small
while i>=2:
    if n1%i==0 and n2%i==0:
        print(i)
        break
    i=i-1
else:
    print('No gcd')
