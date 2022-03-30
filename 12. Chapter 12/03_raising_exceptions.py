# Author: Darshan Ghorpade
# Location: Earth
# Date: 30/03/2022

# Raising Exceptions
# To use custom messages while raising exception
# We can raise custom exceptions using the raise keyword in python.

def Increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("This is not good - Darshan")

a = Increment("23")
print(a)