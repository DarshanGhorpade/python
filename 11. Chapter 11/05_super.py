# Author: Darshan Ghorpade
# Location: Earth
# Date: 29/03/2022

# Super() method
# Super method is used to access the methods of a superclass in the derived class.

class Person:
    country = "India"

    def __init__(self):
        print("Initialising Person...")

    def takeBreak(self):
        print("I am taking break for 5 minutes...")

class Employee(Person):
    company = "Honda"

    def __init__(self):
        super().__init__()  # Calls constructor of the base class
        print("Initialising Employee...")

    def getSalary(self):
        print(f"Salary: {self.salary}")

    def takeBreak(self):
        super().takeBreak()
        print("Employee can take break for max 10 minutes...")

class Programmer(Employee):
    company = "Fiverr"

    def __init__(self):
        super().__init__()  # Calls constructor of the base class
        print("Initialising Programmer...")

    def getSalary(self):
        print("No salary for programmer")

    def takeBreak(self):
        super().takeBreak()
        print("Programmer can take break for max 5 minutes...")

p = Person()
e = Employee()
pr = Programmer()

# p.takeBreak()
# e.takeBreak()
# pr.takeBreak()