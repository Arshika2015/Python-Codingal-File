try:
age = int(input("enter the age:"))
if age<18:
raise ValueError
else:
if age%2 - 0:
print("the age is even")
else:
print("the age is odd")
except ValueError:
print("invalid age")