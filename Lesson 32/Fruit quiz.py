import random
class Fruitquiz:
    def __init__(self):
        self.fruits = {"apple":"red",
                       "watermelon":"green",
                       "bannana":"yellow",
                       "mango":"light yellow"}
    def quiz(self):
        while True:
            fruit,colour=random.choice(list(self.fruits.items()))
            print("what is the colour of ",fruit)
            answer = input()
            if answer.lower()== colour:
                print("correct answer")
            else:
                print("wrong answer")
            option = int(input("enter 0 if u wanna play again otherwise enter 1"))
            if option:
             break
print("welcome to fruitquiz")
object1 = Fruitquiz()
object1.quiz()



            

    
