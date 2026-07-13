# If the names of two friends are same, what will happen to the program 6?

d = {}

name = input("Enter your friend name: ").strip()
lang = input("Enter the language your friend speaks: ").strip()
d.update({name:lang})
name = input("Enter your friend name: ").strip()
lang = input("Enter the language your friend speaks: ").strip()
d.update({name:lang})
name = input("Enter your friend name: ").strip()
lang = input("Enter the language your friend speaks: ").strip()
d.update({name:lang})
name = input("Enter your friend name: ").strip()
lang = input("Enter the language your friend speaks: ").strip()
d.update({name:lang})

print(d)

# If the two friends are same than the latest value added will overwrite early entry in the dictionary
# so key name should be different