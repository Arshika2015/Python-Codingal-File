def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def divide(a,b):
    return a/b
print("please select any operation")
print("a.add")
print("b.subtract")
print("c.multiplication")
print("d.divide")
choice = input("plase enter ur choice a/b/c/d:")
num1 = int(input("please enter a num"))
num2 = int(input("please enter a num"))
if choice == "a":
    print(num1, "+",num2,"=",add(num1,num2))
elif choice == "b":
    print(num1,"-",num2,"=",subtract(num1,num2))
elif choice == "c":
    print(num1,"*",num2,"=",multiplication(num1,num2))
elif choice == "d":
    print(num1,"/",num2,"=",divide(num1,num2))
else:
    print("invalid input")

