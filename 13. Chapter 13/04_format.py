# Author: Darshan Ghorpade
# Location: Earth
# Date: 31/03/2022

# Format method(Strings)
# Formats the values inside the string into the desired output
# template.format(p1, p2, …)        #p1, p2 … are the arguments

name = "Darshan"
channel = "Darshan Ghorpade"
type = "coding"
# a = f"This is {name}"
# a = "This is {} and his channel is {}".format(name, channel)
a = "This is {0} and his {2} channel is {1}".format(name, channel, type)
print(a)