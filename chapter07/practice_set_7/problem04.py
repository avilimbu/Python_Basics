# Write a program to find out whether a given number is prime or not.

n = int(input("Enter a number to find either it is prime number or not:" ))

for i in range(2,n):
    if ((n%2) ==0):
        print(f"{n} is not a prime number")
        break

else:
    print(f"{n} is a prime number")