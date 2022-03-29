# Author: Darshan Ghorpade
# Location: Earth
# Date: 29/03/2022

# @property decorators in Python
'''
Consider the following class

class Employee:
	@property 
	def name(self):
		return self.ename
if e = Employee() is an object of class employee, we can print (e.name) top print the ename/call name() function.
'''

# @.getters and @.setters
# The method name with @property decorator is called getter method.
# We can define a function + @name.setter decorator like below:
'''
@name.setter
def name(self, value):
	self.ename = value
'''

class Employee:
    company = "Bharat Gas"
    salary = 4500
    salaryBonus = 500
    # totalSalary = 5000

    @property   # property decorator
    def totalSalary(self):
        return self.salary + self.salaryBonus

    @totalSalary.setter
    def totalSalary(self, val):
        self.salaryBonus = val - self.salary

e = Employee()
print(e.totalSalary)

e.totalSalary = 9000
print(e.salary)
print(e.totalSalary)