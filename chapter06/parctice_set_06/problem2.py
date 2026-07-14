#  Write a program to find out whether a student has passed or failed if it requires a total of 40% and 
# 33% is each subject too pass. Assume three subjects and take marks as an input from the user.

mark1 = int(input("Enter a mark: "))
mark2 = int(input("Enter a mark: "))
mark3 = int(input("Enter a mark: "))

avg = (mark1+mark2+mark3)/3
print("avg marks = ",avg)

if (mark1>=33 and mark2>=33 and mark3>=33 and avg>=40):
    print("He has passed the exam.")

else:
    print("He has failed the exam.")
    