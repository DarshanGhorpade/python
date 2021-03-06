# Author: Darshan Ghorpade
# Location: Earth
# Date: 29/03/2022

# Inheritance in python
# Inheritance is a way of creating a new class from an existing class
# We can use the methods and attributes of Employee in Programmer object.
# Also, we can overwrite or add new attributes and methods in the Programmer class.

class Employee:     # Base class
    company = "Google"

    def showDetails(self):
        print("This is an Employee")

class Programmer(Employee):     # Derived or Child class
    company = "Youtube"
    language = "Python"

    def getLanguage(self):
        print(f"The language is {self.language}")

    def showDetails(self):
        print("This is an Programmer")

e = Employee()
e.showDetails()

p = Programmer()
p.showDetails()
# print(p.company)
print(p.company)