# Author: Darshan Ghorpade
# Location: Earth
# Date: 28/03/2022

# Q. Write a program to find out the line number where python is present from question 6.

content = True

i = 1

with open("log.txt") as f:
    while content:
        content = f.readline()
        
        if 'python' in content.lower():
            print(content)
            print(f"Yes python is present on line number {i}")
        i += 1