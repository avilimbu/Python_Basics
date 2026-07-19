class Animal:
    def eat(self,name):
        print(f"{name} can eats")

class Mammal(Animal):
    def walk(self,name):
        print(f"{name} can walk")

class Dog(Mammal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.eat("Dog")
d.walk("Dog")
d.bark()
