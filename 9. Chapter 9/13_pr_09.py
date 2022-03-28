# Author: Darshan Ghorpade
# Location: Earth
# Date: 28/03/2022

# Q. Write a program to find out whether a file is identical and matches the content of another file.

file1 = "copy.txt"
file2 = "this.txt"

with open(file1) as f:
    f1 = f.read()

with open(file2) as f:
    f2 = f.read()

if f1 == f2:
    print("Files are identical")
else:
    print("Files aren't identical")