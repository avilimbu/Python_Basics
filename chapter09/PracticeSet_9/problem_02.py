#  The game() function in a program let's a user play a game and returns the score as an integer.
#  You need to read the file "hi-score.txt"  which is either blank or contains previous Hi-score.
#  Write a program to update the hi-score whenever the game() functions breaks the Hi-score. 

import random

def game():
    print("-"*20)
    print("You are playing the game")
    score = random.randint(100,1000)

    # Fetch the high score
    with open("hi-score.txt") as f:
        highscore = f.read()
        if (highscore!=""):
            highscore = int(highscore)
        else:
            highscore = 0

    # writing the high-score in the file
    print(f"Your score: {score}")
    if (score>highscore):
        with open ("hi-score.txt", "w") as f:
            f.write(str(score))
    return score

game()