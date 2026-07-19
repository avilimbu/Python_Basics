#Create a class with class attribute a; create a object from it and set 'a' directly usimg 
# object.a =0. Does this change the class attribute?

class Demo:
    a=4

ob = Demo()
print(ob.a) #prints class attributes as no any instance attrubute is available
ob.a=0
print(ob.a) #prefers instance attrubutes in place of class attribute
print(Demo.a)

#The class attributes doesn't change