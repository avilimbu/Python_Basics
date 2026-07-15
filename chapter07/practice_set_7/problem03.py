# Find a multiplication table using while loop

n = int(input("Enter a number to find it's multiplication table: "))
i = 1
while (i<=10):
    print(f"{n}*{i}= {n*i}")
    i+=1