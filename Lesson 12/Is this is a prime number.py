lower = int(input("enter the lower range"))
upper = int(input("enter the upper range"))
for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)