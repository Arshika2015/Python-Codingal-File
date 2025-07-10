medicalcause = (input("please enter y if u have medical cause else n"))
attendance = int(input("enter their attendance"))
if medicalcause=="y":
     print("u are allowed")
else:
     if attendance>=75:
          print("u are allowed")
     else:
          print("u are not allowed")
          
          