# Author: Darshan Ghorpade
# Location: Earth
# Date: 30/03/2022

# Q. Store the multiplication tables generated in problem 3 in a file named Tables.txt.

# Accept number from user
num = int(input("Enter your number: "))

# Generate table of number and store it in list by using list comprehension
table = [num*i for i in range(1, 11)]
# print(table)

# Write the table to the file
with open("Tables.txt", "a") as f:
    f.write(f"Table of {num}: ")
    f.write(str(table))
    f.write('\n')
    print("Table stored in file successfully.")