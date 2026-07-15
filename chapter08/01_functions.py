# function

def func1(): #function defination
    a = int(input("Enter the marks: "))
    b = int(input("Enter the marks: "))
    c = int(input("Enter the marks: "))
    avg = (a+b+c)/3
    print(avg)

func1() #function calling

#quick quiz
def GoodDay():
    name = input("Enter your name: ").strip()
    print(f"Good day, {name}")

GoodDay()