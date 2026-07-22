# In Qns 3. Write a method `saalryAfterIncrement` method with a `@property` decoretor with
#  a `setter` which changes the value of increment based on salary.


class Employee: 
    salary = 45000
    increment = 10

    @property
    def SalaryAfterIncrement(self):
        return self.salary + (self.salary*self.increment/100)
    
    @SalaryAfterIncrement.setter
    def SalaryAfterIncrement(self,new_salary):
        self.increment = ((new_salary/self.salary)-1)*100

        

e = Employee() 
print("Original salary=",e.salary)
print(f"Salary after increment of {e.increment}% = {e.SalaryAfterIncrement}")
e.SalaryAfterIncrement = 60000
print(f"New salary {e.SalaryAfterIncrement} is possible with increment {e.increment}")
