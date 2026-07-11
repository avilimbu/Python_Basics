t = {1,2,6,55,3,3,2,55}
print(t, type(t))  


#add()
t.add(360)
print(t)


#remove
t.remove(1)
print(t)

#union , intersection, subset, difference, superset
s1 ={1,2,3,4,5}
s2 = {4,5,6,7,8}
s3 ={1,2,3}
s4 ={4,5,6}
print(f"Union of {s1} and {s2} = {s1.union(s2)}")
print(f"Intersection of {s1} and {s2} = {s1.intersection(s2)}")
print(f"Difference of {s1} and {s2} = {s1.difference(s2)}")
print(f"Is {s3} subset of {s1} = {s3.issubset(s1)}")
print(f"Is {s2} superset of {s2} = {s2.issuperset(s4)}")

s1.clear()
print(s1)

#pop | Removes the random data
s2.pop()
print(s2)
