# Write a program to mind a log file and find out whether it contains 'python'.

with open ("log.txt") as f:
    content= f.read()

if ("python" in content):
    print("python is present in log file")

else:
    print("Python is not present in log file")

