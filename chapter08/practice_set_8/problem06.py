# Write a python functions which converts inches to cm.

def inch_to_cm(inch):
    return inch * 2.54

inch = float(input("Enter the value in inch: "))
cm = inch_to_cm(inch)

print(f"{inch} inch = {round(cm,2)} cm")