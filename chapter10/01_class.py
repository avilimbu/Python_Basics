class Employee:
    language = "Python"
    salary = 12000000
#salary and language are class attributes
#avhi is a object here
avhi = Employee()

#giving name 
avhi.name = "Avhi"
print(avhi.name,"salary is",avhi.salary)

#making another object from the class
jerry = Employee()
jerry.name = "Jerry"
jerry.company = "QBC"

#here name and company is instance attributes and language and salary are  class attributes
print(f"{jerry.name} works in {jerry.company} with salary {jerry.salary}")

