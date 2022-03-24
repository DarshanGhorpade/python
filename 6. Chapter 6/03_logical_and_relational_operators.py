# Author: Darshan Ghorpade
# Location: Earth
# Date: 24/03/2022

# Relational operators: Used to execute conditions inside the if statements. eg. ==, >=, <=
# Logical operators: In python logical operators operate on conditional statements. eg. and, or, not

# Accept age from user
age = int(input("Enter your age: "))

# logical and operator
if age>34 and age<56:
    print("You can work with us as senior")
elif age>18 or age<34:
    print("You can work with us as junior")
else:
    print("You can't work with us")

# Important notes:
# 1. There can be any number of elif statements
# 2. Last else is executed only if all the conditions inside elif fails.