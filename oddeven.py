rows=int(input("Enter a number"))
row_no=1
while row_no<=rows:
    if row_no%2==0:
        print("0"*row_no)
    else:
        print("1"*row_no)

    
    row_no+=1
    
