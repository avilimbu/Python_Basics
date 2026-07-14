# Write a program to calculate the grade of a student from his marks from the following scheme:
# 90-100 = A+
# 80-90 = A 
# 70-80 = B+
# 60-70 = B
# 50-60 = c
# <50=F

mark = int(input("Enter your mark: "))

if (mark>90 and mark<=100):
    print(f"{mark} is a A+ grade")

elif(mark>80 and mark<=90):
    print(f"{mark} is A grade")

elif(mark>70 and mark<=80):
    print(f"{mark} is B+ grade")

elif(mark>60 and mark<=50):
    print(f"{mark} is B grade")

elif(mark>=50 and mark<=60):
    print(f"{mark} is C grade")

elif(mark>0 and mark<50):
    print("Sorry you are failed")

else:
    print("Invalid marks, Please enter a valid marks")