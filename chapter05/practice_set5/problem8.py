# If language of two friends are same, what will happen to the program 6 ?

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

#Nothing will happen as,
# values can be same | In dictionary identifier is key | Hence key should be unique