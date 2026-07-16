'''f = open("file.txt")
f.read(text)
f.close()'''

# The same can be written using with statement
with open("file.txt") as f:
    print(f.read())

# we don't need to explicitely close the file 