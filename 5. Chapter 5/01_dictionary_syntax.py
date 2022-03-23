# Author: Darshan Ghorpade
# Location: Earth
# Date: 23/03/2022

# Dictionary in Python
# Dictionary is a collection of key-value pairs

# Creating a dictionary
myDict = {
    "Fast": "In a Quick Manner",
    "Darshan": "A Coder",
    "Marks": [67, 78, 98],
    "anotherDict": {"Darshan": "Player"}
}

# print(myDict['Fast'])
# print(myDict['Darshan'])
# print(myDict['Marks'])

# Printing dictionary value that is inside myDict dictionary
print(myDict['anotherDict']['Darshan'])

# Properties of Python dictionaries
# 1. It is unordered.
# 2. It is mutable.
# 3. It is indexed.
# 4. Can't contain dupliacte keys.

# Changing values in dictionary
myDict['Marks'] = [56, 78, 87]
print(myDict['Marks'])