# Author: Darshan Ghorpade
# Location: Earth
# Date: 24/03/2022

# Q. Write a program to print the multiplication table of a given number using while loop.

# Initialise i to 1
i = 1

# Accept number from user
number = int(input("Enter the number: "))

while i<11:
    # print(str(number) + " X " + str(i) + " = " + str(i*number))
    # Using f-strings
    print(f"{number} X {i} = {number*i}")
    i += 1