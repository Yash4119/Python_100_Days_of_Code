# Access Specifiers in Python

'''
Python do not have public private and protected access modifiers

By default the access modifier is public

giving double underscore ( __ ) in front of variable the variable is declared as private
however, there is not any strict access restricter in python.

=> private variable can be accessed as _ClassName__variableName;
This is called name Mangling in Python.

=> single underscore in front of variable or method ( _variableName ) represents the protected variables and methods.
'''

class Employee:
    __eid = 0
    name = ""

    def __init__(self, eid, name):
        self.__eid = eid
        self.name = name
    

emp = Employee(23,"Yash Ambekar")

print(emp._Employee__eid)       # name mangling took place over here
print(emp.name)