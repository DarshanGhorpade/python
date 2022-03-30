# Author: Darshan Ghorpade
# Location: Earth
# Date: 30/03/2022

# try with finally
# Python offers a finally clause which ensures execution of a piece of code irrespective of the exception.

try:
    i = int(input("Enter a number: "))
    c = 1/i
except Exception as e:
    print(e)
    exit()
finally:
    print("We are done")

print("Thanks for using the program")