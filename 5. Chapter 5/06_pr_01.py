# Author: Darshan Ghorpade
# Location: Earth
# Date: 23/03/2022

# Q. Write a program to create a dictionary of Hindiwords with values as there English translation.
# Provide user with an option to look it up!

myDict = {
    "Pankha": "Fan",
    "Dabba": "Box",
    "Dawai": "Medicine",
}

print("Options are ", myDict.keys())

a = input("Enter the Hindi word: ")
# print("The meaning of word "+ a + " in English is", myDict[a])

# Below line will not throw an error if the key is not present in the dictionary
print("The meaning of word "+ a + " in English is", myDict.get(a))