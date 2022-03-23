# Author: Darshan Ghorpade
# Location: Earth
# Date: 23/03/2022

# Q. Write a program to accept marks of 6 students and display them in a sorted manner.

# Accept the marks as integer (using typecasting) from the user
m1 = int(input("Enter marks for student no 1: "))
m2 = int(input("Enter marks for student no 2: "))
m3 = int(input("Enter marks for student no 3: "))
m4 = int(input("Enter marks for student no 4: "))
m5 = int(input("Enter marks for student no 5: "))
m6 = int(input("Enter marks for student no 6: "))

# Store the marks in list
myList = [m1, m2, m3, m4, m5, m6]

# Use sort method of list
myList.sort()

# Print the list
print(myList)