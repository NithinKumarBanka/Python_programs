x=[1,2,3,4,5,6,7,8,9,10]
tar=int(input("Enter anumber"))
s=0
e=len(x)+1
#mid=(s+e)//2
for i in range(len(x)):
    mid=(s+e)//2
    if s>e:
        print("not Found")
        break
    elif mid==tar:
        print("Found")
        break
    elif tar>mid:
        s=mid+1
    else:
        e=mid-1
        
    
    
