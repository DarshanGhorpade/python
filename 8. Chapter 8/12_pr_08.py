# Author: Darshan Ghorpade
# Location: Earth
# Date: 25/03/2022

# Q. Write a python function to print the multiplication table of a given number.

def multiplication(number):
    print("Multiplication table of", number)
    for i in range(1, 11):
        print(str(number) + " X " + str(i) + " = " + str(i*number))

n = int(input("Enter a number: "))
multiplication(n)