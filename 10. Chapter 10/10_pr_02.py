# Author: Darshan Ghorpade
# Location: Earth
# Date: 28/03/2022

# Q. Write a class calculator capable of finding square, cube, and the square root of a number.

class Calculator:
    # constructor
    def __init__(self, num):
        self.number = num
    
    # method to calculate square
    def square(self):
        print(f"The value of {self.number} square is {self.number **2}")

    # method to calculate squareroot
    def squareRoot(self):
        print(f"The value of {self.number} square-root is {self.number **0.5}")

    # method to calculate cube
    def cube(self):
        print(f"The value of {self.number} cube is {self.number **3}")

a = Calculator(4)
a.square()
a.squareRoot()
a.cube()