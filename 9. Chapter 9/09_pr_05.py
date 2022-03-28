# Author: Darshan Ghorpade
# Location: Earth
# Date: 28/03/2022

# Q. Repeat program 4 for a list of such words to be censored.

words = ["donkey", "kaddu", "mote"]

# open file
with open("sample.txt") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "$%^@$^#")
    with open("sample.txt", "w") as f:
        f.write(content)