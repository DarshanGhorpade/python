# Author: Darshan Ghorpade
# Location: Earth
# Date: 31/03/2022

# Q. Write a program to find the maximum of the numbers in a list using the reduce function.

from functools import reduce

l = [ 2, 5, 1, 6, 7, 9]

a = reduce(max, l)

print(a)