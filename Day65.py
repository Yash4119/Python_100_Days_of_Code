# Static Methods in Python

# Static methods need not be instantiated. they can be used to implement utility functions within a class
# Static methods do not consists of self keyword. static methods are not associated with the class
# Static methods can be invoked using class name

class Math:
    def __init__(self, num):
        self.num = num
    
    def addToNum(self , a):
        self.num += self.add(a,a) + a

    @staticmethod
    def add(a, b):
        return a+b

obj = Math(10)
print(obj.num)

obj.addToNum(12)

print(obj.num)

print(obj.add(2,2))
print(Math.add(2,2))