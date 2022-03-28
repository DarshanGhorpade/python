# Author: Darshan Ghorpade
# Location: Earth
# Date: 28/03/2022

# self parameter
# self refers to the instance of the class.
# It is automatically passed with a function call from an object.

# Create class employee
class Employee:
    company = "Google"
    def getSalary(self):
        # print("Salary is 100k")
        print(f"Salary of employee working in {self.company} is {self.salary}")

Darshan = Employee()
Darshan.salary = 100000
# Darshan.getSalary()   # here, self is Darshan, and the above line of code is equivalent to Employee.getSalary(harry)
Employee.getSalary(Darshan)