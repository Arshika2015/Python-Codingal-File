import random
import time
number = random.randint(1,100)
def intro():
    print("may i ask for your name")
    name = input()
    print(name+",we are going to play a game,i am thinking of a number between 1 to 100")
    if number%2==0:
        x = "even"
    else:
        x = "odd"
    print("this is the number ",number)
    time.sleep(.5)
    print("go ahead and guess!")
def pick():
        guesstaken = 0
        while guesstaken<6:
            time.sleep(.25)
            enter = input("enter your guess:")
            try:
                guess = int(enter)
                if guess<=100 and guess>=1:
                    guesstaken = guesstaken+1
                    if guesstaken<6:
                        if guess<number:
                            print("the number you have guessed is too low")
                        if guess>number:
                            print("the guess of the number you have guessed is too high")
                        if guess!=number:
                            time.sleep(.5)
                            print("try again")
                        if guess==number:
                            break
                if guess>100 or guess<1:
                 print("silly goose!the number is not in the range")
                 time.sleep(.25)
                 print("please enter a number between 1 to 100")
            except:
                print("i dont think that "+enter+"is a number.sorry")
        if guess==number:
            guesstaken = str("guess taken")
            print("good job","u guess my number in ",guesstaken)
        if guess!= number:
            print("nope the number i was thinking of was ",str(number))
playagain = "yes"
while playagain == "yes" or playagain == "y" or playagain == "Yes":
    intro()
    pick()
    print("do you want to play again?")
    playagain=input()
    print("thank you")



            

            
                        

                    





