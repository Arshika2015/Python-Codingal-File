print("enter marks optained in five subjects")
mark1 = int(input("please enter ur first mark"))
mark2 = int(input("please enter ur second mark"))
mark3 = int(input("please enter ur third mark"))
mark4 = int(input("please enter ur fourth mark"))
mark5 = int(input("please enter ur fifth mark"))
total = mark1+mark2+mark3+mark4+mark5
average = total/5
if average>= 91 and average<= 100:
    print("your grade is a1")
elif average>= 81 and average< 91:
    print("your grade is a2")
elif average>= 71 and average< 81:
    print("yopur grade is b1")
elif average>= 61 and average< 71:
    print("your grade is b2")
elif average>= 51 and average< 61:
    print("your grade is c1")
elif average>= 41 and average< 51:
    print("your grade is c2")
elif average>= 33 and average< 41:
    print("your grade is d")
elif average>= 21 and average< 33:
    print("your grade is e1")
elif average>= 0 and average< 21:
    print("your grade is e2")
else:
    print("invalid input")
