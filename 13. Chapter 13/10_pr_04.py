# Author: Darshan Ghorpade
# Location: Earth
# Date: 31/03/2022

# Q. Write a program to filter a list of numbers that are divisible by 5.

def divisible_by_5(num):
    if num%5 == 0:
        return True
    else:
        return False

l = [1, 4, 5, 8, 13, 20, 26, 34, 40, 44, 55]

print(list(filter(divisible_by_5, l)))

# Using lambda
a = filter(lambda a: a%5 == 0, l)
print(list(a))