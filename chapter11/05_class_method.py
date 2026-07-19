class student:
    rollno = 1

    #class method tells to run a class attribute in place of instance attribute in a method
    @classmethod
    def show(cls):
        print(f"Rollno of a student is {cls.rollno}")

s = student()
s.rollno = 23
s.show()

