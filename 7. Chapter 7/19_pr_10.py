# Author: Darshan Ghorpade
# Location: Earth
# Date: 24/03/2022

# Q. Write a program to print the multiplication table of n using for loop in reversed order.

# Accept number from user
number = int(input("Enter the number: "))

# Initialise a to 10
a = 10

for i in range(1, 11):
    # print(str(number) + " X " + str(i) + " = " + str(i*number))
    # Using f-strings
    print(f"{number} X {a} = {number*a}")
    a -= 1