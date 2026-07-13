# Create an empty dictionary. Allow 4 friends to enter their favourite language as values 
# and use key as their names. Assume the names are unique.

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