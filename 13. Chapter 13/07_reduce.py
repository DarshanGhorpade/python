# Author: Darshan Ghorpade
# Location: Earth
# Date: 31/03/2022

# Reduce in python
# Reduce applies a rolling computation to sequential pair of elements.
# from functools import reduce
# val = reduce(function, list1)        #function can be a lambda function
# If the function computes sum of two numbers and the list is [1, 2, 3, 4]

from functools import reduce

sum = lambda a, b: a+b

l = [1, 2, 3, 4]

val = reduce(sum, l)

print(val)

# This reduce will apply sum on 1 & 2 first = 3 then apply sum on 3 and 3 and so on..