character = input("please enter a character")
if len(character)>1:
    print("please enter exactly one character")
else:
    asciivalue = ord(character)
    print("the ascii value is",asciivalue)
