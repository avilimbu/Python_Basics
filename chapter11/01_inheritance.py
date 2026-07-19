class Employee:
    company = "QBC"
    def show(self):
        print("You are great")

class programmer(Employee):
    company = "RBD"
    def language(self):
        print("you are brillient at Pyhton")

a = Employee()
b = programmer()
b.show()
b.language()