#  Write a program to find out whether a given username contains less than 10 characters or not.

username = input("Enter your username: ")

if (len(username)<10):
    print("Please enter 10 or more than 10 character in a username.")

else:
    print("All fine")