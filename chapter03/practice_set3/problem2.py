#  Write a program to fill in a letter tamplete given below with name and date.
#`letters = Dear <|Name|>,
# You are choosen to come in a seminar.
# <|Date|>

letters = '''Dear <|Name|>,
You are choosen to come in a seminar.
<|Date|> '''

user = input("enter your name: ").strip()
print(letters.replace("<|Name|>", user).replace("<|Date|>", "2025"))
