# Author: Darshan Ghorpade
# Location: Earth
# Date: 31/03/2022

# Q. A list contains the multiplication table of 7. 
# Write a program to convert it to a vertical string of the same numbers (7,14,….)

l = [str(i*7) for i in range(1, 11)]
verticalTable = "\n".join(l)
print(verticalTable)