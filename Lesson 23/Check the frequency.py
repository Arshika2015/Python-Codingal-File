testdict = {"codingal":2,"is":2,"best":2,"for":2,"coding":1}
print("the orignal dicitionary is",testdict)
count = 0
v = 2
for key in testdict:
    if testdict[key]== v:
        count = count+1
print(count)
            