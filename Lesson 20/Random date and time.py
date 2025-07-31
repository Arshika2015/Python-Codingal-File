import random
import time
def getrandomdate(startdate,enddate):
    print(" printing random date between",startdate,"and",enddate)
    randomgenerator = random.random()
    date = "%d/%m/%Y"
    starttime = time.mktime(time.strptime(startdate,date))
    endtime = time.mktime(time.strptime(enddate,date))
    randomtime = starttime+randomgenerator*(endtime-starttime)
    randomdate = time.strftime(date,time.localtime(randomtime))
    return randomdate
print("the randomdate is",getrandomdate("1/1/2016","12/12/2018"))

