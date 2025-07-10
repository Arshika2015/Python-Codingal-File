print("select your ride:")
print("1.Bike")
print("2.car")

choice = int(input("enter your choice:"))

if choice == 1:
    print("what type of bike:")
    print("1.scooty")
    print("2.scooter")
    choice2 = int(input("enter your choice:"))
    if choice2 == 1:
        print("you have selected scooty")
    else:
        print("you have selected scooter")
elif choice == 2:
    print("what type of car")
    print("1. bmw")
    print("2. nano")
    choice3 = int(input("enter ur choice"))
    if choice3 == 1:
        print("u have selected bmw ")
    else:
        print("2. nano")
        print("u have selected nano")
else:
    print("wrong choice")
