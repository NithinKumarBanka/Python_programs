y=[100,120,6,10,15,14,13,10]
x=set(y)
first=float('-inf')
second=float('-inf')

for i in x:
    if i>first:
        #first=i
        second=first
        first=i
    if i>second and i<first:
        second =i

print(second)
print(first)
print(x)
