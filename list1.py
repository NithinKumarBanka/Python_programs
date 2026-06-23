n=int(input())
x=[]
for i in range(n):
   x.append(int(input())) 
print(x)
x.sort()
print(x)
x.pop()
print(x)
x.remove(x[1])
print(x)
