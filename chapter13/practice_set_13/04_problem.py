# Write a program to find a miximum of numbers in a list using reduce function. 
from functools import reduce

def maximum(a,b):
    if (a>b):
        return a
    else:
        return b

a = [25,25,67,99,50,5,6,5,498522]

print(reduce(maximum,a))