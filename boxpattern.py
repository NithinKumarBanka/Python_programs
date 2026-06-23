rows=int(input("Enter a number"))
row_no=1
while row_no<=rows:
    if row_no==1:
        print("*"*rows)

    elif row_no==rows:
        print("*"*rows)
        
    else:
        print("*" + " "*(rows-2) + "*")

    row_no+=1
    
