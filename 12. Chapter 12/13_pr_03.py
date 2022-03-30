# Author: Darshan Ghorpade
# Location: Earth
# Date: 30/03/2022

# Q. Write a list comprehension to print a list that contains the multiplication table of a user-entered number.

num = int(input("Enter a number: "))

table = [num*i for i in range(1, 11) ]
print(table)