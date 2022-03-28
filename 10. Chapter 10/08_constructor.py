# Author: Darshan Ghorpade
# Location: Earth
# Date: 28/03/2022

# __init__() constructor in Python
# __init__() is a special method which runs as soon as the object is created.
# __init__() method is also known as constructor.
# It takes self-argument and can also take further arguments.

# Create class Employee
class Employee:
    company = "Google"

    # constructor : initialise the object
    def __init__(self, name, salary, subunit):
        self.name = name
        self.slary = salary
        self.subunit = subunit 
        print("Employee is created!")
        
    def getDetails(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.slary}")
        print(f"Subunit: {self.subunit}")

    def getSalary(self, signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")

    # Static methods
    # Sometimes we need a function that doesn’t use the self-parameter. We can define a static method like this:
    @staticmethod   # method decorator
    def greet():
        print("Good Morning, Sir")

    @staticmethod
    def time():
        print("The time is 9AM in the morning")

Darshan = Employee("Darshan", "100", "Youtube")
# Darshan = Employee() --> This throws an error (missing 3 required positional arguments:)
Darshan.getDetails()