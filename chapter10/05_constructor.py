class Employee:
    language= "JS"
    salary = 120000

    # dunder method which is called automatically when the object is created
    def __init__(self,name,salry, language): 
        self.name = name
        self.salary = salry
        self.language = language
        print("I am creating an object")

    def getInfo(self):
        print(f"Language is {self.language} and salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning Employee")

avhi = Employee("Avhishek", 1500000, "Python")
print(avhi.name, avhi.salary,avhi.language)



