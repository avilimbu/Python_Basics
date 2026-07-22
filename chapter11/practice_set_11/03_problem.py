# Create a class `Employee` and add `salary` and `increment` property to it.

class Employee: 
    salary = 45000
    increment = 10

    def incrementSalary(self):
        return self.salary + (self.salary*self.increment/100)

e = Employee()
print("Original salary=",e.salary)
print(f"Salary after increment of {e.increment}% = {e.incrementSalary()}")
