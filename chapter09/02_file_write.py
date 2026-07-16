#write mode alows us to write in a file but it overwrites the content present in the file
text = "Hey isn't learning awesome"

f = open("file.txt", "w")
f.write(text)
f.close()