# Author: Darshan Ghorpade
# Location: Earth
# Date: 24/03/2022

# Q. Write a program to find whether a given number is prime or not.

# Declare prime as True
prime = True

# Accept the number from user
number = int(input("Enter the number: "))

for i in range(2, number):
    if number%i == 0 and number!=2:
        prime = False
        break

if number <= 1:
    prime = False

if prime:
    print(str(number) + " is prime")
else:
    print(str(number) + " is not prime")