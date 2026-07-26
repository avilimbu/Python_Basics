try:
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))

    c = a / b

    print(f"The result of {a}/{b} = {c}")

except ZeroDivisionError:
    print(f"The number cannot be divided by zero as {a}/{b}")

except ValueError:
    print("Both values should be integers.")