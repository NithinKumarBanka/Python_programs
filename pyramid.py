rows=int(input("Enter a number"))
row_no=1
while row_no<=rows:
    print(" "*(rows-row_no)+"*"*(2*row_no-1))
    row_no+=1
print()
