# Author: Darshan Ghorpade
# Location: Earth
# Date: 31/03/2022

# Lambda functions
# Functions created using an expression using the lambda keyword

# Syntax:
# lambda arguments: expressions (can be used as a normal function)

# def func(a):
    # return a+5

# lambda function
func = lambda a:a+5

square = lambda x:x*x

sum = lambda a, b, c: a+b+c

x = 3

print(func(x))
print(square(x))
print(sum(x, 2, 1))