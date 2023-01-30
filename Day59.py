# Decorators in Python

'''
Decorators are the functcions that take a function as an argument and return a new function
An easy way to modify an existing function
'''

def greet(fx):
    def mfx(*args, **kwargs):
        print("Good morning from Harry Bhai!!")
        fx(*args, **kwargs)
        print("Thank you using the Program")
    return mfx

@greet
def show(a,b):
    print(f"sum of {a} and {b} is :- ",a+b)


show(3,5)
greet(show)(5,6)
