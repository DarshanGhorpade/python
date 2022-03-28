# Author: Darshan Ghorpade
# Location: Earth
# Date: 28/03/2022

# Q. Create a class programmer for storing information of a few programmers working at Microsoft.

# Create class Programmer

class Programmer:
    company = "Microsoft"

    # Constructor
    def __init__(self, name, product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(f"The name of the {self.company} programmer is {self.name} and the product is {self.product}")

Darshan = Programmer("Darshan", "Skype")
Alka = Programmer("Alka", "Github")
Darshan.getInfo()
Alka.getInfo()