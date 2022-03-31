# Author: Darshan Ghorpade
# Location: Earth
# Date: 31/03/2022

# Q. Write a program to input name, marks and phone number of a student and format it using the format function like below:
#   “The name of the student is Harry, his marks are 72 and the phone number is 99999888”

name = input("Enter your name: ")
marks = input("Enter your marks: ")
phone = input("Enter your phone no.: ")

template = "The name of the student is {}, his marks are {} and the phone number is {}".format(name, marks, phone)
print(template)