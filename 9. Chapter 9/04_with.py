# Author: Darshan Ghorpade
# Location: Earth
# Date: 28/03/2022

# With statement in Python
# The best way to open and close the file automatically is the “with” statement.

# The main advantage of using with is
# There is no need to write f.close() as it is done automatically


with open('another.txt', 'w') as f:
    a = f.write("me")
with open('another.txt', 'r') as f:
    a = f.read()
print(a)