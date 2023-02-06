# Object introspection methods dir, __dict__ and help

'''
Object introspection methods are basically used to find info about the objects of a class
# mthods used for this purpose are
1. dir
2. __dict__
3. help
'''


nums = [1,2,3,4]

# dir function gives all the info regarding the object
print(dir(nums))

# also we can find info about a particular function that can act on a list nums
print(nums.__add__)

'''
__methodName__ are called as dunder methods that help us know more about the methods
'''


'''
__dict__ method basically allows us to know about the methods and variables declared or assigned values for a object/instance of a class in the form of a dictionary
'''

class person:
    def __init__(self, name, age, id) -> None:
        self.name = name
        self.age = age
        self.id = id

p1 = person("Yash Jayram Ambekar", 21, "03")
print(p1.__dict__)

# Help method gives conplete description of an object as an documentation

print(help(person))