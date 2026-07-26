# Write a program to input name, marks, and phone number of and format it using format function.
#  Like `The name of a student is shyam, his marks are 45, and phone number is 982245365.`

try:
    name = str(input("Enter your name: ")).strip().capitalize()
    marks = int(input("Enter you marks: "))
    phoneNo = int(input("Enter your phone number: "))

    s = "The name of a student is {0}, his marks are {1}, and phone number is {2}".format(name,marks,phoneNo)
    print(s)
except Exception as e:
    print(e)
