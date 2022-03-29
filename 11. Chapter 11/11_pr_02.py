# Author: Darshan Ghorpade
# Location: Earth
# Date: 29/03/2022

# Q. Create a class of pets from a class Animals and further create class Dog from Pets. Add a method bark to class Dog.

class Animal:
    animalType = "Mammal"

class Pets(Animal):
    color = "White"

class Dog(Pets):
    @staticmethod 
    def bark():
        print("Bow Bow!")

d = Dog()
d.bark()