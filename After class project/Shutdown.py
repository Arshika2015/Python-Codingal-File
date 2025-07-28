counter = 1
password = input ("Enter Password:")
while password != "Test":
 counter = counter + 1
 password = input ("Incorrect, try again: ")
 counter = int (counter)
 if counter == 3:
  ("Enter Password:")