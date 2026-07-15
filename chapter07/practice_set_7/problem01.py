# Write a program to print multiplication of a given number using for loop.

n = int(input("Enter a number to find it's multiplication table:  "))

for i in range(1,11):
    print(f"{n}*{i}= {n*i}")