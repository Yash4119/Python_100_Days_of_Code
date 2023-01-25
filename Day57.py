# Classes and Objects In Python

class person:
    name = "Harry"
    age = 20
    job = "SDE"

    # self defines the object on which the method is been called
    def show(self):
        print(f"{self.name} is a {self.job}")

a = person()
print(a.name)
a.name = "Teja"
print(a.name," ",a.age)
a.show()

b = person()
b.name = "Yash"
b.job = "CEO"

a.show()
b.show()
