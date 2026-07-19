class Animal:
    def __init__(self):
        print("All animals are very found of leaving")

    def eat(self,name):
        print(f"{name} can eats")

class Mammal(Animal):
    def __init__(self):
        print("It can give birth")

    def walk(self,name):
        print(f"{name} can walk")

class Dog(Mammal):
    def __init__(self):
        #super method helps to call the constructor of a prent class
        super().__init__()
        print("Dog are lovely animal")

    def bark(self):
        print("Dog barks")

d = Dog()
d.bark()
