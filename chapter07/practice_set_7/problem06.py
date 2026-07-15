# Write a program to calculate the factorial of a given number using for loop.

n = int(input("Enter the number to find it's factorial: "))
fact = n
for i in range(1,n):
    fact *=i
    i+=1

print(f"Factorial of {n} = {fact}")