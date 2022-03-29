# Author: Darshan Ghorpade
# Location: Earth
# Date: 29/03/2022

# 2. Multiple inheritance
# Multiple inheritances occurs when the child class inherits from more than one parent class.

class Employee:
    company = "VISA"
    eCode = 120

class Freelancer:
    company = "Fiverr"
    level = 0

    def upgradeLevel(self):
        self.level = self.level + 1

class Programmer(Employee, Freelancer):
    name = "Darshan"

p = Programmer()
p.upgradeLevel()
print(p.company)
print(p.level)