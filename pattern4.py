rows=int(input("Enter a number"))
row_no=1
while row_no<=rows:
    col=1
    while col<=row_no:
        print(row_no,end=" ")
        col+=1
    
    print()

    row_no+=1
