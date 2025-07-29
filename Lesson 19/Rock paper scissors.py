import random
options = ["rock","paper","scissor"]
userchoice = input("choose rock,paper or scissor")
computerchoice = random.choice(options)
print("computer choice is",computerchoice)
print("user choice is",userchoice)
if userchoice ==computerchoice:
    print("it is a tie")
elif userchoice =="rock" and computerchoice=='scissor':
    print("you win")
elif userchoice== "scissor" and computerchoice=="paper":
    print("you win")
elif userchoice=="paper" and computerchoice=="rock":
    print("you win")
else:
    print("you lose")
