class parrot:
    species = "birds"
    def __init__(self,name,age):
        self.name = name
        self.age = age
nemo = parrot("nemo",2)
lily = parrot("lily",2)
print("nemo is a ",nemo.species)
print("lily is a ",lily.species)
print(nemo.name," is ",nemo.age," years old ")
print(lily.name," is ",lily.age," years old ")
