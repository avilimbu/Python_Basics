class Employee:
    language = "Python" #class attribute
    salary = 12000000


avhi = Employee()

avhi.language = "JavaScript" #object attribute

#here instance attribute takes preference when attriutes are same in both instance and class.
print(avhi.language,"salary is",avhi.salary)