# 2. The game() function in a program lets a user play a game and returns the score
# as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or
# contains the previous Hi-score. You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score.
import random as rd

def game():
    score = rd.randint(1, 10000)
    print(f'New score: {score}')
    return score

score1=game()

with open("Hi-score.txt", "r") as f:
    hiscore = f.read()
    hiscore=int(hiscore)

if score1>hiscore:
    hiscore=str(score1)
    with open("Hi-score.txt", "w") as f:
        f.write(hiscore)
        print("the updated value ",hiscore)
else:
    print("NO New Hi-Score")
