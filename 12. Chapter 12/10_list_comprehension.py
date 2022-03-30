# Author: Darshan Ghorpade
# Location: Earth
# Date: 30/03/2022

# List comprehensions
# List comprehensions is an elegant way to create lists based on existing lists.
# list1 = [1, 7, 12, 11, 22]
# list2 = [i for item in list1 if item>8]

a = [4, 5, 6, 8, 11, 15, 18, 22, 27, 29, 78]

# b = []
# for item in a:
#     if item % 2 == 0:
#         b.append(item)
# print(b)

# Shortcut to write the same:
b = [i for i in a if i%2 == 0]
print(b)