# Author: Darshan Ghorpade
# Location: Earth
# Date: 29/03/2022

# Q. Create a class C-2d vector and use it to create another class representing a 3-d vector.

class C2dVed:
    def __init__(self, i, j):
        self.icap = i
        self.jcap = j

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"

class C3dVed(C2dVed):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.kcap = k

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"

v2d = C2dVed(1, 3)
v3d = C3dVed(1, 9, 7)

print(v2d)
print(v3d)