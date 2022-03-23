# Author: Darshan Ghorpade
# Location: Earth
# Date: 23/03/2022

# Set methods in python

# Creating an empty set
from ctypes import Union


a = set()
print(type(a))

# 1. add(value): To add items to the set
a.add(4)
a.add(5)
a.add(4)    # Adding a value repeatedly does not change the set

# Printing the set
print(a)

# This will throw error
# a.add([4,5,6])  # TypeError: unhashable type: 'list'
# As list is mutable and set is not mutable so we can't add list to set

# Also
# a.add({4:5})    # We can't add dictionary to set

# We can add tuple to set
a.add((5, 6))
print(a)


# 2. len(): Returns length of the set
print(len(a))


# 3. remove(): Removes the value from the set
a.remove((5,6)) # removes tuple (5,6) from set a
# a.remove(15)    # throws an error while trying to remove 15 which is not present in set
print(a)


# 4. pop(): Removes an arbitrary element from the set and returns the element removed 
print(a.pop())
print(a)


# 5. clear(): Make the set empty
a.clear()
print(a)

# 6. union(): Returns a new set with all items from both the sets
b = {1, 2, 3, 4}
c = {2, 4, 5, 6}
print(b.union(c))

# 7. intersection(): Returns a new set which contains only items present in both the sets
print(b.intersection(c))