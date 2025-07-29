import random
playing = True
number = str(random.randint(1,30))
while playing:
    guess = input("guess any number")
    if number==guess:
        print("you win the game")
        print("the number was ",number)
        break 
    else:
        print("your guess is not correct,try again")