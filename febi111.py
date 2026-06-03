n=int(input('Enter a Number'))
a=0
b=1
print(a)
print(b)
while True:
    c=a+b
    print(c)

    if n==c:
        print('Febinoci')
        break
    if n<c:
        print('Not Febinoci')
        break

    a=b
    b=c
