# Author: Darshan Ghorpade
# Location: Earth
# Date: 28/03/2022

# readline function
# Other methods to read the file
# We can also use f.readline() function to read one full line at a time.
# f.readline()               #Reads one line from the file

# open the file
f = open('sample.txt')  # by default the mode is r

# read first line
data = f.readline()
print(data)

# read second line
data = f.readline()
print(data)

# close the file
f.close()