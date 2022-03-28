# Author: Darshan Ghorpade
# Location: Earth
# Date: 28/03/2022

# Object-Oriented Programming in Python
# Solving a problem by creating objects is one of the most popular approaches in programming. 
# This is called object-oriented programming.
# This concept focuses on using reusable code. (Implements DRY principle)

# What is a Class?
# A class is a blueprint for creating objects.

# What is an Object?
# An object is an instantiation of a class. When class is defined, a template(info) is defined. 
# Memory is allocated only after object instantiation.

# Objects of a given class can invoke the methods available to it without revealing the implementation details to the user.     
# Abstraction & Encapsulation!

# Define a class
class Number:
    # Number class have 2 variables a and b
    def sum(self):
        return self.a + self.b

# Object instatiation
num = Number()

num.a = 16
num.b = 24
s = num.sum()
print(f"The sum of {num.a} and {num.b} is", s)

# a = 16
# b = 24

# print("The sum of a and b is ", a+b)