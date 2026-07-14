#A spam comment is defined as text containing of following keywords:
# "Make a lot of money", "buy now", "subscribe this", "click this". Write a program to detect this spams.

p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe now"
p4 = "click this"

message = input("Enter a comment: ")

if ((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("The comment is a spam")

else:
    print("This comment is not a spam")