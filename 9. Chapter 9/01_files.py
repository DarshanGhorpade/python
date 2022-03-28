# Author: Darshan Ghorpade
# Location: Earth
# Date: 28/03/2022

# Files I/O in Python
# The random access memory is volatile, and all its contents are lost once a program terminates.
# In order to persist the data forever, we use files.

# What is file?
# A file is data stored in a storage device. A python program can talk to the file by reading 
# content from it and writing content to it.

# Types of files
# There are 2 types of files:
# 1. Text files (.txt, .c, etc)
# 2. Binary files (.jpg, .dat, etc)

# Python has a lot of functions for reading, updating, and deleting files.

# 1. Opening a file
# Python has an open() function for opening files. It takes 2 parameters: filename and mode.

# open file in read mode
# Use open function to read the content of a file!
# f = open('sample.txt', 'r')
f = open('sample.txt')  # by default the mode is r

# data = f.read()
data = f.read(7) # reads first 7 characters from the file
print(data)

# close the file
f.close()

# Modes of opening a file
# 1. r – open for reading
# 2. w – open for writing
# 3. a – open for appending
# 4. + -> open for updating
# 5. ‘rb’ will open for read in binary mode
# 6. ‘rt’ will open for read in text mode