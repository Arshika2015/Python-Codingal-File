def matchwords(words):
    count = 0
    list = []
    for word in words:
        if len(word)>1 and word[0]==word[-1]:
            count = count+1
            list.append(word)
    print("list of words which is having 1st and last charcter same is ",list)
    return count
python = matchwords(["abc","ice","hello","cfc","bcb"])
print("number of words having 1st and last character same ",python)


            








