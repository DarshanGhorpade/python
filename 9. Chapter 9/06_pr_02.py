# Author: Darshan Ghorpade
# Location: Earth
# Date: 28/03/2022

# Q. The game() function in a program lets a user play a game and returns the score as an integer. 
#    You need to read a file “Hiscore.txt” which is either blank or contains the previous Hi-score. 
#    You need to write a program to update the Hi-score whenever game() breaks the Hi-Score.

# Suppose there is a function game which returns some value say 64 here
def game():
    return 64

# call game() function
score = game()

# open file in read mode and assign value stored in it to a variable hiscoreStr
with open('hiscore.txt') as f:
    hiscoreStr = int(f.read())

# if hiscoreStr contain nothing then write the score directly to file
if hiscoreStr=='':
  with open('hiscore.txt', 'w') as f:
        f.write(str(score))

# if hiscoreStr contain some score compare the scores then write the max score to file
elif int(hiscoreStr)<score:
    with open('hiscore.txt', 'w') as f:
        f.write(str(score))