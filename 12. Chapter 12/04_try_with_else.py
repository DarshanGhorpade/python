# Author: Darshan Ghorpade
# Location: Earth
# Date: 30/03/2022

# try with else clause
# Sometimes we want to run a piece of code when try was successful.

try:
    i = int(input("Enter a number: "))
    c = 1/i
except Exception as e:
    print(e)
else:
    print("We are successful")