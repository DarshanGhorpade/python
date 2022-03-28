# Author: Darshan Ghorpade
# Location: Earth
# Date: 28/03/2022

# Employee example

# Create class Employee
class Employee:
    company = "Google"
    salary = 100

Darshan = Employee()
Rajni = Employee()

print(Darshan.company)
print(Rajni.company)

# Creating class attribute for class Employee
# Class Attributes
# An attribute that belongs to the class rather than a particular object.
Employee.company = "Youtube"

# Creating instance attributes for both the objects
# Instance Attributes
# An attribute that belongs to the Instance (object)
Darshan.salary = 30000
Rajni.salary = 25000

# Note: Instance attributes take preference over class attributes during assignment and retrieval.
# Darshan.attribute1  :
# 1. Is attribute1 present in the object?
# 2. Is attribute1 present in class?

print(Darshan.company, end=" ")
print(Darshan.salary)
print(Rajni.company, end=" ")
print(Rajni.salary)