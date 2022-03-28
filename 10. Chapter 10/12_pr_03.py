# Author: Darshan Ghorpade
# Location: Earth
# Date: 28/03/2022

# Q. Add a static method in problem 2 to greet the user with hello.

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

    # static method
    @staticmethod
    def greet():
        print("\n*************Hello there welcome to the best calculator of the world*************\n")

a = Calculator(4)
# call static method
a.greet()
a.square()
a.squareRoot()
a.cube()