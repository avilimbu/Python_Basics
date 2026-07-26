# Write a list comprehension to print a list which contains the multiplication of a user entered number.

try:
    n = int(input("Enter a number: "))
    table = [f"{i}*{n}={i*n}" for i in range(1,11)]
    print(table)

except Exception as e:
    print(e)

