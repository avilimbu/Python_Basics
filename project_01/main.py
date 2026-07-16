import random

# Snake = -1
# Water =0
# Gun = 1

#opening game interface
print("Welcome to the Snake, Water, Gun Game:")
print("______________________________________")

#game logic
def game():
    ComputerChoice = random.choice([-1,0,1])
    Choice = input('''Enter your choice:
    "s" for "Snake"
    "w" for "Water" and
    "g" for "Gun"\n\n: ''').lower()

    youdict = {
        "s":-1,
        "w":0,
        "g":1
    }

    revdict = {
        -1: "Snake",
        0: "Water",
        1: "Gun"
    }

    UserChoice = youdict[Choice]

    print(f"Computer choose {revdict[ComputerChoice]}")
    print(f"you choose {revdict[UserChoice]}")

    if (ComputerChoice == UserChoice):
            print("Draw!")
    else:
        if (ComputerChoice==-1 and UserChoice==0):
            print("You lose!")
        elif (ComputerChoice==-1 and UserChoice==1):
            print("You Win!")
        elif (ComputerChoice==0 and UserChoice==-1):
            print("You Win!")
        elif (ComputerChoice==0 and UserChoice==1):
            print("You lose!")
        elif (ComputerChoice==1 and UserChoice==-1):
            print("You lose!")
        elif (ComputerChoice==1 and UserChoice==0):
            print("You Win!")
        else:
            print("Your choise is invalid!")




#game runs from here
cont = "yes"

while True:
    if (cont == "yes"):
        game()
       
    else:
        print("Thank you for playing the game.")
        break
    cont= input("Do you want to continue this game.\nEnter 'yes' to continue and Anything to end the game: ").strip().lower()
    print("\n")