def main():
    try:
        a = int(input("Enter a number: "))
        b = int(input("Enter a number: "))

        c = a / b

        print(f"The result of {a}/{b} = {c}")
        return

    except ZeroDivisionError:
        print(f"The number cannot be divided by zero as {a}/{b}")
        return

    except ValueError:
        print("Both values should be integers.")
        return

    finally:
        print("execution done")

main()

# using return means don't run the conde after return occurance but with finally,
#finally part runs no matter what bending the rule of return and function
