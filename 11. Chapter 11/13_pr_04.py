# Author: Darshan Ghorpade
# Location: Earth
# Date: 29/03/2022

# Q. Write a class complex to represent complex numbers, along with overloaded operators + and * which adds and multiplies them.

# (a+bi) + (c+di) = (a+c) + (b+d)i

# (a+bi)(c+di) = (ac−bd) + (ad+bc)i


class Complex:
    def __init__(self, r, i):
        self.real = r
        self.imaginary = i

    def __add__(self, c):
        return Complex(self.real + c.real, self.imaginary + self.imaginary)

    def __mul__(self, c):
        mulReal = self.real*c.real - self.imaginary*c.imaginary
        mulImg = self.real*c.imaginary + self.imaginary*c.real
        return Complex(mulReal, mulImg)

    def __str__(self):
        if self.imaginary < 0:
            return f"{self.real} - {-self.imaginary}i"
        else:
            return f"{self.real} + {-self.imaginary}i"

c1 = Complex(1, -4)
c2 = Complex(8, -5)

print(c1+c2)
print(c1*c2)