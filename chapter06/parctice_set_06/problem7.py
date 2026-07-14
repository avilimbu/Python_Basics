# Write a program to find out whether a given post is talking about "shyam" or not.

post = input("Enter the post: ")

if ("shyam".lower() in post.lower()):
    print("This post is talking about shyam")

else:
    print("This post is not talking about shyam")