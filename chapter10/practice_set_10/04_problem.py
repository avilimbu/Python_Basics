# Add the static method in problem 2, to greet the user with hello.

# Write a class `calculator` capable of finding square, cube and square root of a number.

class Calculator():
    def __init__(self, n):
        self.n = n

    @staticmethod #we dont need self with static method
    def Greet():
        print("hello buddy")

    def square(self):
        print(f"Square of a {self.n} = {self.n**2}")

    def cube(self):
        print(f"Cube of a {self.n} ={self.n**3} ")

    def squareRoot(self):
        print(f"Square root of {self.n}= {self.n**(1/2)} ")

n = int(input("Enter a number: "))
c = Calculator(n)
c.Greet()
c.square()
c.cube()
c.squareRoot()
