# Author: Darshan Ghorpade
# Location: Earth
# Date: 30/03/2022

# The global keyword
# global keyword is used to modify the variable outside of the current scope.

a = 54      # Global variable

def func1():
    global a
    print(f"print statement 1: {a}")
    a = 8   # Local variable if global keyword is not used
    print(f"print statement 2: {a}")

func1()
print(f"print statement 3: {a}")