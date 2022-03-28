# Author: Darshan Ghorpade
# Location: Earth
# Date: 28/03/2022

# Q. Write a program to read the text from a given file, “poems.txt” and find out whether it contains the word ‘twinkle’.

# open file 
f = open('poems.txt')

# read data from file
t = f.read()

# check is twinkle is in file data or not
if 'twinkle' in t:
    print("Twinkle word is present in file text")
else:
    print("Twinkle word isn't present in file text")