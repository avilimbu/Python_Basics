# Strore the multiplication table generated in problem 3 in a file named table.txt. 

try:
    n = int(input("Enter a number: "))
    table = [f"{i}*{n}={i*n}" for i in range(1,11)]
    final = "\n".join(table)
    with open("table.txt", "a") as f:
        f.write(f"Multiplication table of {n} \n")
        f.write(final)
        f.write("\n \n")

except Exception as e:
    print(e)
