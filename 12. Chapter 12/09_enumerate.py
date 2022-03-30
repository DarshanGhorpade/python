# Author: Darshan Ghorpade
# Location: Earth
# Date: 30/03/2022

# enumerate function in Python
# The enumerate function adds counter to an iterable and returns it.

list1 = [1, 3, 53, False, 6.2, "Darshan"]

# index =0
# for item in list1:
#     print(index, item)
#     index += 1


for index, item in enumerate(list1):
    print(index, item)