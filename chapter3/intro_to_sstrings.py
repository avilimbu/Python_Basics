name = "radhashyam"
sentence = "wow, iam liking reading"

#slicing
short_name = name[0:5] #starts for 0 index all the way to 5 excluding 5

print(short_name)

print(name[:6]) # is same as name[0:6]

# slicing with skip value
print(name[0:9:2])

#len() function
print(len(name))

#endswith() 
print(name.endswith("am"))

#starts with
print(name.startswith("ras"))

#capitalize()
print(name.capitalize())

#upper()
print(name.upper())

#title()
print(sentence.title())

#find(word)
print(sentence.find("like")) #7

#replace(old_word, new_word)
print(sentence.replace("iam", "everyone"))

#Escape sequence character 
fav = "my favourite\\ fruit is \"mango\"" # my favourite\ fruit is "mango"
print(fav)

