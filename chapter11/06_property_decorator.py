class Student:

    def __init__(self, name, age):
        self.name = name
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            print("Age cannot be negative")


s = Student("John", 20)

print(s.age)

s.age = 25

print(s.age)

s.age = -5