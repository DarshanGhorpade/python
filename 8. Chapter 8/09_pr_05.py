# Author: Darshan Ghorpade
# Location: Earth
# Date: 25/03/2022

# Q. Write a python function to print the first n lines of the following pattern.
'''
***
**       # For n = 3
*
'''

n = int(input("Enter value of n: "))

for i in range(n):
    print("*" * (n-i))