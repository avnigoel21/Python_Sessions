# The game() function in a program lets a user play a game and returns the score as an integer.
# You need to read a file 'HighScore.txt' which is either blank or contains the previous High-score
# You need to write a program to update the High-score whenever game() breaks the high score.



def game():
    return 100

score = game()

with open("highScore.txt") as f:
    highScoreStr = f.read()

if highScoreStr == '' or int(highScoreStr)<score :
    with open ("highScore.txt" , 'w') as f:
        f.write(str(score))




