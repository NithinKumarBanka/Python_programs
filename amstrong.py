def digitcount(num):
    count=0
    while num!=0:
        num=num//10
        count+=1
    return count
def digits(num,d):
    s=0
    while num!=0:
        digit=num%10
        out=digit**d
        s=s+out
        num=num//10
    return s
n=153
res=digitcount(n)
print(res)
output=digits(n,res)
print(output)
if n==output:
    print("Amstrong Number")

else :
    print("Not Amstrong")
    
