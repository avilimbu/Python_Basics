# Write a program to find out the line number where python is present in qns 6.

with open("log.txt") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if  ("python" in line):
        print(f"python is present in line no: {lineno}")
        break
else:
    print("python is not present")
