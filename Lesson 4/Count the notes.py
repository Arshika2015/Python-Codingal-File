amount = int(input("enter the amount"))
note1 = amount//100
note2 = (amount%100)//50
note3 = ((amount%100)%50)//10
print("the no of hundred rupee note are ",note1)
print("the no of fifty rupee note are ",note2)
print("the no of ten rupee note are ",note3)