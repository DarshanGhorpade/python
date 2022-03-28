# Author: Darshan Ghorpade
# Location: Earth
# Date: 28/03/2022

# static method in python

# Create class Employee
class Employee:
    company = "Google"

    def getSalary(self, signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")

    # Static methods
    # Sometimes we need a function that doesn’t use the self-parameter. We can define a static method like this:
    @staticmethod   # method decorator
    def greet():
        print("Good Morning, Sir")

    @staticmethod   # method decorator
    def time():
        print("The time is 9AM in the morning")

Darshan = Employee()
Darshan.salary = 100000
Darshan.getSalary("Thanks!") # Employee.getSalary(Darshan)
Darshan.greet() # Employee.greet()
Darshan.time()