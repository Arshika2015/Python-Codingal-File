try: 
 num1,num2 = eval(input("enter 2 numbers seperated by comma:"))
 result = num1/num2
 print("the result is",result)
except ZeroDivisionError:
 print("division by zero is error")
except SyntaxError:
 print("the comma is missing,enter comma by putting 2 numbers ")
except:
 print("invalid input")
else:
 print("no exception")
finally:
 print("goodbye thank you")
