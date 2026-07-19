# Write a class `calculator` capable of finding square, cube and square root of a number.

class Calculator():
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"Square of a {self.n} = {self.n**2}")

    def cube(self):
        print(f"Cube of a {self.n} ={self.n**3} ")

    def squareRoot(self):
        print(f"Square root of {self.n}= {self.n**(1/2)} ")

n = int(input("Enter a number: "))
c = Calculator(n)
c.square()
c.cube()
c.squareRoot()
