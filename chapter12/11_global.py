a =67 #global variable

def func():
    global a
    a = 3 #local variable
    print(a)

print(a)
func()
print(f"a=67 is changed to a={a} with global keyword")