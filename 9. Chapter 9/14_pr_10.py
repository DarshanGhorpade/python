# Author: Darshan Ghorpade
# Location: Earth
# Date: 28/03/2022

# Q. Write a program to wipe out the contents of a file using python.

filename = "erase.txt"

with open(filename, "w") as f:
    f.write("")