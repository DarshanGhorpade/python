# Author: Darshan Ghorpade
# Location: Earth
# Date: 25/03/2022

# Project 1: Snake, Water, Gun Game
# Its similar to Rock Paper Scissors Game

# We all have played snake, water gun game in our childhood. 
# If you haven’t, google the rules of this game and write a Python program 
# capable of playing this game with the user

import random

def gameWin(comp, you):
    # If two values are equal, declare a tie!
    if comp == you:
        return None

    # Check for all possibilities when computer chose s
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True

    # Check for all possibilities when computer chose w
    elif comp == 'w':
        if you == 's':
            return True
        elif you == 'g':
            return False

    # Check for all possibilities when computer chose g
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True

print("Comp Turn: Snake(s) Water(w) or Gun(g)? ")
randomNo = random.randint(1, 3)
# print(randomNo)
if randomNo == 1:
    comp = 's'
elif randomNo == 2:
    comp = 'w'
elif randomNo == 3:
    comp = 'g'


you = input("Your Turn: Snake(s) Water(w) or Gun(g)? ")
a = gameWin(comp, you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!!")
else:
    print("You Lose!")