class Dog:
    species = "Canis familiaris"
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def display_details(self):
        """Displays the details of a dog."""
        print(f"Name: {self.name}")
        print(f"Breed: {self.breed}")
        print(f"Species: {Dog.species}\n") 
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "German Shepherd")
print("Details of Dog 1:")
dog1.display_details()
print("Details of Dog 2:")
dog2.display_details()
print("arshika will get a dog on yashs birthday ")