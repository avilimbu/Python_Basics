class Employee:
    company = "QNB"
    def show(self):
        print(f"You are currently working in {self.company}")

class Language:
    language = "Pyhton"
    def printLanguage(self):
        print(f"You are currently working this means you are excellent in {self.language}")

class programmer(Employee, Language):
    salary = 1205553
    def showAll(self):
        print(f"You work at {self.company} that means you should be good at {self.language}")
        print("your salary is",self.salary)

p = programmer()
p.showAll()
p.printLanguage()