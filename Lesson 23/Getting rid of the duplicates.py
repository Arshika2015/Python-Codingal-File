studendata = {
    "id1":{
        "name":"sarah",
        "class":"v",
        "subject":["english,maths,science"]
    },
        "id2":{
        "name":"david",
        "class":"vi",
        "subject":["english,maths,science"]
    },
        "id3":{
        "name":"sarah",
        "class":"v",
        "subject":["english,maths,science"]
    },
    "id4":{
        "name":"zoey",
        "class":"vii",
        "subject":["english,maths,science"]
    }
}
result = {}
for key,value in  studendata.items():
    if value not in result.values():
        result[key]= value
print(result)



