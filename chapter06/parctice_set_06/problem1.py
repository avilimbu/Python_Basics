# Write the program to find the greatest of the four number entered by the user.

a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
c = int(input("Enter the number: "))
d = int(input("Enter the number: "))

if a>b and a>c and a>d:
    print(f"a = {a} is greater in {a},{b},{c},{d}")

elif b>a and b>c and b>d:
    print(f"b = {b} is greater in {a},{b},{c},{d}")

elif c>a and c>b and c>d:
    print(f"c = {c} is greater in {a},{b},{c},{d}")

else:
    print(f"d = {d} is greater in {a},{b},{c},{d}")