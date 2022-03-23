# Author: Darshan Ghorpade
# Location: Earth
# Date: 23/03/2022

# Dictionary methods in Python

# Creating a dictionary
myDict = {
    "Fast": "In a Quick Manner",
    "Darshan": "A Coder",
    "Marks": [67, 78, 98],
    "anotherDict": {"Darshan": "Player"},
    1: 2,
}

# 1. keys(): Print all keys of the dictionary
print(myDict.keys())
# Print its type
print(type(myDict.keys()))
# Covert it to list
print(list(myDict.keys()))

# 2. values(): print the values of the dictionary
print(myDict.values())

# 3. items(): print the (key, value) for all contents of the dictionary
print(myDict.items())

# 4. update(): updates the dictionary by adding key-value pairs from updateDict
print(myDict)
updateDict = {
    "Lovish": "Friend",
    "Divya": "Friend",
    "Darshan": "A Dancer",
}
myDict.update(updateDict)
print(myDict)

# 5. get(): prints value associated with key
print(myDict.get("Darshan"))

# Difference between .get and [] syntax in Dictionaries?
# If a key is not present in dictionary get() will return None
print(myDict.get("Darshan2"))   # returns None
print(myDict["Darshan2"])   # thows error as Darshan2 is not present in the dictionary