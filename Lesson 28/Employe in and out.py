class employee:
    def __init__(self):
        print("employee created")
    def __del__(self):
        print("destructor called")
def createobj():
    print("making object()function")
    obj = employee()
    print("function ended")
    return obj
print("calling and create object function")
obj = createobj()
print("program end")