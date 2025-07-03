actualcost = int(input("please enter the actual cost"))
sellingamount = int(input("please enter the selling amount"))
if sellingamount >actualcost:
    profit = sellingamount-actualcost
    print("the profit is ",profit)
else:
    print("no profit")
    