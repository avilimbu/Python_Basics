# Strore the multiplication table generated in problem 3 in a file named table.txt. 

try:
    n = int(input("Enter a number: "))
    table = [f"{i}*{n}={i*n}" for i in range(1,11)]
    with open("table.txt", "a") as f:
        f.write("_" * 20 + "\n")
        f.write(f"Table of {n}\n")
        f.write(str(table) + "\n")

except Exception as e:
    print(e)
