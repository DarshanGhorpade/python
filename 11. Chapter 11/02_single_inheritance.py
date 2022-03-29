# Author: Darshan Ghorpade
# Location: Earth
# Date: 29/03/2022

# Types of Inheritance in python
# 1. Single inheritance
# 2. Multiple inheritance
# 3. Multilevel inheritance

# 1. Single inheritance
# Single inheritance occurs when a child class inherits only a single parent class.
# Base -> Derived
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