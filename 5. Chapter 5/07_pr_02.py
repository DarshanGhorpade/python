# Author: Darshan Ghorpade
# Location: Earth
# Date: 23/03/2022

# Q. Write a program to input 8 numbers from user and display all the unique numbers(once).

# Accept the 8 numbers from user
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))
num5 = int(input("Enter number 5: "))
num6 = int(input("Enter number 6: "))
num7 = int(input("Enter number 7: "))
num8 = int(input("Enter number 8: "))

# Storing the values in set so repeated values will be ignored
s = {num1, num2, num3, num4, num5, num6, num7, num8}

# Printing the set
print(s)