# Author: Darshan Ghorpade
# Location: Earth
# Date: 24/03/2022

# Q. Write a program to calculate the factorial of a given number using for loop.

# n! = 1 x 2 x 3 x ... x n
# 5! = 1 x 2 x 3 x 4 x 5

# Initialise factorial to 1 
factorial = 1


number = int(input("Enter a number: "))

for i in range(1, number+1):
    factorial *= i

# using f string
print(f"Factorial of {number} is {factorial}" )