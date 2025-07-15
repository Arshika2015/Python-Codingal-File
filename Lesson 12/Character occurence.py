string = input("enter the word")
character = input("enter a character which is from ur choice and can be repeated")
i = 0
count = 0
while i<len(string):
    if string[i] == character:
        count = count+1
    i = i+1
print("the number of times it has to be repeated is",count)

