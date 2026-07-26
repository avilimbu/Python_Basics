# write a program to display a/b where a and b are integers. 
# If b=0 dispay infinite by handling the ZeroDivisionError.

try:
    a = int(input("Enter a number to be divided: "))
    b = int(input("Enter a number that divides: "))
    print(f"{a}/{b} = {a/b}")
except ZeroDivisionError:
    print("Infinite")
except Exception as e:
    print(e)