# Author: Darshan Ghorpade
# Location: Earth
# Date: 24/03/2022

# Q. Write a program to print the multiplication table of a given number using for loop.

number = int(input("Enter the number: "))

for i in range(1, 11):
    # print(str(number) + " X " + str(i) + " = " + str(i*number))
    # Using f-strings
    print(f"{number} X {i} = {number*i}")