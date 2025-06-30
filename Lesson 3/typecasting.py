#integer -> all positive and negative numbers
#float => all decimal values
#boolean -> only two values that is True and False
#string -> all the letters, words, characters, or sentence


name = "Arshika"
age = 10
is_student= True
weight = 40.0

print("name:",name)
print("the data type of name is:",type(name))

print("age:",age)
print("the data type of age is:",type(age))

print("is_student:",is_student)
print("the data type of is_student is:",type(is_student))

print("weight:",weight)
print("the data type of weight is:",type(weight))


print("after typecasting \n")

age = str(age)
print("data type of age is ",type(age))
weight = int(weight)
print("data type of weight is ",type(weight))
print(weight)
