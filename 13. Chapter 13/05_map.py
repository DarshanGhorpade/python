# Author: Darshan Ghorpade
# Location: Earth
# Date: 31/03/2022

# Map, Filter & Reduce
# Map applies a function to all the items in an input_list.
# Syntax:
# map(function, input_list)             #function can be lambda function

def square(num):
    return num*num

l1 = [1, 2, 3]
l2 = []

# method 1
for item in l1:
    l2.append(square(item))
print(l2)

# method 2
print(list(map(square, l1)))