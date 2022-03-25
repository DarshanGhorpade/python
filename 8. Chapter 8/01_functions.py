# Author: Darshan Ghorpade
# Location: Earth
# Date: 25/03/2022

# functions in Python

# A function is a group of statements performing a specific task.
# When a program gets bigger in size and its complexity grows, 
# it gets difficult for a programmer to keep track of which piece of code is doing what!
# A function can be reused by the programmer in a given program any number of times.

# Function definition
# The part containing the exact set of instructions that are executed during the function call.

# Define a function to calculate percent
def percent(marks): 
    return ((marks[0] + marks[1] + marks[2] + marks[3]) / 400) * 100

marks1 = [45, 76, 78, 77]
# percentage1 = (sum(marks1)/400) * 100
# percentage1 = ((marks1[0] + marks1[1] + marks1[2] + marks1[3]) / 400) * 100

# Function call
# Whenever we want to call a function, we put the name of the function followed by parenthesis as follows:

percentage1 = percent(marks1)   # function call to percent
print(percentage1)

marks2 = [65, 67, 98, 80]
# percentage2 = (sum(marks2)/400) * 100
# percentage2 = ((marks2[0] + marks2[1] + marks2[2] + marks2[3]) / 400) * 100
percentage2 = percent(marks2)
print(percentage2)


# Types of functions in Python
# There are two types of functions in Python:
# 1. Built-in functions # Already present in Python
# 2. User-defined functions # Defined by the user