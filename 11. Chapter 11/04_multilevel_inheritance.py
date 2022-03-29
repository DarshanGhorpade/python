# Author: Darshan Ghorpade
# Location: Earth
# Date: 29/03/2022

# 2. Multilevel inheritance
# Multiple inheritances occurs when the child class inherits from more than one parent class.

class Person:
    country = "India"

    def takeBreak(self):
        print("I am taking break for 5 minutes...")

class Employee(Person):
    company = "Honda"

    def getSalary(self):
        print(f"Salary: {self.salary}")

    def takeBreak(self):
        print("Employee can take break for max 10 minutes...")

class Programmer(Employee):
    company = "Fiverr"

    def getSalary(self):
        print("No salary for programmer")

p = Person()
e = Employee()
pr = Programmer()

p.takeBreak()
pr.getSalary()
pr.takeBreak()
e.takeBreak()
print(pr.country)