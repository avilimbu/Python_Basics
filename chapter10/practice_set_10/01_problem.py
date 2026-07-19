# Create a class `programmer` for storing the information of a few programmer working at microsoft.

class Programmer:
    company = "Microsoft"

    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin
        print(name, salary, pin)

p1 = Programmer("avhi", 120000, 3556)
p2 = Programmer("grace", 25416, 459)