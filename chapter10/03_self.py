class Employee:
    language= "Python"
    salary = 120000

    def getInfo(self):
        print(f"Language is {self.language} and salary is {self.salary}")

    def greet(self):
        print("Good Morning Employee")

avhi = Employee()
avhi.getInfo()



