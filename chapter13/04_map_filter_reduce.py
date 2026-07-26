l =[1,2,3,4,5]
square = lambda x: x**2

# map example
sqlist = map(square, l)
print(f"square of all numbers {l} = {list(sqlist)}")

# filter example
even = filter(lambda x: x%2==0, l)
print(f"even number of list from {l} = {list(even)}")

#reduce
from functools import reduce
def sum(a,b):
    return a+b

print(f"Sum of all numbers {l} = {reduce(sum,l)}")