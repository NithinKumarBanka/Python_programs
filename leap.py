i=1500
while i<=2026:
    if(i%4==0 and i%100!=0) or (i%400==0):
        print(i)
    i=i+1      
