# Author: Darshan Ghorpade
# Location: Earth
# Date: 29/03/2022

# Class methods
# A class method is a method which is bound to the class and not the object of the class.
# @classmethod decorator is used to create a class method.

class Employee:
    company = "Camel"
    salary = 100
    location = "Delhi"

    # def changeSalary(self, sal):
    #     self.__class__.salary = sal

    @classmethod    # decorator is function which takes function as input and modify it
    def changeSalary(cls, sal):
        cls.salary = sal

e = Employee()
print(e.salary)
e.changeSalary(455)
print(e.salary)
print(Employee.salary)