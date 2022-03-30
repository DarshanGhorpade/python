# Author: Darshan Ghorpade
# Location: Earth
# Date: 30/03/2022

# Handling different exceptions in Python

try:
    a = int(input("Enter a number: "))
    c = 1/a
    print(c)
except ValueError as e:
    print("Please enter a valid value")
    # print(e)
except ZeroDivisionError as e:
    print("Make sure you are not dividing by zero!")
    # print(e)

print("Thanks for using this code!")