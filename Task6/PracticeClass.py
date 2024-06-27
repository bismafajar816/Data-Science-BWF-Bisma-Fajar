class Enemy:
    def __init__(self, name="Enemy", age=10):
        self.name = name       # Default values
        self.age = age

    @classmethod
    def create_enemy(cls, name, age):  # cls is a reference to the class
        return cls(name, age) # Returns a new instance of the class

    def display(self):
        print("Name: ", self.name)
        print("Age: ", self.age)

    def attack(self):
        print("Attack")

enemy = Enemy()  # Uses default values
enemy1 = Enemy.create_enemy("Enemy1", 20)  # Uses provided values

enemy.display()  # Output: Name: Enemy, Age: 10
enemy1.display()  # Output: Name: Enemy1, Age: 20
enemy.attack()  # Output: Attack


#Inheritance without attributes
class Parent:
    def __init__(self):
        print("Parent Constructor")

    def parentMethod(self):
        print("Parent Method")
class Child(Parent):
    def __init__(self):
        print("Child Constructor")

    def childMethod(self):
        print("Child Method")
child = Child()  # Output: Child Constructor

#Inheritance with attributes
class Parent:
    def __init__(self, name):
        self.name = name
        print("Parent Constructor")
    def parentMethod(self):
        print("Parent Method")
class Child(Parent):
    def __init__(self, name, age):
        self.age = age
        Parent.__init__(self, name)
        print("Child Constructor")
    def childMethod(self):
        print("Child Method")
        
child = Child("Child", 10)  # Output: Parent Constructor, Child Constructor