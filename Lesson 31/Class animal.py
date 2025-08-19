from abc import ABC
class animal(ABC):
    def move(self):
        pass
class human(animal):
    def move(self):
        print("i can walk and run")
class snake(animal):
    def move(self):
        print("i can crawl")
class dog(animal):
    def move(self):
        print("it barks")
class lion(animal):
    def move(self):
        print("it roars")
r = human()
r.move()
a = snake()
a.move()
d = dog()
d.move()
h = lion()
h.move()

