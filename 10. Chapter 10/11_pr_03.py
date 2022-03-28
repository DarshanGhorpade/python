# Author: Darshan Ghorpade
# Location: Earth
# Date: 28/03/2022

# Q. Create a class with a class attribute a; create an object from it and set a directly 
# using object.a=0 Does this change the class attribute? -> No

class Sample:
    a = "Darshan"

obj = Sample()
obj.a = "Vikky" # instance attribute
# Sample.a = "Vikky"

print(Sample.a)
print(obj.a)