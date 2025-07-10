character = (input("enter ur character"))
if len(character)>1:
    print("please enter only 1 character")
elif character.isalpha():
    print("it is a alphabet")
else:
    print("it is not a alphabet")
