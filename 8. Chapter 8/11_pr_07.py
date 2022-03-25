# Author: Darshan Ghorpade
# Location: Earth
# Date: 25/03/2022

# Q. Write a python function to remove a given word from a string and strip it at the same time.

# strip function is strings
# strip function removes unwanted spaces in string
# this = "           Darshan is a good boy      "
# print(this)
# print(this.strip())

def remove_and_split(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()


string = "           Darshan is a good boy      "
result = remove_and_split(string, "Darshan")

print(result)