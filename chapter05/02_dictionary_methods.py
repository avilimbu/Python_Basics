marks = {
    "harry" : 100,
    "jerry" : 45,
    "merry" : 67
}

#items()
print(marks.items())

#keys()
print(marks.keys())

#values()
print(marks.values())

#update()
marks.update({"harry":99, "cantly":78})
print(marks)

#get method | It avoids error as it returns None if any key is not found
print(marks.get("harry"))
print(marks.get("saimon"))

#pop()
print(marks.pop('harry', "key not found"))

#popitem() | Removes the last item
print(marks.popitem())

#len() function
print(len(marks))