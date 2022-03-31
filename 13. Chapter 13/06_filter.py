# Author: Darshan Ghorpade
# Location: Earth
# Date: 31/03/2022

# Filter
# Filter creates a list of items for which the function returns true.
# list(filter(function))            #function can be a lambda function

def greater_than_5(num):
    if num > 5:
        return True
    else:
        return False

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list(filter(greater_than_5, l)))