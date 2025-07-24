rows = int(input("enter the number of rows"))
for i in range(1,rows+1):#outer loops for rows
    for j in range(rows-1):#inner loop for spaces
        print(" ",end="")
    for k in range(i):#inner loop for stars
        print("*",end="")
print()#newline after each row


    