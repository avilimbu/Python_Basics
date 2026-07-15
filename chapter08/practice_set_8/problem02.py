# Write a program using function to convert  `Fahrenheit`to celcius.

def f_t0_c(f):
    return 5*(f-32)/9

f = float(input("Enter the Temperature in F: "))
c= f_t0_c(f)
print(f"{f} Fahrenheit = {round(c,2)} Celcius")


