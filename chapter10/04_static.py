class Employee:
    language= "Python"
    salary = 120000

    def getInfo(self):
        print(f"Language is {self.language} and salary is {self.salary}")

    #when a static method is used than there is no need to pass self parameter
    @staticmethod
    def greet():
        print("Good Morning Employee")

avhi = Employee()
avhi.getInfo()



