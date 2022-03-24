# Author: Darshan Ghorpade
# Location: Earth
# Date: 24/03/2022

# Q. Write a program to print the following star pattern.
'''    *
      ***  
     *****   for n=3'''

# Initialise n to 3 
n = 3

for i in range(n):
    print(" " * (n-i-1), end="")
    print("*" * (2*i+1), end="")
    print(" " * (n-i-1))