# Create a class `Pets` form `Animal` and further create a class `Dog` from `Pets`. 
# Add a method `bark` to class `Dog`.

class Animal:
    
    def eat(self,name):
        print(f"{name} can eats")

class Pets(Animal):

    def loved(self,name):
        print(f"{name} is loved by many people")

class Dog(Pets):

    @staticmethod
    def bark():
        print("Dog barks")

d = Dog()
d.eat("Dog")
d.loved("Dog")
d.bark()
