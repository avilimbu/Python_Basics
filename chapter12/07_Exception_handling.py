try:
    a = int(input("Enter a number: "))
    print(a)
except ValueError:
    print("hey, enter the integer")
except Exception as e:
    print(e)

print("Done!")