# Author: Darshan Ghorpade
# Location: Earth
# Date: 24/03/2022

# Q. Write a program to greet all the person names stored in a list l1 and which starts with S.

l1 = ["Harry", "Soham", "Sachin", "Rohit"]

for name in l1:
    if name.startswith("S"):
        print("Hello " + name)