# Author: Darshan Ghorpade
# Location: Earth
# Date: 29/03/2022

# Other dunder methods in Python

'''
__str__() -> used  to set what gets displayed upon calling str(obj)

__len__() -> used to set what gets displayed upon calling .__len__() or len(obj)

'''

class Number:
    def __init__(self, num):
        self.num = num
    
    def __add__(self, num2):
        print("Lets add")
        return self.num + num2.num

    def __str__(self):
        print(f"Decimal Number: {self.num}")
        
    def __len__(self):
        return 1

n = Number(9)
print(9)
print(len(n))