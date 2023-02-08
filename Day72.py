# Magic methods / Dunder methods in Python

'''
1. __init__    :-   Basically returns a contructor which is invoked on instantiation of an class instance.
2. __len__     :-   Returns the length of the object for which it is called.
3. __str__     :-   Returns an human readable string information about the object.
4. __repr__    :-   This method is called whenever we try to print an object of the class.
5. __call__    :-   Used to call a method with the instance without actually creating a method for it in the class.
'''

from Day71 import programmer

p = programmer("Yash",213,"C++")

print(len(p))
print(str(p))
print(repr(p))
print(p(1))
