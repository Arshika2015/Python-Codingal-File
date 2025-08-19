from abc import ABC,abstractmethod
class abcclass (ABC):
    def print(self,x):
        print("passed value is ",x)
    @abstractmethod
    def task(self):
        print("we are inside abcclass")
class testclass(abcclass):
    def task(self):
        print("we are inside task method")
a = testclass()
a.task()
a.print(100)




