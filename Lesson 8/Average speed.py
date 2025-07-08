speed1 = int(input("please enter the speed of 1 cyclist"))
speed2 = int(input("please enter the speed of 2 cyclist"))
speed3 = int(input("please enter the speed of 3 cyclist"))
average = speed1+speed2+speed3/3
print("the average of all the speeds is ",average)
if speed1<average:
    print("1 cyclist is slower than average")
if speed2<average:
    print("2 cyclist is slower than average")
if speed3<average:
    print("3 cyclist is slower than average")