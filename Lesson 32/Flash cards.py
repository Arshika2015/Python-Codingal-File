class Flashcard:
    def __init__(self,word,meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        return self.word+'('+self.meaning+')'
flash = []
print("welcome to the Flashcard application")
while True:
    word = input("enter the word you want to add to flashcard")
    meaning = input("enter the meaning of the word")
    flash.append(Flashcard(word,meaning))
    option = int(input("enter 0 if you want add another flashcard otherwise enter 1"))
    if option:
        break
print("my flashcard are")
for i in flash:
    print(">",i)

