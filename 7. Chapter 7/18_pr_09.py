# Author: Darshan Ghorpade
# Location: Earth
# Date: 24/03/2022

# Q. Write a program to print the following star pattern:
'''
   * * *
   *   *             #For n=3
   * * * 
'''

# Initialise n to 3
n = 3

for i in range(n):
   for j in range(n):
      if i == 0 or i == n - 1 or j == 0 or j == n - 1:
         print("*", end=" ")
      else:
         print(" ", end=" ")
   print()