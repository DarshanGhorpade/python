# Author: Darshan Ghorpade
# Location: Earth
# Date: 25/03/2022

# Q. Write a python function that converts inches to cms.

def centimeters(inches):
    return inches * 2.54

inches = int(input("Enter inches: "))

print(str(inches) + " inches = " + str(centimeters(inches)) + " cms")
