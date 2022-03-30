# Author: Darshan Ghorpade
# Location: Earth
# Date: 30/03/2022

# Q. Write a program to print the third, fifth, and seventh elements from a list using the enumerate function.

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for index, item in enumerate(l):
    if index == 2 or index == 4 or index ==  6:
        # print(index, item)
        print(f"The {index+1}th element is {item}")