# Author: Darshan Ghorpade
# Location: Earth
# Date: 24/03/2022

# Q. Write a program to find whether a given username contains less than 10 characters or not.

# Accept username from user
username = input("Enter username: ")

# Use len() function
if len(username) < 10:
    print("Username contains characters less than 10")
elif len(username)==10:
    print("Username contains exactly 10 characters")
else:
    print("Username contains characters more than 10")