# Author: Darshan Ghorpade
# Location: Earth
# Date: 25/03/2022

# Q. Write a recursive function to calculate the sum of first n natural numbers

def sum_recursive(n):
    if n==0:
        return 0
    return n + sum_recursive(n-1)


sum = sum_recursive(5)
print(sum)