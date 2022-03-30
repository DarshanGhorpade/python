# Author: Darshan Ghorpade
# Location: Earth
# Date: 30/03/2022

# Q. Write a program to display a/b where a and b are integers. If b=0, display infinite by handling the ZeroDivisionError.

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

try:
    print(f"a/b = {a/b}")
except ZeroDivisionError:
    print("infinite")