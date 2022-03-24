# Author: Darshan Ghorpade
# Location: Earth
# Date: 24/03/2022

# Q. Write a program to find the sum of first n natural numbers using a while loop.

# Initialise i to 1 
i = 1

# Initialise sum to 0 
sum = 0

# Accept value of n from user
n = int(input("Enter number n: "))

while i<=n:
    sum += i
    i += 1

print("Sum of first " + str(n) +" natural numbers is", sum)