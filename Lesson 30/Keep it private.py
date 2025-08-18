class myclass:
    __privatevar = 27
    def __privatemethod(self):
        print("i am inside the class ",myclass)
    def hello(self):
        print("privatemethod",myclass.__privatevar)
object = myclass()
object.hello()
object.__privatemethod()



    
