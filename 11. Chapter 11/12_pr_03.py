# Author: Darshan Ghorpade
# Location: Earth
# Date: 29/03/2022

# Q. Create a class Employee and add salary and increment properties to it.
#    Write a method SalaryAfterIncrement method with a @property decorator with a setter 
#    which changes the value of increment based on the salary.

class Employee:
    salary = 10000
    increment = 1.5

    @property
    def salaryAfterIncrement(self):
        return self.salary * self.increment
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, sai):
        self.increment = sai / self.salary

e = Employee()
print("Salary after increment:", e.salaryAfterIncrement)

print(e.increment)
e.salaryAfterIncrement = 20000
print(e.increment)