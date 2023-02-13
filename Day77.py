# Operator Overloading in python

# Dunder methods can be used to perfrom operator overloading in PYthon.

class Vector:
    def __init__(self, i, j, k) -> None:
        self.i = i
        self.j = j
        self.k = k
    
    def __str__(self) -> str:
        return f"{self.i}i + {self.j}j + {self.k}k"

    # Here we perform operator overloading for perform addition of vectors
    def __add__(self, v2):
        return Vector(self.i+v2.i, self.j+v2.j, self.k+v2.k)

v1 = Vector(2,3,4)
print(v1)

v2 = Vector(3,4,5)
print(v2)

v3 = v1 + v2;
print(v3)
print(type(v3))