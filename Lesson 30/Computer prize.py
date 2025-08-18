class computer:
    def __init__(self):
        self.__maxprize = 900
    def sell(self):
        print("selling price is ",self.__maxprize)
    def setmaxprize(self,prize):
        self.__maxprize = prize
technology = computer()
technology.sell()
technology.__maxprize = 57507
technology.sell()
technology.setmaxprize(2799)
technology.sell()
        