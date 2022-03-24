# Author: Darshan Ghorpade
# Location: Earth
# Date: 24/03/2022

# Q. Write a program which finds out whether a given name is present in a list or not.

names = ["darshan", "shubham", "rohit", "rohan", "aditi"]

name = input("Enter the nameto check: ")

if name in names:
    print("Your name is present in the list")
else:
    print("Your name is not present in the list")