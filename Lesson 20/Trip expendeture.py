def hotelcost(days):
    return 140*days
def planecost(city):
    if "delhi" ==city:
        return 10000
    elif "banglore"==city:
        return 5383
    elif "japan"==city:
        return 8497
    elif "haridwar"==city:
        return 9999
def rentalcost(days):
    if days>=7:
        return 40*days-50
    elif days>=3:
        return 40*days-20
    else:
        return 40*days
def totalcost(city,days,spendingmoney):
    return rentalcost(days)+hotelcost(days)+planecost(city)+spendingmoney
print("cost of car rental",rentalcost(5))
print("cost of plane ride",planecost("japan"))
print("cost of hotel",hotelcost(15))
print("total cost",totalcost("japan",20,1000000000000))
