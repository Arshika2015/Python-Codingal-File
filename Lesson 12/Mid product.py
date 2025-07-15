num = int(input("enter a number"))
t = num 
numlen = 0 
while t>0:
    numlen = numlen+1
    t= t // 10
if numlen>=4:
    numlen = int(numlen/2)
    chk = 0
    while num>0:
        rem = num %10
        if chk == numlen:
            midone = rem
        elif chk==(numlen-1):
            midtwo = rem
        num = num // 10
        chk= chk+1
    product = midone*midtwo
    print("the product is",product)
else:
    print("its not 4 or more than 4 digit number")
    

