# Author: Darshan Ghorpade
# Location: Earth
# Date: 28/03/2022

# Q. A file contains the word “Donkey” multiple times. 
# You need to write a program which replaces this word with ###### by updating the same file.

# open file
with open("sample.txt") as f:
    content = f.read()

content = content.replace("donkey", "$%^@$^#")

with open("sample.txt", "w") as f:
    f.write(content)