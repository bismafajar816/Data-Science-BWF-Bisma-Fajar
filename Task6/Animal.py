from PracticeClass import Enemy  # Import the Enemy class from PracticeClass.py
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Some generic animal sound")

    def display_info(self):
        print(f"Name: {self.name}, Species: {self.species}")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed

    def make_sound(self):
        super().make_sound()  # Call the parent class method (optional)
        #Override the parent class method
        print("Bark!")

    def display_info(self):
        super().display_info()  # Call the parent class method
        print(f"Breed: {self.breed}")

# Usage:
generic_animal = Animal("Generic", "Unknown")
dog = Dog("Buddy", "Golden Retriever")

generic_animal.make_sound()  # Output: Some generic animal sound
dog.make_sound()             # Output: Some generic animal sound (optional) and Bark!

generic_animal.display_info()  # Output: Name: Generic, Species: Unknown
dog.display_info()             # Output: Name: Buddy, Species: Dog, Breed: Golden Retriever
