#Repeat program 4 for a list of such words to be censored.

words = ["Donkey", "bad", "stinks"]

with open ("05_file.txt", "r") as f:
    content = f.read()
for word in words:
    content = content.replace(word, "#"*len(word)) #updating content after each loop

with open ("05_file.txt", "w") as f:
    f.write(content)