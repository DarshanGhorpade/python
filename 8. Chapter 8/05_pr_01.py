# Author: Darshan Ghorpade
# Location: Earth
# Date: 25/03/2022

# Q. Write a program using the function to find the greatest of three numbers.

def maximum(num1, num2, num3):
    if num1 > num2:
        if num1 > num3:
            return num1
        else:
            return num3
    else:
        if num2 > num3:
            return num2
        else:
            return num3


print("The greatest among 1, 10, 3 is", maximum(1,10,3))