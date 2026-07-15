# Write a python program to print first n lines of following patterns:

# ***
# **
# * for n = 3

def pattern(n):
    if n==0:
        return
    print("*" * n)
    return pattern(n-1)

n = int(input("Enter the number: "))
pattern(n)