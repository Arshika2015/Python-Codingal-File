height = float (input("enter ur height in metres"))
weight = float(input("eter ur weight in kg"))

BMI = weight / (height * height)
print("your BMI is ",BMI)


if BMI <= 18.4:
    print("you are underweight")
elif BMI <= 24.9:
    print("you are healthy")
elif BMI <= 29.9:
    print("you are overweight ")
elif BMI <= 34.9:
    print("you are severely overweight")
elif BMI <= 39.9:
    print(" u are obese")
else:
    print("u are severely obese")