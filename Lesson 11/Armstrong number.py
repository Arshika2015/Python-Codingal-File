num = int(input("enter a number"))
sum = 0
temp = num
while temp>0:
    digit = temp%10
    sum = sum+digit**3
    temp//=10
if num==sum:
    print("the number is a armstrong number")
else:
    print("the number is not a armstrong number")


