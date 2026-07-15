#  Write a program to greet all person's names stored in list `l` and which starts with `S`.

# l = ["Ram", "Shyam", "Suvam", "hari"]

l = ["Ram", "Shyam", "Suvam", "haSi"]

for name in l:
    if name.startswith("S"):
        print("Hello",name)