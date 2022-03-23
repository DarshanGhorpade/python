# Author: Darshan Ghorpade
# Location: Earth
# Date: 23/03/2022

# Q. Create an empty dictionary. Allow 4 friends to enter their favourite language as values and use keys as their name.
# Assume that the names are unique.

# Q.7 If names of two friends are same; What will happen to the program in problem 6?
# Then it will override the value for that friend name

# Q.8 If languages of two friends are same; What will happen to the program in problem 6?
# It will work, In dictionary keys are unique, its allowed values not to be unique.

favLang = {}

a = input("Enter your favourite language Shubham: ")
b = input("Enter your favourite language Ankit: ")
c = input("Enter your favourite language Sonali: ")
d = input("Enter your favourite language Harshita: ")

favLang['Shubham'] = a
favLang['Ankit'] = b
favLang['Sonali'] = c
# favLang['Shubham'] = c    # Override the value for key Shubham
favLang['Harshita'] = d

print(favLang)