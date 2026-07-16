#this add the written content at the end of the file for the number of times it runs

text = "Hey what's up"

f = open("file.txt", "a")
f.write(text)
f.close()