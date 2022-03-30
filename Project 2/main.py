# Author: Darshan Ghorpade
# Location: Earth
# Date: 30/03/2022

# Project 2: Perfect guess
# We are going to write a program that generates a random number and asks the user to guess it.
# If the player’s guess is higher than the actual number, the program displays “Lower number please”. 
# Similarly, if the user’s guess is too low, the program prints “higher number please”.
# When the user guesses the correct number, the program displays the number of guesses the player 
# used to arrive at the number.
# Hint: Use the random module

import random

# Generate a random number between 1 to 100
randNumber = random.randint(1, 100)
# print(randNumber)

# Initialise userGuess to None and guesses to zero
userGuess = None
guesses = 0

# Now run while loop until userGuess the right number
while(userGuess != randNumber):
    userGuess = int(input("Enter your guess: "))
    guesses += 1
    if(userGuess == randNumber):
        print("You guessed it right!")
    else:
        if(userGuess > randNumber):
            print("You guessed it wrong! Enter smaller number")
        else:
            print("You guessed it wrong! Enter greater number")
    

print(f"You guessed the number in {guesses} guesses")

# Read hiscore from file
with open("hiscore.txt", "r") as f:
    hiscore = int(f.read())

# Write the score in file only if the current score is less than the stored value in file
if(guesses < hiscore):
    print("You have just broken the high score!")
    with open("hiscore.txt", "w") as f:
        f.write(str(guesses))