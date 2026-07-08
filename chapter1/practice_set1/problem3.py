# Write the python program to print the contents of a directory using os module.
# I have searched in chatgpt just to know how the os module works.

import os

# Print all files and folders in the current directory
contents = os.listdir()

print("Contents of the current directory:")
for item in contents:
    print(item)


import os

# Specify the directory path
path = "C:/Users/Lenovo/Documents"   # Change this to your directory path

print("Contents of the directory:")
for item in os.listdir(path):
    print(item)