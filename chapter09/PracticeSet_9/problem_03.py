# Write a program to generate multiplication table from 2 to 20 and write it to the different files. 
# Place these file in a folder for a 13-year old.

def generateTables(n):
    table = ""
    for i in range(1,11):
        table+= f"{n}*{i} = {n*i}\n"
    with open (f"13-year_old/tables_{n}.txt", "w") as f:
        f.write(table)
    



for i in range(2,21):
    generateTables(i)