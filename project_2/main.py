import random

n = random.randint(0,100)
print("The Perfect Guess Game")
print("-"*30)
guess = 1
a = -1

while (a!=n):
    a = int(input("Enter the number: "))
    if(a>n):
        guess+=1
        print("Lower number please")
    elif(a<n):
        guess+=1
        print("Higher number please")

print(f"You have guessed the correct number {n} in {guess} attempts")