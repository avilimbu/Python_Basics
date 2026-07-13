#  What will be the length of a following set:


# s = set()
# s.add(20)
# s.add(20.0)
# s.add("20")


s = set()
s.add(20)
s.add(20.0)
s.add("20")

print(s)
print("lenght of s = ",len(s)) # 2 || because 1 == 1.00 gives True as they are numerically equal in python

