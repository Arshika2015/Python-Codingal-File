class A:
    def __init__(self,a):
        self.a = a
    def __lt__(self,other):
        if self.a<other.a:
            return "object1 is less than object2"
        else:
            return "object1 is not less than object2"
    def __eq__(self,other):
        if self.a==other.a:
            return "both are equal"
        else:
            return "both are not equal"
object1 = A(270)
object2 = A(450)
print("the two values are",object1.a,object2.a)
print(object1<object2)
object3 = A(330)
object4 = A(330)
print("the two values are",object3.a,object4.a)
print(object3==object4)

        




