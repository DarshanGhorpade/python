# Author: Darshan Ghorpade
# Location: Earth
# Date: 22/03/2022

# String functions in Python

story = "once upon a time there was a guy named Darshan who learned python course with notes"

# len() : returns the length of the string 
print(len(story))

# string.endswith("tes") : Tells whether the variable string ends with the string 'tes' or not
print(story.endswith('notes'))
print(story.endswith('Darshan'))

# count() : counts the occurence of character or string in the given string
print(story.count('a'))
print(story.count('Darshan'))

# capitalize() : capitalizes the first character of a given string
print(story.capitalize())

# find() : finds a word and returns the index of first occurence of that word in the string ,if not found word returns -1 
print(story.find("Darshan"))    # prints 39
print(story.find("Ghorpade"))   # prints -1

# replace() : replaces all occurences of oldword with newword
print(story.replace("Darshan", "CodeWithDarshan"))