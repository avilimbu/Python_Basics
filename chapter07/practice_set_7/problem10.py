# Write a progrma to print the multiplication table of n using loop in reverse order.

n = int(input("Enter the number to find it's multipliccation table in reverse"))

for i in range (10,0,-1):
    print(f"{n}*{i}= {n*i}")