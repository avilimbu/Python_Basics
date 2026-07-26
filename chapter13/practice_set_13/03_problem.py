# Write a program to filter a numbers which are divisible by 5.

def divisible(n):
    if (n%5==0):
        return True
    return False

a = [25,67,99,50,5,6,498522]

print(list(filter(divisible,a)))