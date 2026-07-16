# it allows us to read the line in the file
f = open("file.txt")

# readlines() || allows to read all the line
'''lines = f.readlines()

print(lines, type(lines))'''

#readline()

'''line1 = f.readline()
print(line1, type(line1))

line2 = f.readline()
print(line2, type(line2))

line3 = f.readline()
print(line3, type(line3))'''

#another way for | readline | allows to read every line
line = f.readline()
while(line!=""):
    print(line)
    line = f.readline()

f.close()