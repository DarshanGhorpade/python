# Author: Darshan Ghorpade
# Location: Earth
# Date: 28/03/2022

# Q. Can you change the self parameter inside a class to something else (say ‘harry’)? 
# Try changing self to ‘slf’ or ‘harry’ and see the effects.

# This work, but while working with team you should follow some basic code rules

class Sample: 
    def __init__(slf, name):
        slf.name = name

obj = Sample("Darshan") 
print(obj.name)