# Author: Darshan Ghorpade
# Location: Earth
# Date: 22/03/2022

# String Slicing in Python
# A string in python can be sliced for getting a part of string

greeting = "Good Afternoon, "
name = "Darshan"
# print(type(name))

print(greeting + name)

c = greeting + name
print(c)

# Index
# name = D a r s h a n
#        0 1 2 3 4 5 6

print(name[0])

# name[3] = "a" --> will not work

# Slicing

print(name[0:3])    # will print characters at 0, 1, 2

print(name[:4])     # will replace the blank by minimum index i.e 0
# i.e print(name[0:4])

print(name[3:])     # will replace the blank by maximum index i.e 6
# i.e print(name[3:6])

# Negative index
# name = D a r s h a n
#       -6  . . . -2 -1
print(name[-1])

c = name[-4:-1]
print(c)


# Slicing with skip value
# We can provide a skip value as a part of our slice 

name = "DarshanIsGood"
# name = D a r s h a n I s G o  o  d
#        0 1 2 3 4 5 6 7 8 9 10 11 12

d = name[1:4:1] # will not skip anything as skip value is 1
d = name[0::2] # skip every second character 
print(d)