# Author: Darshan Ghorpade
# Location: Earth
# Date: 25/03/2022

# Q. Write a python program using the function to convert Celsius to Fahrenheit.

def fahrenheit(celcius):
    return (celcius*(9/5))+32

celcius = float(input("Enter temperature: "))

print("fahrenheit temperature of "+ str(celcius) + "°C is " + str(fahrenheit(celcius)) + "°F")