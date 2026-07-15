# Write a program using function to find greatest of the three numbers
def greatest(a,b,c):
    if (a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c

great = greatest(8, 9, 45)
print(f"{great} is the greatest")