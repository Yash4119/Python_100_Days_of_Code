# Method Overriding in Python

class shape:
    def __init__(self, length, width) -> None:
        self.len = length
        self.width = width

    def area(self):
        print(f"This is the Area function ")
        return self.len*self.width


class rectangle(shape):
    def __init__(self, length, width) -> None:
        super().__init__(length, width)

    def area(self):
        return super().area()

class circle(shape):
    def __init__(self, radius) -> None:
        super().__init__(radius, radius)

    def area(self):
        return 3.14 * super().area()

sh = shape(4,4)
print(sh.area())

rec = rectangle(2,3)
print(rec.area())

cir = circle(3)
print(cir.area())