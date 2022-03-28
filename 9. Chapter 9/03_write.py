# Author: Darshan Ghorpade
# Location: Earth
# Date: 28/03/2022

# Writing Files in Python
# In order to write to a file, we first open it in write or append mode, 
# after which, we use the python’s f.write() method to write to the file!

# open file in write mode
f = open('another.txt', 'w')

# write to the file using write function
f.write("Please write this to the file")

# open file in append mode
f = open('another.txt', 'a')

# write to the file using write function
f.write("   I am appending")

# close file
f.close()