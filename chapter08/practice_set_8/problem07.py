# Write a pyhton function to remove given word from a list and strip it at the same time.

def rem(l, word):
    n = []
    for item in l:
        if not(item ==word):
            n.append(item.strip(word))
    return n

l = ["harry", "Rohan", "Roshan", "an"]

print(rem(l,"an"))

