
def goodDay(name, ending):
    print("Good Day "+name)
    print(ending)

goodDay("Avhi", "Thank you")
goodDay("Roman", "Thanks")



print("------------------")
# function with return
def goodDay(name, ending):
    print("Good Day "+name)
    print(ending)
    return "ok"

a= goodDay("Avhi", "Thank you")
print(a)
