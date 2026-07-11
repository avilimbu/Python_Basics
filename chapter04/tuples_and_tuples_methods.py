#creating a tuple

a = (1,2,5,6)
print(type(a))

# tuples with only one element
a2 =(1,) #if a =(1) than it is considered int
a1=() # empty tuple


#tuples methods

#count
print(f"Occurance of 6 in {a} = {a.count(6)}")

#indexing
print(f"Index of 6 = {a.index(6)}")