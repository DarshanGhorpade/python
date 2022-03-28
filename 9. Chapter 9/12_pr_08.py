# Author: Darshan Ghorpade
# Location: Earth
# Date: 28/03/2022

# Q. Write a program to make a copy of a text file “this.txt.”

with open('this.txt') as f:
    content = f.read()

with open('copy.txt', 'w') as f:
    f.write(content)