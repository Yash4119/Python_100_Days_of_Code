# Constructors in Python

'''
A constructor is a special method in a class that is used to initialize the objects in a class
A constructor is automatically invoked when an object of a class is created.

1. Parameterized constructor
2. Default Constructor
3. Copy Constructor
'''

class student:
        
    def __init__(self):
        self.name = "Default"
        self.age = 21
        self.std = "B"
    
    def info(self):
        print(self.name," is ",self.age," years old and is in standard ",self.std)


a = student()
a.name = "Yash"
a.std = "A"

b = student()
b.name = "Omkar"
b.std = "B"

c = student()

a.info()
b.info()
c.info()